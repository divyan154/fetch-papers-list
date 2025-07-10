import pandas as pd
from typing import List, Dict

def export_to_csv(data: List[Dict], filename: str):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(data)} papers to {filename}")
