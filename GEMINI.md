# Project: Houlab School Fes 2026 Digital Newspaper

This project is a static digital newspaper for the "Houlab School Fes 2026" (放らぼ文化祭2026), created by the Newspaper & Photography Club (新聞写真部). It uses a classic newspaper aesthetic and is built with vanilla web technologies.

## Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript.
- **Styling**: 
    - `style.css`: Main layout using CSS Grid and multi-column layout.
    - `article_detail.css`: Specific styles for article pages.
    - **Fonts**: Google Fonts "Shippori Mincho" (serif).
- **Backend/Scripting**: 
    - Python (for utility scripts like PDF text extraction).

## Project Structure
- `index.html`: The main landing page mimicking a newspaper front page.
- `article-*.html`: Individual article pages (e.g., `article-daily-report-0215.html`).
- `article_template.html`: A boilerplate template for creating new articles.
- `script.js`: Simple utility script to update the date dynamically.
- `_extract_pdf.py`: A Python script to extract text from PDF drafts using `pdfminer.six`.
- `img_*.png/jpg`: Image assets used in the articles.
- `無題のドキュメント (*).pdf`: Drafts or source materials for articles.

## Development Workflow

### Adding a New Article
1. Copy `article_template.html` to a new file (e.g., `article-my-new-story.html`).
2. Update the title, metadata, and body content.
3. Add a link to the new article in the "新着ニュース" (New News) section of `index.html`.
4. Add the article image to the root directory and update the `<img>` tag in the HTML.

### Using the PDF Extractor
If you have a PDF draft and want to extract its text:
```bash
python _extract_pdf.py "filename.pdf"
```
*Note: Requires `pdfminer.six` (`pip install pdfminer.six`).*

## Coding Conventions
- **Naming**: Use kebab-case for HTML files and image assets (e.g., `article-name.html`).
- **Styling**: Maintain the "newspaper" aesthetic. Use `--accent-red` for highlights and `Shippori Mincho` for headings and body text.
- **Language**: The primary language of the content is Japanese.
