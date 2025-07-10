from typer import Typer, Argument, Option
from get_pubmed_papers.fetcher import fetch_papers
from get_pubmed_papers.exporter import export_to_csv

app = Typer()

@app.command()
def search(
    query: str = Argument(..., help="PubMed search query"),
    file: str = Option(None, "--file", "-f", help="Output CSV filename"),
    debug: bool = Option(False, "--debug", "-d", help="Enable debug logs")
):
    """
    Fetches papers from PubMed with optional debug and export functionality.
    """
    if debug:
        print(f"[DEBUG] Searching PubMed for: {query}")

    try:
        papers = fetch_papers(query, debug=debug)

        if not papers:
            print("⚠️  No papers found for the given query.")
            return

        if file:
            export_to_csv(papers, file)
        else:
            for paper in papers:
                print(paper)

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    app()
