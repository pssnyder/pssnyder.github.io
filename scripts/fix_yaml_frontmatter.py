#!/usr/bin/env python3
"""
Fix YAML front matter issues in generated Jekyll posts

This script fixes common issues in the generated posts:
- Escapes backslashes in titles and excerpts
- Fixes overly long titles
- Removes problematic characters

Usage:
    python scripts/fix_yaml_frontmatter.py
"""

import os
import re
import yaml
from pathlib import Path

def fix_yaml_frontmatter():
    """Fix YAML front matter issues in all post files"""
    posts_dir = Path("_posts")
    fixed_count = 0
    
    for post_file in posts_dir.glob("*.md"):
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split front matter and content
            if content.startswith('---\n'):
                parts = content.split('---\n', 2)
                if len(parts) >= 3:
                    frontmatter_text = parts[1]
                    post_content = parts[2]
                    
                    # Try to parse the YAML
                    try:
                        frontmatter = yaml.safe_load(frontmatter_text)
                        
                        # Fix title issues
                        if 'title' in frontmatter:
                            title = frontmatter['title']
                            # Remove Windows path separators and problematic chars
                            title = title.replace('\\', '/')
                            title = re.sub(r'[^\w\s\-\.\:\!\?\,\(\)\[\]\/\|\#\&\@\%\+\=\~]', '', title)
                            # Limit title length
                            if len(title) > 120:
                                title = title[:120].rstrip()
                            frontmatter['title'] = title
                        
                        # Fix excerpt issues
                        if 'excerpt' in frontmatter:
                            excerpt = frontmatter['excerpt']
                            excerpt = excerpt.replace('\\', '/')
                            excerpt = re.sub(r'[^\w\s\-\.\:\!\?\,\(\)\[\]\/\|\#\&\@\%\+\=\~]', '', excerpt)
                            if len(excerpt) > 200:
                                excerpt = excerpt[:200].rstrip()
                            frontmatter['excerpt'] = excerpt
                        
                        # Regenerate the YAML
                        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
                        new_content = f"---\n{new_frontmatter}---\n{post_content}"
                        
                        # Write back to file
                        with open(post_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        fixed_count += 1
                        print(f"Fixed: {post_file.name}")
                        
                    except yaml.YAMLError as e:
                        print(f"YAML error in {post_file.name}: {e}")
                        continue
                        
        except Exception as e:
            print(f"Error processing {post_file.name}: {e}")
            continue
    
    print(f"\nFixed {fixed_count} files")

def remove_duplicate_posts():
    """Remove duplicate posts that may have been generated"""
    posts_dir = Path("_posts")
    seen_dates_titles = set()
    duplicates = []
    
    for post_file in posts_dir.glob("*.md"):
        # Extract date and basic title from filename
        filename = post_file.name
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
        if date_match:
            date = date_match.group(1)
            # Get a simplified title for comparison
            title_part = filename[11:].replace('.md', '')  # Remove date and extension
            title_key = re.sub(r'[^a-z0-9]', '', title_part.lower())[:50]  # First 50 chars, normalized
            
            key = (date, title_key)
            if key in seen_dates_titles:
                duplicates.append(post_file)
                print(f"Duplicate found: {filename}")
            else:
                seen_dates_titles.add(key)
    
    # Remove duplicates
    for dup_file in duplicates:
        try:
            dup_file.unlink()
            print(f"Removed duplicate: {dup_file.name}")
        except Exception as e:
            print(f"Error removing {dup_file.name}: {e}")
    
    print(f"Removed {len(duplicates)} duplicate files")

if __name__ == "__main__":
    print("Fixing YAML front matter issues...")
    fix_yaml_frontmatter()
    
    print("\nRemoving duplicate posts...")
    remove_duplicate_posts()
    
    print("\nDone! Try running 'jekyll build' again.")
