#!/usr/bin/env python3
"""
Content Generator for Chess Engine Documentation Project

This script generates Jekyll-compatible content from repository analysis:
- Journal entries from milestone commits
- Technical analysis notebooks from performance data
- Project documentation from README files

Usage:
    python scripts/generate_content.py
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess

class ContentGenerator:
    def __init__(self, analysis_file="analysis_results.json", suggestions_file="content_suggestions.json"):
        self.analysis_file = analysis_file
        self.suggestions_file = suggestions_file
        self.posts_dir = Path("_posts")
        self.notebooks_dir = Path("_notebooks")
        self.projects_dir = Path("_projects")
        
        # Create directories if they don't exist
        self.posts_dir.mkdir(exist_ok=True)
        self.notebooks_dir.mkdir(exist_ok=True)
        self.projects_dir.mkdir(exist_ok=True)
        
        self.analysis_data = {}
        self.suggestions = {}
        
        # Load data if files exist
        if os.path.exists(analysis_file):
            with open(analysis_file) as f:
                self.analysis_data = json.load(f)
        
        if os.path.exists(suggestions_file):
            with open(suggestions_file) as f:
                self.suggestions = json.load(f)
    
    def sanitize_filename(self, title, date_str=None):
        """Convert title to Jekyll-compatible filename"""
        if date_str:
            date_part = datetime.fromisoformat(date_str.replace('Z', '+00:00')).strftime('%Y-%m-%d')
        else:
            date_part = datetime.now().strftime('%Y-%m-%d')
        
        # Clean title for filename
        clean_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
        clean_title = re.sub(r'\s+', '-', clean_title.strip())
        clean_title = clean_title.lower()
        
        # Limit filename length (Windows has 260 char limit, leave room for path)
        max_title_length = 80
        if len(clean_title) > max_title_length:
            clean_title = clean_title[:max_title_length].rstrip('-')
        
        return f"{date_part}-{clean_title}.md"
    
    def generate_jekyll_frontmatter(self, title, date, layout="post", **kwargs):
        """Generate Jekyll front matter for posts"""
        # Parse date if it's a string
        if isinstance(date, str):
            try:
                dt = datetime.fromisoformat(date.replace('Z', '+00:00'))
            except:
                dt = datetime.now()
        else:
            dt = date
        
        frontmatter = f"""---
layout: {layout}
title: "{title}"
date: {dt.strftime('%Y-%m-%d %H:%M:%S %z')}
author: Pat Snyder
categories: chess-engine development
tags: [{', '.join(kwargs.get('tags', []))}]
"""
        
        # Add optional fields
        if 'repo' in kwargs:
            frontmatter += f"repo: {kwargs['repo']}\n"
        if 'commit_hash' in kwargs:
            frontmatter += f"commit: {kwargs['commit_hash']}\n"
        if 'excerpt' in kwargs:
            frontmatter += f"excerpt: \"{kwargs['excerpt']}\"\n"
        
        frontmatter += "---\n\n"
        return frontmatter
    
    def get_commit_details(self, repo_name, commit_hash):
        """Get detailed information about a specific commit"""
        repo_path = Path("repos") / repo_name
        
        if not repo_path.exists():
            return None
        
        # Get commit details
        cmd = ["git", "-C", str(repo_path), "show", "--stat", commit_hash]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        if result.returncode != 0:
            return None
        
        return {
            'diff_stat': result.stdout,
            'repo_path': repo_path
        }
    
    def get_file_content_at_commit(self, repo_name, commit_hash, file_path):
        """Get content of a file at a specific commit"""
        repo_path = Path("repos") / repo_name
        
        cmd = ["git", "-C", str(repo_path), "show", f"{commit_hash}:{file_path}"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        if result.returncode == 0:
            return result.stdout
        return None
    
    def generate_journal_entry(self, suggestion):
        """Generate a journal entry from a milestone commit"""
        repo_name = suggestion['repo']
        commit_hash = suggestion['commit_hash']
        title = suggestion['title']
        date = suggestion['date']
        
        # Get commit details
        commit_details = self.get_commit_details(repo_name, commit_hash)
        
        # Find the actual commit data
        commit_data = None
        if repo_name in self.analysis_data:
            for commit in self.analysis_data[repo_name]['milestones']:
                if commit['hash'] == commit_hash:
                    commit_data = commit
                    break
        
        if not commit_data:
            return None
        
        # Generate content
        content = self.generate_jekyll_frontmatter(
            title=title,
            date=date,
            repo=repo_name,
            commit_hash=commit_hash[:8],
            tags=[repo_name, 'milestone', 'development'],
            excerpt=f"Development milestone in {repo_name}: {commit_data.get('cleaned_subject', '')}"
        )
        
        content += f"# {title}\n\n"
        content += f"**Repository:** [{repo_name}](https://github.com/pssnyder/{repo_name})\n"
        content += f"**Commit:** [`{commit_hash[:8]}`](https://github.com/pssnyder/{repo_name}/commit/{commit_hash})\n"
        content += f"**Date:** {date}\n\n"
        
        content += "## Overview\n\n"
        content += f"{commit_data.get('cleaned_subject', 'Development milestone')}\n\n"
        
        if commit_details and commit_details['diff_stat']:
            content += "## Changes\n\n"
            content += "```\n"
            # Extract just the file change summary, not the full diff
            lines = commit_details['diff_stat'].split('\n')
            for line in lines:
                if 'file' in line and 'changed' in line:
                    content += line + '\n'
                elif '|' in line and ('+' in line or '-' in line):
                    content += line + '\n'
            content += "```\n\n"
        
        # Add context about the files changed
        if commit_data.get('files'):
            content += "## Files Modified\n\n"
            for file_path in commit_data['files'][:10]:  # Limit to first 10 files
                content += f"- `{file_path}`\n"
            
            if len(commit_data['files']) > 10:
                content += f"- ... and {len(commit_data['files']) - 10} more files\n"
            content += "\n"
        
        # Add development notes section
        content += "## Development Notes\n\n"
        content += f"This milestone represents a significant step in the evolution of the {repo_name} chess engine. "
        
        # Add some context based on the commit message
        subject_lower = commit_data.get('cleaned_subject', '').lower()
        if 'search' in subject_lower:
            content += "The changes focus on search algorithm improvements, which are crucial for engine strength.\n\n"
        elif 'eval' in subject_lower or 'evaluation' in subject_lower:
            content += "The modifications enhance the position evaluation system, affecting how the engine assesses chess positions.\n\n"
        elif 'optimization' in subject_lower or 'performance' in subject_lower:
            content += "These optimizations should improve engine performance and playing strength.\n\n"
        elif 'bug' in subject_lower or 'fix' in subject_lower:
            content += "Bug fixes and stability improvements help ensure reliable engine operation.\n\n"
        else:
            content += "These changes contribute to the overall development and refinement of the engine.\n\n"
        
        content += "## Next Steps\n\n"
        content += "- Continue monitoring engine performance\n"
        content += "- Test changes against benchmark positions\n"
        content += "- Consider additional optimizations\n\n"
        
        content += "---\n\n"
        content += f"*This entry was generated from commit analysis of the {repo_name} repository.*\n"
        
        return content
    
    def generate_performance_notebook(self, suggestion):
        """Generate a Jupyter notebook for performance analysis"""
        repo_name = suggestion['title'].split()[0].lower()
        
        # Basic notebook structure with proper outputs for each code cell
        notebook = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"# {suggestion['title']}\n",
                        "\n",
                        f"{suggestion['description']}\n",
                        "\n",
                        f"**Author:** Pat Snyder  \n",
                        f"**Date:** {datetime.now().strftime('%Y-%m-%d')}  \n",
                        f"**Repository:** {repo_name}\n",
                        "\n",
                        "## Overview\n",
                        "\n",
                        f"This notebook analyzes the performance data from the {repo_name} chess engine, "
                        "examining various metrics and trends over the development timeline.\n"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "import json\n",
                        "import pandas as pd\n",
                        "import matplotlib.pyplot as plt\n",
                        "import seaborn as sns\n",
                        "from pathlib import Path\n",
                        "\n",
                        "# Set up plotting style\n",
                        "plt.style.use('dark_background')\n",
                        "sns.set_palette('viridis')\n",
                        "\n",
                        f"print(f'Analysis notebook for {repo_name} engine')"
                    ]
                },
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Data Loading\n",
                        "\n",
                        "Load and examine the available test results and performance data."
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# Load test results\n",
                        "data_files = [\n"
                    ] + [f"    'repos/{repo_name}/{file}',\n" for file in suggestion.get('data_sources', [])] + [
                        "]\n",
                        "\n",
                        "test_data = {}\n",
                        "for file_path in data_files:\n",
                        "    if Path(file_path).exists():\n",
                        "        with open(file_path) as f:\n",
                        "            try:\n",
                        "                test_data[Path(file_path).name] = json.load(f)\n",
                        "                print(f'Loaded: {file_path}')\n",
                        "            except json.JSONDecodeError:\n",
                        "                print(f'Error loading: {file_path}')\n",
                        "    else:\n",
                        "        print(f'File not found: {file_path}')\n",
                        "\n",
                        "print(f'\\nLoaded {len(test_data)} data files')"
                    ]
                },
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Performance Analysis\n",
                        "\n",
                        "Analyze the engine performance metrics and visualize trends."
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# Placeholder for performance analysis\n",
                        "# This will be customized based on the actual data structure\n",
                        "\n",
                        "for filename, data in test_data.items():\n",
                        "    print(f'\\n=== {filename} ===')\n",
                        "    if isinstance(data, dict):\n",
                        "        print(f'Keys: {list(data.keys())}')\n",
                        "    elif isinstance(data, list):\n",
                        "        print(f'List with {len(data)} items')\n",
                        "        if data and isinstance(data[0], dict):\n",
                        "            print(f'Sample keys: {list(data[0].keys())}')\n",
                        "    else:\n",
                        "        print(f'Type: {type(data)}')"
                    ]
                },
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## Conclusions\n",
                        "\n",
                        "Summary of findings and next steps for engine development."
                    ]
                },
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "### Key Findings\n",
                        "\n",
                        "- TODO: Add specific performance insights\n",
                        "- TODO: Identify optimization opportunities\n",
                        "- TODO: Compare with baseline metrics\n",
                        "\n",
                        "### Recommendations\n",
                        "\n",
                        "- TODO: Suggest areas for improvement\n",
                        "- TODO: Prioritize development efforts\n",
                        "- TODO: Set performance targets\n",
                        "\n",
                        "---\n",
                        "\n",
                        "*This analysis notebook was generated automatically from repository data.*"
                    ]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.x"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        return json.dumps(notebook, indent=2)
    
    def generate_notebook_markdown(self, suggestion):
        """Generate a markdown file for notebook content that Jekyll can process"""
        repo_name = suggestion['title'].split()[0].lower()
        
        frontmatter = self.generate_jekyll_frontmatter(
            title=suggestion['title'],
            date=datetime.now(),
            layout="notebook",
            tags=[repo_name, 'performance-analysis', 'notebook'],
            excerpt=suggestion['description'],
            notebook_type="Performance Analysis",
            github_repo=f"https://github.com/pssnyder/{repo_name}",
            technologies=["Python", "Pandas", "Matplotlib", "Seaborn"]
        )
        
        content = frontmatter
        content += f"# {suggestion['title']}\n\n"
        content += f"{suggestion['description']}\n\n"
        content += f"**Repository:** [{repo_name}](https://github.com/pssnyder/{repo_name})\n\n"
        
        content += "## Overview\n\n"
        content += f"This analysis examines the performance data from the {repo_name} chess engine, "
        content += "tracking metrics and trends throughout the development process.\n\n"
        
        content += "## Data Sources\n\n"
        if suggestion.get('data_sources'):
            content += "The analysis draws from the following data files:\n\n"
            for source in suggestion['data_sources'][:10]:  # Limit to first 10
                content += f"- `{source}`\n"
            if len(suggestion['data_sources']) > 10:
                content += f"- ... and {len(suggestion['data_sources']) - 10} more files\n"
        else:
            content += "Performance data files from the repository will be analyzed.\n"
        content += "\n"
        
        content += "## Analysis Objectives\n\n"
        content += "This notebook aims to:\n\n"
        content += "- **Load and examine** performance test results\n"
        content += "- **Visualize trends** in engine performance over time\n"
        content += "- **Identify patterns** in optimization efforts\n"
        content += "- **Compare metrics** across different engine versions\n"
        content += "- **Generate insights** for future development priorities\n\n"
        
        content += "## Key Metrics\n\n"
        content += f"The {repo_name} engine performance analysis typically includes:\n\n"
        content += "- **Search Speed**: Nodes per second evaluation\n"
        content += "- **Search Depth**: Average and maximum depth reached\n"
        content += "- **Move Quality**: Tactical accuracy and positional understanding\n"
        content += "- **Time Management**: Efficiency in time allocation\n"
        content += "- **Memory Usage**: Resource utilization patterns\n\n"
        
        content += "## Interactive Analysis\n\n"
        content += "```python\n"
        content += "# Sample analysis code\n"
        content += "import json\n"
        content += "import pandas as pd\n"
        content += "import matplotlib.pyplot as plt\n"
        content += "import seaborn as sns\n"
        content += "from pathlib import Path\n\n"
        content += "# Set up plotting style for dark theme\n"
        content += "plt.style.use('dark_background')\n"
        content += "sns.set_palette('viridis')\n\n"
        content += f"print('Analysis notebook for {repo_name} engine')\n"
        content += "```\n\n"
        
        content += "## Results Summary\n\n"
        content += "This section will be populated with findings once the analysis is executed.\n\n"
        content += "### Performance Trends\n\n"
        content += "- Engine performance progression over development timeline\n"
        content += "- Impact of major algorithm changes\n"
        content += "- Optimization effectiveness\n\n"
        
        content += "### Recommendations\n\n"
        content += "Based on the performance data analysis:\n\n"
        content += "- Areas showing the most improvement potential\n"
        content += "- Suggested optimization priorities\n"
        content += "- Performance targets for future versions\n\n"
        
        content += "---\n\n"
        content += "*This performance analysis was generated from automated repository data mining.*\n"
        
        return content
    
    def generate_project_overview(self, repo_name):
        """Generate a project overview page"""
        repo_data = self.analysis_data.get(repo_name, {})
        
        frontmatter = self.generate_jekyll_frontmatter(
            title=f"{repo_name.upper()} Chess Engine",
            date=datetime.now(),
            layout="project",
            tags=[repo_name, 'chess-engine', 'project'],
            excerpt=f"Overview of the {repo_name} chess engine development project"
        )
        
        content = frontmatter
        content += f"# {repo_name.upper()} Chess Engine\n\n"
        content += f"**Repository:** [pssnyder/{repo_name}](https://github.com/pssnyder/{repo_name})\n\n"
        
        # Add project statistics
        if repo_data:
            content += "## Project Statistics\n\n"
            content += f"- **Total Commits:** {repo_data.get('total_commits', 'Unknown')}\n"
            content += f"- **Milestone Commits:** {len(repo_data.get('milestones', []))}\n"
            content += f"- **Documentation Files:** {len(repo_data.get('documentation', {}))}\n"
            content += f"- **Data Files:** {len(repo_data.get('test_results', []))}\n\n"
        
        content += "## Overview\n\n"
        content += f"The {repo_name} chess engine represents a significant development effort in chess AI programming. "
        content += "This project showcases various algorithms and optimization techniques used in modern chess engines.\n\n"
        
        content += "## Key Features\n\n"
        content += "- Advanced search algorithms\n"
        content += "- Sophisticated position evaluation\n"
        content += "- Performance optimization\n"
        content += "- Comprehensive testing framework\n\n"
        
        # Add milestone timeline
        if repo_data and repo_data.get('milestones'):
            content += "## Development Timeline\n\n"
            milestones = sorted(repo_data['milestones'], key=lambda x: x['date'])
            for milestone in milestones[-5:]:  # Last 5 milestones
                date = milestone['date'][:10]
                subject = milestone.get('cleaned_subject', milestone.get('subject', ''))
                commit_hash = milestone['hash'][:8]
                content += f"- **{date}** - {subject} ([`{commit_hash}`](https://github.com/pssnyder/{repo_name}/commit/{milestone['hash']}))\n"
            content += "\n"
        
        content += "## Documentation\n\n"
        if repo_data and repo_data.get('documentation'):
            for doc_file in list(repo_data['documentation'].keys())[:5]:  # First 5 docs
                content += f"- [{doc_file}](https://github.com/pssnyder/{repo_name}/blob/main/{doc_file})\n"
            content += "\n"
        else:
            content += "Project documentation is available in the repository.\n\n"
        
        content += "## Performance Data\n\n"
        if repo_data and repo_data.get('test_results'):
            content += "The project includes comprehensive performance testing and benchmarking:\n\n"
            for test_file in repo_data['test_results'][:3]:  # First 3 test files
                content += f"- `{test_file}`\n"
            content += "\n"
        else:
            content += "Performance metrics and test results are tracked throughout development.\n\n"
        
        content += "## Related Content\n\n"
        content += f"- [Development Journal Entries](/categories/chess-engine/)\n"
        content += f"- [Technical Analysis Notebooks](/notebooks/)\n"
        content += f"- [Repository on GitHub](https://github.com/pssnyder/{repo_name})\n\n"
        
        content += "---\n\n"
        content += f"*This project overview was generated from repository analysis.*\n"
        
        return content
    
    def generate_all_content(self):
        """Generate all content types"""
        generated_files = []
        
        # Generate journal entries
        if 'journal_entries' in self.suggestions:
            print(f"Generating {len(self.suggestions['journal_entries'])} journal entries...")
            
            for suggestion in self.suggestions['journal_entries']:
                content = self.generate_journal_entry(suggestion)
                if content:
                    filename = self.sanitize_filename(suggestion['title'], suggestion['date'])
                    filepath = self.posts_dir / filename
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    generated_files.append(str(filepath))
                    print(f"  Generated: {filename}")
        
        # Generate notebooks as markdown files for Jekyll
        if 'notebooks' in self.suggestions:
            print(f"Generating {len(self.suggestions['notebooks'])} notebook markdown files...")
            
            for suggestion in self.suggestions['notebooks']:
                # Generate the actual .ipynb file
                notebook_content = self.generate_performance_notebook(suggestion)
                notebook_filename = self.sanitize_filename(suggestion['title']) + "nb"
                notebook_filename = notebook_filename.replace('.md', '.ipynb')
                notebook_filepath = self.notebooks_dir / notebook_filename
                
                with open(notebook_filepath, 'w', encoding='utf-8') as f:
                    f.write(notebook_content)
                
                # Generate markdown content for Jekyll
                markdown_content = self.generate_notebook_markdown(suggestion)
                markdown_filename = self.sanitize_filename(suggestion['title'])
                markdown_filepath = self.notebooks_dir / markdown_filename
                
                with open(markdown_filepath, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                
                generated_files.append(str(notebook_filepath))
                generated_files.append(str(markdown_filepath))
                print(f"  Generated: {notebook_filename} and {markdown_filename}")
            
            # Remove old invalid notebooks
            for old_file in self.notebooks_dir.glob("*.ipynb"):
                if old_file.name.startswith("2025-08-30-") and "performance-analysis" in old_file.name:
                    try:
                        old_file.unlink()
                        print(f"  Removed old invalid notebook: {old_file.name}")
                    except:
                        pass
        
        # Generate project overviews
        for repo_name in self.analysis_data.keys():
            print(f"Generating project overview for {repo_name}...")
            content = self.generate_project_overview(repo_name)
            filename = f"{repo_name}-overview.md"
            filepath = self.projects_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            generated_files.append(str(filepath))
            print(f"  Generated: {filename}")
        
        return generated_files

def main():
    generator = ContentGenerator()
    
    if not generator.analysis_data:
        print("No analysis data found. Run analyze_repos.py first.")
        return
    
    if not generator.suggestions:
        print("No content suggestions found. Run analyze_repos.py first.")
        return
    
    # Generate all content
    generated_files = generator.generate_all_content()
    
    print(f"\nContent generation complete!")
    print(f"Generated {len(generated_files)} files:")
    for file_path in generated_files:
        print(f"  - {file_path}")
    
    print("\nNext steps:")
    print("1. Review and edit generated content")
    print("2. Test Jekyll build: jekyll build")
    print("3. Preview site: jekyll serve")
    print("4. Commit and push changes")

if __name__ == "__main__":
    main()
