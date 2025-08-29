# Technical Portfolio & Journal

A Jekyll-based portfolio website that transforms project documentation into a living journal, featuring automated Jupyter notebook conversion and comprehensive project showcases.

## 🚀 Quick Start

### Prerequisites

- Ruby 3.0+ 
- Git
- Python 3.8+ (for notebook conversion)

### Local Development

1. **Clone and setup**:
   ```bash
   git clone https://github.com/pssnyder/pssnyder.github.io.git
   cd pssnyder.github.io
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   pip install nbconvert jupyter
   ```

3. **Start local server**:
   ```bash
   bundle exec jekyll serve
   ```

4. **View site**: Navigate to `http://localhost:4000`

## 📁 Project Structure

```
├── _config.yml           # Jekyll configuration
├── _layouts/              # Page templates
│   ├── default.html      # Base layout
│   ├── post.html         # Journal entries
│   ├── notebook.html     # Converted notebooks
│   └── project.html      # Project showcases
├── _includes/             # Reusable components
├── _posts/                # Journal entries (auto-generated from notebooks)
├── _notebooks/            # Original Jupyter notebooks
├── _projects/             # Project documentation
├── scripts/               # Automation scripts
│   ├── convert_notebooks.py  # Notebook → Markdown converter
│   └── convert.sh        # Bash wrapper for conversion
├── assets/css/            # Styling
└── index.html             # Homepage
```

## 📓 Content Creation Workflow

### Adding Journal Entries

1. **Write directly**: Create markdown files in `_posts/` with proper front matter
2. **Convert from notebooks**: Place `.ipynb` files in `_notebooks/` and run conversion

### Converting Notebooks

**Convert all notebooks**:
```bash
python scripts/convert_notebooks.py
```

**Convert specific notebook**:
```bash
python scripts/convert_notebooks.py my_analysis.ipynb
```

**Using bash wrapper**:
```bash
bash scripts/convert.sh
```

### Adding Projects

Create markdown files in `_projects/` with front matter:

```yaml
---
layout: project
title: "Project Name"
description: "Brief project description"
start_date: 2024-01-01
status: "Active"  # Active, Completed, Planning, Archived
featured: true
technologies: ["Python", "Machine Learning"]
github_repo: "https://github.com/username/repo"
---
```

## 🎨 Customization

### Site Configuration

Edit `_config.yml` to customize:
- Site title and description
- Author information
- Social links
- Collection settings

### Styling

The site uses a custom CSS framework in `assets/css/style.scss` with:
- CSS custom properties for easy theming
- Responsive grid layouts
- Professional typography
- Syntax highlighting
- Mobile-optimized design

### Notebook Metadata

Add Jekyll metadata to notebooks using cell metadata:

```json
{
  "jekyll": {
    "title": "Analysis Title",
    "description": "Brief description",
    "tags": ["analysis", "python"],
    "technologies": ["pandas", "matplotlib"]
  }
}
```

## 🔧 Advanced Features

### Automatic Notebook Conversion

The conversion script:
- Extracts metadata from notebooks
- Generates Jekyll front matter
- Handles image paths and internal links
- Infers technologies from code content
- Creates SEO-friendly URLs

### Content Collections

Three main content types:
- **Posts**: Journal entries and blog-style content
- **Notebooks**: Converted Jupyter notebook analyses  
- **Projects**: Comprehensive project documentation

### Navigation & Discovery

- **Responsive navigation** with mobile hamburger menu
- **Archive pages** for each content type
- **Tag and category** organization
- **Related content** suggestions
- **Search functionality** (via browser)

## 📱 Responsive Design

The site is optimized for:
- **Desktop**: Full-width layouts with sidebar navigation
- **Tablet**: Responsive grid layouts
- **Mobile**: Stacked layouts with collapsible navigation
- **Print**: Clean print styles for documentation

## 🚀 Deployment

### GitHub Pages (Recommended)

1. **Push to GitHub**: Ensure repository is named `username.github.io`
2. **Enable GitHub Pages**: Settings → Pages → Deploy from main branch
3. **Automatic deployment**: Site rebuilds on every push

### Custom Domain

1. Add `CNAME` file with your domain
2. Configure DNS with your domain provider
3. Enable HTTPS in GitHub Pages settings

## 🔍 SEO & Performance

### Built-in Optimizations

- Semantic HTML structure
- Open Graph meta tags
- Twitter Card support
- Sitemap generation
- RSS feed
- Optimized image handling

### Performance Features

- Minimal JavaScript dependencies
- Optimized CSS with custom properties
- Lazy loading for images
- Compressed assets
- Fast Jekyll build times

## 🛠️ Development Tools

### Useful Commands

```bash
# Development server with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Convert specific notebook
python scripts/convert_notebooks.py notebook.ipynb

# Check for broken links (requires html-proofer gem)
bundle exec htmlproofer ./_site
```

### VS Code Integration

Recommended extensions:
- Jekyll snippets
- Liquid syntax highlighting
- Markdown preview
- YAML support

## 📋 Content Guidelines

### Writing Style

- **Technical accuracy** with accessible explanations
- **Narrative context** explaining the "why" behind decisions
- **Code examples** with proper syntax highlighting
- **Visual elements** (diagrams, charts, screenshots)

### Front Matter Standards

Always include:
- `layout`: Appropriate layout type
- `title`: Descriptive, SEO-friendly title
- `date`: Publication date (YYYY-MM-DD format)
- `description`: Brief summary for search and social sharing

### File Naming

- **Posts**: `YYYY-MM-DD-title-slug.md`
- **Projects**: `project-name.md`
- **Notebooks**: `descriptive-name.ipynb`

## 🤝 Contributing

This is a personal portfolio, but suggestions and improvements are welcome:

1. **Issues**: Report bugs or suggest features
2. **Pull Requests**: Improvements to scripts or documentation
3. **Discussions**: Share ideas for content organization

## 📄 License

Content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Code is licensed under [MIT License](LICENSE).

## 🙋‍♂️ Support

For questions about the technical implementation or suggestions for improvements:

- **GitHub Issues**: Technical problems or feature requests
- **Discussions**: General questions about the approach
- **Main Website**: [rapidtechconsultants.com](https://rapidtechconsultants.com)

---

*This portfolio represents an ongoing experiment in technical documentation and knowledge sharing. The goal is to bridge the gap between strategic thinking and detailed implementation through comprehensive, accessible documentation.*
