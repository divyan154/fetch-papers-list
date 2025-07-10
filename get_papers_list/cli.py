from typer import Typer, Option, Argument
from get_papers_list.fetcher import fetch_papers
from get_papers_list.exporter import export_to_csv

app = Typer()

@app.command()
def main(
    query: str = Argument(..., help="Search query for PubMed"),
    file: str = Option(None, "--file", "-f", help="File name to save CSV"),
    debug: bool = Option(False, "--debug", "-d", help="Enable debug logging")
):
    """
    Fetches research papers from PubMed for a given query.
    Filters for pharmaceutical/biotech affiliations and outputs to CSV or console.
    """
    if debug:
        print(f"[DEBUG] Searching PubMed for: {query}")

    try:
        papers = fetch_papers(query, debug=debug)
        if file:
            export_to_csv(papers, file)
        else:
            for paper in papers:
                print(paper)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    app()
