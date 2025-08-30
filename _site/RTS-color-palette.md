# RTS Technology & Solutions Color Palette & Typography

This document summarizes the color palette and text styles used in the RTS Technology & Solutions site. Use these guidelines to match your GitHub portfolio to the site's look and feel.

## Color Palette

| Name              | Usage                | Hex Code   | Example |
|-------------------|---------------------|------------|---------|
| brand-dark        | Background, header  | #0D0D0D    | ![#0D0D0D](https://via.placeholder.com/20/0D0D0D/FFFFFF?text=+) |
| brand-surface     | Card backgrounds    | #1A1A1A    | ![#1A1A1A](https://via.placeholder.com/20/1A1A1A/FFFFFF?text=+) |
| brand-border      | Card borders        | #2C2C2C    | ![#2C2C2C](https://via.placeholder.com/20/2C2C2C/FFFFFF?text=+) |
| text-primary      | Main text           | #E0E0E0    | ![#E0E0E0](https://via.placeholder.com/20/E0E0E0/000000?text=+) |
| text-secondary    | Subtle text         | #A0A0A0    | ![#A0A0A0](https://via.placeholder.com/20/A0A0A0/000000?text=+) |
| accent-primary    | Highlights, links   | #00FFFF    | ![#00FFFF](https://via.placeholder.com/20/00FFFF/000000?text=+) |
| accent-secondary  | Highlights, hover   | #FF00FF    | ![#FF00FF](https://via.placeholder.com/20/FF00FF/000000?text=+) |

## Typography

- **Primary Font:** Inter (sans-serif)
- **Mono Font:** Space Mono (monospace)

### Text Styles

| Class Name         | Font Family   | Color         | Usage Example                |
|--------------------|--------------|---------------|------------------------------|
| font-sans          | Inter        | text-primary  | Main body text               |
| font-mono          | Space Mono   | accent-primary| Headings, code, highlights   |
| text-text-primary  | Inter/Mono   | #E0E0E0       | Main text                    |
| text-text-secondary| Inter/Mono   | #A0A0A0       | Subtle/secondary text        |
| text-accent-primary| Space Mono   | #00FFFF       | Headings, links, highlights  |
| text-accent-secondary| Space Mono | #FF00FF       | Hover, accent, highlights    |

## UI Elements

- **Cards:**
  - Background: brand-surface
  - Border: brand-border
  - Title: accent-primary (hover: accent-secondary)
  - Description: text-secondary
  - Tags: accent-primary, accent-secondary, and other accent colors
- **Header/Footer:**
  - Background: brand-dark
  - Text: accent-primary, text-primary, text-secondary
  - Borders: accent-primary (with opacity)
- **Buttons/Links:**
  - Background: accent-primary (hover: accent-secondary)
  - Text: brand-dark or white

## Example Usage

```jsx
<h1 className="text-accent-primary font-mono text-4xl">RTS //_ Technology & Solutions</h1>
<p className="text-text-secondary font-sans">Empowering future innovators...</p>
<a className="bg-accent-primary text-brand-dark hover:bg-accent-secondary hover:text-white">Explore</a>
```

---

Feel free to use these colors and fonts to style your GitHub portfolio for a cohesive look!
