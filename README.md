# ae2.nl

This repository contains the source for the static **ae2.nl** help site.

## Purpose

The site hosts documentation and support pages for **Acoustics Engineering** products. The content is authored as plain HTML and served as static files, instead of using a Markdown-based documentation generator.

## Structure

- `docs/` contains the public website pages and shared assets
- `docs/assets/` contains images, logos, and shared styling
- product sections such as `docs/echo/`, `docs/atlas/`, and `docs/dirac/` contain the individual help pages

## Local preview

To preview the site locally, run the PowerShell task or execute:

- `powershell -ExecutionPolicy Bypass -File ./serve-docs.ps1`

This starts a simple local web server and opens the site at:

- http://127.0.0.1:8000/

## License

This project is licensed under the MIT License. See `LICENSE` for details.
