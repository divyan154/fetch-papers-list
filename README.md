# 🧬 get-pubmed-papers

A Python CLI tool to fetch PubMed papers and extract company-affiliated metadata. Ideal for research, academic mining, and market analysis.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-^3.9-blue)
![Poetry](https://img.shields.io/badge/Built%20with-Poetry-3985FF)

---

## 📦 Project Overview

This tool allows users to:
- Search PubMed for papers by keyword
- Extract author affiliations and metadata
- Filter for company-affiliated papers
- Export data to **CSV** or **JSON**

---

## 🚀 Features

- ✅ CLI powered by [Typer](https://typer.tiangolo.com/)
- ✅ Fetch up to thousands of papers from PubMed
- ✅ Extract organization names from author affiliations
- ✅ Export results in tabular format
- ✅ Built with Python 3.9+ and Poetry

---

## 🛠️ Installation

### Option 1: Install via Poetry (Recommended)

```bash
git clone https://github.com/divyan154/fetch-papers-list.git
cd fetch-papers-list
poetry install
poetry run get-pubmed-papers --help

### Option 2: Install globally (after building)
```bash
poetry build
pip install dist/get_pubmed_papers-0.1.1-py3-none-any.whl
get-pubmed-papers --help

🧪 Usage
Basic Command
poetry run get-pubmed-papers "cancer therapy" --file papers.csv --debug



📂 Project Structure
csharp
Copy
Edit
get-pubmed-papers/
├── get_pubmed_papers/
│   ├── cli.py       # CLI interface (Typer-based)
│   ├── fetcher.py   # PubMed data fetching logic
│   ├── exporter.py  # CSV export utilities
│   ├── parser.py    # Metadata parsing (e.g., affiliation filter)
│   └── __init__.py
├── .env             # Optional: API keys or runtime settings
├── output.csv       # Sample output
├── results.csv      # Sample filtered results
├── pyproject.toml   # Poetry project config
├── poetry.lock
└── README.md

🧠 Example Output
Sample CSV:

Title	Authors	Affiliation	Date	PMID
AI in Cancer	Smith J., Doe A.	Pfizer Inc., USA	2023-06-01	12345678