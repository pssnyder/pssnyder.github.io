#!/usr/bin/env python3
"""
Notebook to Jekyll Post Converter

This script converts Jupyter notebooks from the _notebooks directory
to Jekyll-compatible markdown files in the _posts directory.

Usage:
    python scripts/convert_notebooks.py [notebook_file]
    
If no notebook_file is specified, all notebooks in _notebooks will be converted.
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
import nbformat
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import Preprocessor
import re

class JekyllPreprocessor(Preprocessor):
    """Custom preprocessor to enhance notebooks for Jekyll"""
    
    def preprocess_cell(self, cell, resources, index):
        """Process each cell for Jekyll compatibility"""
        if cell.cell_type == 'markdown':
            # Fix image paths for Jekyll
            cell.source = re.sub(
                r'!\[(.*?)\]\(((?!http).*?)\)',
                r'![\1]({{ "/assets/images/\2" | relative_url }})',
                cell.source
            )
            
            # Fix internal links
            cell.source = re.sub(
                r'\[([^\]]+)\]\((?!http)([^)]+)\.ipynb\)',
                r'[\1]({{ "/notebooks/\2/" | relative_url }})',
                cell.source
            )
        
        return cell, resources

def extract_notebook_metadata(notebook_path):
    """Extract metadata from notebook for Jekyll front matter"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Get metadata from notebook
    metadata = nb.metadata.get('jekyll', {})
    
    # Try to extract title from first markdown cell or filename
    title = metadata.get('title')
    if not title:
        for cell in nb.cells:
            if cell.cell_type == 'markdown' and cell.source.strip():
                # Look for h1 header
                lines = cell.source.split('\n')
                for line in lines:
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
                if title:
                    break
    
    if not title:
        title = Path(notebook_path).stem.replace('_', ' ').replace('-', ' ').title()
    
    # Extract description from notebook metadata or first text after title
    description = metadata.get('description', '')
    if not description:
        found_title = False
        for cell in nb.cells:
            if cell.cell_type == 'markdown' and cell.source.strip():
                lines = cell.source.split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith('# ') and not found_title:
                        found_title = True
                        continue
                    elif found_title and line and not line.startswith('#'):
                        description = line[:200] + ('...' if len(line) > 200 else '')
                        break
                if description:
                    break
    
    # Get other metadata
    date = metadata.get('date')
    if not date:
        # Use file modification time or current time
        try:
            date = datetime.fromtimestamp(os.path.getmtime(notebook_path)).strftime('%Y-%m-%d')
        except:
            date = datetime.now().strftime('%Y-%m-%d')
    
    # Extract tags and categories
    tags = metadata.get('tags', [])
    categories = metadata.get('categories', ['notebook'])
    technologies = metadata.get('technologies', [])
    
    # Try to infer technologies from notebook content
    if not technologies:
        notebook_text = str(nb).lower()
        tech_patterns = {
            'python': ['import ', 'python'],
            'pandas': ['import pandas', 'pd.'],
            'numpy': ['import numpy', 'np.'],
            'matplotlib': ['import matplotlib', 'plt.'],
            'seaborn': ['import seaborn'],
            'sklearn': ['sklearn', 'scikit-learn'],
            'tensorflow': ['tensorflow', 'import tf'],
            'pytorch': ['torch', 'pytorch'],
            'jupyter': ['jupyter', 'notebook'],
        }
        
        for tech, patterns in tech_patterns.items():
            if any(pattern in notebook_text for pattern in patterns):
                technologies.append(tech)
    
    return {
        'title': title,
        'description': description,
        'date': date,
        'tags': tags,
        'categories': categories,
        'technologies': technologies,
        'notebook_type': metadata.get('notebook_type', 'Analysis'),
        'github_repo': metadata.get('github_repo', ''),
        'notebook_file': metadata.get('notebook_file', ''),
    }

def create_jekyll_front_matter(metadata):
    """Create Jekyll front matter from metadata"""
    front_matter = ['---']
    front_matter.append('layout: notebook')
    front_matter.append(f'title: "{metadata["title"]}"')
    front_matter.append(f'date: {metadata["date"]}')
    
    if metadata['description']:
        front_matter.append(f'description: "{metadata["description"]}"')
    
    if metadata['categories']:
        front_matter.append(f'categories: {metadata["categories"]}')
    
    if metadata['tags']:
        front_matter.append(f'tags: {metadata["tags"]}')
    
    if metadata['technologies']:
        front_matter.append(f'technologies: {metadata["technologies"]}')
    
    if metadata['notebook_type']:
        front_matter.append(f'notebook_type: "{metadata["notebook_type"]}"')
    
    if metadata['github_repo']:
        front_matter.append(f'github_repo: "{metadata["github_repo"]}"')
    
    if metadata['notebook_file']:
        front_matter.append(f'notebook_file: "{metadata["notebook_file"]}"')
    
    front_matter.append('author: "Pat Snyder"')
    front_matter.append('---')
    front_matter.append('')
    
    return '\n'.join(front_matter)

def convert_notebook_to_post(notebook_path, output_dir):
    """Convert a single notebook to a Jekyll post"""
    print(f"Converting {notebook_path}...")
    
    # Extract metadata
    metadata = extract_notebook_metadata(notebook_path)
    
    # Create markdown exporter with custom preprocessor
    exporter = MarkdownExporter()
    exporter.register_preprocessor(JekyllPreprocessor(), enabled=True)
    
    # Convert notebook
    try:
        (body, resources) = exporter.from_filename(notebook_path)
    except Exception as e:
        print(f"Error converting {notebook_path}: {e}")
        return False
    
    # Create output filename
    notebook_name = Path(notebook_path).stem
    output_filename = f"{metadata['date']}-{notebook_name}.md"
    output_path = Path(output_dir) / output_filename
    
    # Create Jekyll front matter
    front_matter = create_jekyll_front_matter(metadata)
    
    # Combine front matter and body
    full_content = front_matter + body
    
    # Write output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Created {output_path}")
        return True
    except Exception as e:
        print(f"Error writing {output_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert Jupyter notebooks to Jekyll posts')
    parser.add_argument('notebook', nargs='?', help='Specific notebook to convert')
    parser.add_argument('--input-dir', default='_notebooks', help='Input directory (default: _notebooks)')
    parser.add_argument('--output-dir', default='_posts', help='Output directory (default: _posts)')
    
    args = parser.parse_args()
    
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    
    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)
    
    if args.notebook:
        # Convert specific notebook
        notebook_path = Path(args.notebook)
        if not notebook_path.exists():
            notebook_path = input_dir / args.notebook
            if not notebook_path.exists():
                print(f"Notebook not found: {args.notebook}")
                return 1
        
        success = convert_notebook_to_post(notebook_path, output_dir)
        return 0 if success else 1
    else:
        # Convert all notebooks in input directory
        if not input_dir.exists():
            print(f"Input directory does not exist: {input_dir}")
            return 1
        
        notebooks = list(input_dir.glob('*.ipynb'))
        if not notebooks:
            print(f"No notebooks found in {input_dir}")
            return 1
        
        success_count = 0
        for notebook_path in notebooks:
            if convert_notebook_to_post(notebook_path, output_dir):
                success_count += 1
        
        print(f"\nConverted {success_count}/{len(notebooks)} notebooks successfully")
        return 0 if success_count == len(notebooks) else 1

if __name__ == '__main__':
    sys.exit(main())
