#!/bin/bash

# Notebook to Jekyll Conversion Script
# This script provides a simple interface to convert notebooks

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "🔄 Converting Jupyter Notebooks to Jekyll Posts"
echo "================================================"

# Check if Python and required packages are available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if nbconvert is installed
if ! python3 -c "import nbconvert" 2>/dev/null; then
    echo "📦 Installing required packages..."
    pip install nbconvert jupyter
fi

# Run the conversion
cd "$PROJECT_ROOT"

if [ "$1" ]; then
    echo "🔄 Converting specific notebook: $1"
    python3 scripts/convert_notebooks.py "$1"
else
    echo "🔄 Converting all notebooks in _notebooks directory..."
    python3 scripts/convert_notebooks.py
fi

echo ""
echo "✅ Conversion complete!"
echo ""
echo "📝 Next steps:"
echo "1. Review the generated markdown files in _posts/"
echo "2. Run 'bundle exec jekyll serve' to preview your site"
echo "3. Commit and push to deploy to GitHub Pages"
