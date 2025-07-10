import re
from typing import List, Tuple
from xml.etree import ElementTree as ET

# Company/industry-related keywords
COMPANY_KEYWORDS = [
    "pharma", "biotech", "inc", "llc", "gmbh", "ltd", "genentech", "pfizer",
    "novartis", "astrazeneca", "sanofi", "bayer", "merck", "roche",
    "therapeutics", "laboratories", "regeneron", "moderna", "abbvie",
    "group", "corp", "company"
]

# Location and address-related keywords (to be excluded from cleaned affiliations)
LOCATION_KEYWORDS = [
    "usa", "united states", "germany", "india", "china", "france", "canada",
    "australia", "japan", "singapore", "tx", "ca", "uk", "austin", "boston",
    "new york", "paris", "delhi", "bangalore", "seoul", "shanghai", "mumbai",
    "houston", "berlin", "tokyo", "london", "sydney", "melbourne",
    "vancouver", "montreal"
]

def is_company_affiliation(affiliation: str) -> bool:
    """Returns True if the affiliation seems to be a company, not a university/institution."""
    academic_keywords = [
        "university", "college", "school", "hospital", "institute", "dept", "department",
        "faculty", "center", "centre", "clinic", "medical"
    ]
    return not any(keyword in affiliation.lower() for keyword in academic_keywords)

def extract_emails(text: str) -> List[str]:
    """Extracts email addresses from a given text string."""
    if not text:
        return []
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

def is_non_academic(affiliation: str) -> bool:
    """Returns True if affiliation string contains industry-related keywords."""
    if not affiliation:
        return False
    lower_aff = affiliation.lower()
    return any(keyword in lower_aff for keyword in COMPANY_KEYWORDS)

def clean_affiliation(text: str) -> str:
    """Cleans affiliation string by removing location and address parts."""
    if not text:
        return ""
    segments = re.split(r"[;,]", text)
    for seg in segments:
        seg = seg.strip()
        if not any(loc in seg.lower() for loc in LOCATION_KEYWORDS):
            return seg
    return segments[0].strip() if segments else text.strip()

def parse_authors_and_affiliations(article: ET.Element) -> Tuple[List[str], List[str], List[str]]:
    """
    Extracts non-academic author names, company affiliations, and emails.
    Returns a tuple of (author_names, company_names, email_list)
    """
    authors = []
    companies = set()
    emails = set()

    for author in article.findall(".//Author"):
        last = author.findtext("LastName") or ""
        fore = author.findtext("ForeName") or ""
        fullname = f"{fore} {last}".strip()

        aff_nodes = author.findall("AffiliationInfo/Affiliation")
        for aff_node in aff_nodes:
            aff_text = aff_node.text or ""

            if is_non_academic(aff_text) and is_company_affiliation(aff_text):
                authors.append(fullname)
                companies.add(clean_affiliation(aff_text))

            for email in extract_emails(aff_text):
                emails.add(email)

    return authors, list(companies), list(emails)
