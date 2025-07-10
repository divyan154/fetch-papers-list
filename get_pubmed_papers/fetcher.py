import requests
from typing import List, Dict
from xml.etree import ElementTree as ET
from get_pubmed_papers.parser import parse_authors_and_affiliations

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    search_url = f"{BASE_URL}/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": 10,
        "retmode": "json"
    }

    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()
    id_list = search_data["esearchresult"]["idlist"]

    if debug:
        print(f"[DEBUG] Found {len(id_list)} PubMed IDs: {id_list}")

    fetch_url = f"{BASE_URL}/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }

    fetch_response = requests.get(fetch_url, params=fetch_params)
    root = ET.fromstring(fetch_response.content)

    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pubdate = article.findtext(".//PubDate/Year") or "N/A"
        authors, companies, emails = parse_authors_and_affiliations(article)

        # Placeholder — you’ll update with parser later
        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pubdate,
            "Non-academic Author(s)": "; ".join(authors) if authors else "N/A",
            "Company Affiliation(s)": "; ".join(companies) if companies else "N/A",
            "Corresponding Author Email": "; ".join(emails) if emails else "N/A",
            
        })

    return results
# 40637021