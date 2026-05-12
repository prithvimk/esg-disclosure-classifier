import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def extract_esrs_paragraphs(url: str) -> pd.DataFrame:
    """
    Extract paragraphs (including appendix) and their text from an ESRS XBRL HTML document.
    Handles numbered and appendix-style paragraphs (e.g. 37a, AG12b, AR37(a)).
    """

    try:
        response = requests.get(url, timeout=25)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return pd.DataFrame(columns=["paragraph_name", "text"])

    try:
        soup = BeautifulSoup(response.text, "html.parser")

        # Include broader range of elements for appendix text
        text_blocks = soup.find_all(['p', 'div', 'span', 'li', 'td', 'section'])
        data = []
        last_para = None

        # Regex pattern to detect paragraph IDs:
        #  - 37, 37(a), 37b
        #  - AR 12(a), AG12b, etc.
        para_pattern = re.compile(r'^(?:(AR|AG)\s*)?(\d+\(?[a-zA-Z]?\)?)\s*(.*)')

        for block in text_blocks:
            text = " ".join(block.get_text(strip=True).split())
            if not text:
                continue

            match = para_pattern.match(text)
            if match:
                prefix = match.group(1) or ""
                num = match.group(2).replace("(", "").replace(")", "")
                para_text = match.group(3).strip()

                para_id = f"{prefix}{num}".strip()
                last_para = para_id
                data.append((para_id, para_text))
            else:
                # If no match but continuation of previous paragraph
                if last_para and data:
                    data[-1] = (data[-1][0], data[-1][1] + " " + text)

        df = pd.DataFrame(data, columns=["paragraph_name", "text"])

        # Drop duplicates and clean up
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df

    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return pd.DataFrame(columns=["paragraph_name", "text"])


if __name__ == "__main__":
    url = "https://xbrl.efrag.org/e-esrs/esrs-set1-2023.html#d1e24283-3-1"
    df = extract_esrs_paragraphs(url)
    print(df.head(20))
    print(f"\nExtracted {len(df)} paragraphs (including appendix).")
