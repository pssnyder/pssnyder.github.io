#!/usr/bin/env python3
"""
Repository Analysis Tool for Chess Engine Documentation Project

This script analyzes the chess engine repositories to extract:
- Commit history and milestones
- Documentation files across different versions
- Test results and performance data
- Timeline of development

Usage:
    python scripts/analyze_repos.py
"""

import os
import json
import subprocess
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

class RepoAnalyzer:
    def __init__(self, base_dir="repos"):
        self.base_dir = Path(base_dir)
        self.repos = {
            "v7p3r": "https://github.com/pssnyder/v7p3r-chess-engine",
            "slowmate": "https://github.com/pssnyder/slowmate-chess-engine", 
            "c0br4": "https://github.com/pssnyder/c0br4-chess-engine",
            "engine-tester": "https://github.com/pssnyder/engine-tester",
            "engine-metrics": "https://github.com/pssnyder/engine-metrics"
        }
        self.analysis_results = {}
    
    def clone_repos(self):
        """Clone all repositories for analysis"""
        self.base_dir.mkdir(exist_ok=True)
        
        for name, url in self.repos.items():
            repo_path = self.base_dir / name
            if not repo_path.exists():
                print(f"Cloning {name}...")
                subprocess.run(["git", "clone", url, str(repo_path)], 
                             check=True, capture_output=True)
            else:
                print(f"Repository {name} already exists, pulling latest...")
                subprocess.run(["git", "-C", str(repo_path), "pull"], 
                             capture_output=True)
    
    def extract_commit_history(self, repo_name):
        """Extract commit history with metadata"""
        repo_path = self.base_dir / repo_name
        
        # Get commit log with format: hash|date|author|subject|files
        cmd = [
            "git", "-C", str(repo_path), "log", 
            "--pretty=format:%H|%ai|%an|%s",
            "--name-only"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        commits = []
        
        lines = result.stdout.split('\n')
        i = 0
        while i < len(lines):
            if '|' in lines[i]:
                parts = lines[i].split('|')
                if len(parts) >= 4:
                    commit = {
                        'hash': parts[0],
                        'date': parts[1],
                        'author': parts[2],
                        'subject': parts[3],
                        'files': []
                    }
                    
                    # Get files changed in this commit
                    i += 1
                    while i < len(lines) and lines[i] and '|' not in lines[i]:
                        if lines[i].strip():
                            commit['files'].append(lines[i].strip())
                        i += 1
                    
                    commits.append(commit)
                else:
                    i += 1
            else:
                i += 1
        
        return commits
    
    def find_documentation_files(self, repo_name):
        """Find all .md files across all commits"""
        repo_path = self.base_dir / repo_name
        
        # Find all .md files that ever existed
        cmd = ["git", "-C", str(repo_path), "log", "--all", "--name-only", "--pretty=format:", "*.md"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        md_files = set()
        for line in result.stdout.split('\n'):
            if line.strip() and line.endswith('.md'):
                md_files.add(line.strip())
        
        # For each .md file, find when it was created/modified
        file_history = {}
        for md_file in md_files:
            cmd = ["git", "-C", str(repo_path), "log", "--follow", "--pretty=format:%H|%ai|%s", "--", md_file]
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
            
            commits = []
            for line in result.stdout.split('\n'):
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        commits.append({
                            'hash': parts[0],
                            'date': parts[1],
                            'subject': parts[2]
                        })
            
            if commits:
                file_history[md_file] = commits
        
        return file_history
    
    def find_test_results(self, repo_name):
        """Find all .json files containing test results"""
        repo_path = self.base_dir / repo_name
        
        # Find all .json files
        cmd = ["git", "-C", str(repo_path), "log", "--all", "--name-only", "--pretty=format:", "*.json"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        json_files = set()
        for line in result.stdout.split('\n'):
            if line.strip() and line.endswith('.json'):
                json_files.add(line.strip())
        
        return list(json_files)
    
    def identify_milestones(self, commits):
        """Identify milestone commits based on patterns"""
        milestones = []
        
        milestone_patterns = [
            r'v\d+\.\d+',  # Version numbers
            r'release',
            r'milestone',
            r'major',
            r'breakthrough',
            r'optimization',
            r'tournament',
            r'benchmark',
            r'performance',
            r'algorithm',
            r'search',
            r'evaluation'
        ]
        
        for commit in commits:
            subject_lower = commit['subject'].lower()
            for pattern in milestone_patterns:
                if re.search(pattern, subject_lower):
                    commit['milestone'] = True
                    milestones.append(commit)
                    break
        
        return milestones
    
    def filter_commit_messages(self, commits):
        """Filter and clean commit messages for professional presentation"""
        filtered = []
        
        # Patterns to filter out or clean up
        skip_patterns = [
            r'^\s*$',  # Empty messages
            r'^\.+$',  # Just dots
            r'^fix$',  # Too vague
            r'^update$',  # Too vague
            r'^wip',   # Work in progress
        ]
        
        cleanup_patterns = [
            (r'\bfuck\b', 'fix'),
            (r'\bshit\b', 'issue'),
            (r'\bdamn\b', 'darn'),
            (r'\bwtf\b', 'what'),
            (r'\bugh\b', ''),
        ]
        
        for commit in commits:
            subject = commit['subject']
            
            # Skip obviously unprofessional or empty commits
            skip = False
            for pattern in skip_patterns:
                if re.search(pattern, subject, re.IGNORECASE):
                    skip = True
                    break
            
            if skip:
                continue
            
            # Clean up language
            cleaned_subject = subject
            for pattern, replacement in cleanup_patterns:
                cleaned_subject = re.sub(pattern, replacement, cleaned_subject, flags=re.IGNORECASE)
            
            # Add to filtered list if it's substantive
            if len(cleaned_subject.strip()) > 5:  # At least 5 characters
                commit['original_subject'] = subject
                commit['cleaned_subject'] = cleaned_subject.strip()
                filtered.append(commit)
        
        return filtered
    
    def analyze_all_repos(self):
        """Run complete analysis on all repositories"""
        print("Starting repository analysis...")
        
        # Clone repositories
        self.clone_repos()
        
        # Analyze each repository
        for repo_name in self.repos.keys():
            print(f"\nAnalyzing {repo_name}...")
            
            # Extract commit history
            commits = self.extract_commit_history(repo_name)
            print(f"  Found {len(commits)} commits")
            
            # Filter commits
            filtered_commits = self.filter_commit_messages(commits)
            print(f"  {len(filtered_commits)} commits after filtering")
            
            # Identify milestones
            milestones = self.identify_milestones(filtered_commits)
            print(f"  Identified {len(milestones)} milestone commits")
            
            # Find documentation
            docs = self.find_documentation_files(repo_name)
            print(f"  Found {len(docs)} documentation files")
            
            # Find test results
            json_files = self.find_test_results(repo_name)
            print(f"  Found {len(json_files)} JSON files")
            
            self.analysis_results[repo_name] = {
                'commits': filtered_commits,
                'milestones': milestones,
                'documentation': docs,
                'test_results': json_files,
                'total_commits': len(commits),
                'filtered_commits': len(filtered_commits)
            }
        
        return self.analysis_results
    
    def save_analysis(self, output_file="analysis_results.json"):
        """Save analysis results to JSON file"""
        with open(output_file, 'w') as f:
            json.dump(self.analysis_results, f, indent=2, default=str)
        print(f"Analysis results saved to {output_file}")
    
    def generate_timeline(self):
        """Generate a unified timeline across all repositories"""
        all_milestones = []
        
        for repo_name, data in self.analysis_results.items():
            for milestone in data['milestones']:
                milestone['repo'] = repo_name
                all_milestones.append(milestone)
        
        # Sort by date
        all_milestones.sort(key=lambda x: x['date'])
        
        return all_milestones
    
    def create_content_suggestions(self):
        """Generate suggestions for journal entries and analysis"""
        suggestions = {
            'journal_entries': [],
            'technical_analysis': [],
            'notebooks': []
        }
        
        # Generate journal entry suggestions from milestones
        timeline = self.generate_timeline()
        
        for milestone in timeline:
            entry = {
                'title': f"{milestone['repo'].upper()}: {milestone['cleaned_subject']}",
                'date': milestone['date'][:10],  # Just the date part
                'repo': milestone['repo'],
                'commit_hash': milestone['hash'],
                'content_type': 'journal_entry'
            }
            suggestions['journal_entries'].append(entry)
        
        # Generate technical analysis suggestions
        for repo_name, data in self.analysis_results.items():
            if data['test_results']:
                analysis = {
                    'title': f"{repo_name.upper()} Performance Analysis",
                    'description': f"Comprehensive analysis of {repo_name} engine performance data",
                    'data_sources': data['test_results'],
                    'content_type': 'notebook'
                }
                suggestions['notebooks'].append(analysis)
        
        return suggestions

def main():
    analyzer = RepoAnalyzer()
    
    # Run complete analysis
    results = analyzer.analyze_all_repos()
    
    # Save results
    analyzer.save_analysis()
    
    # Generate timeline
    timeline = analyzer.generate_timeline()
    print(f"\nGenerated timeline with {len(timeline)} milestones")
    
    # Generate content suggestions
    suggestions = analyzer.create_content_suggestions()
    print(f"Generated {len(suggestions['journal_entries'])} journal entry suggestions")
    print(f"Generated {len(suggestions['notebooks'])} notebook suggestions")
    
    # Save suggestions
    with open('content_suggestions.json', 'w') as f:
        json.dump(suggestions, f, indent=2, default=str)
    
    print("\nAnalysis complete! Check analysis_results.json and content_suggestions.json")

if __name__ == "__main__":
    main()
