import fitz
import pandas as pd
import sys
import os
import logging

sys.path.insert(1, "./")

from config.paths import METADATA_FILE, RAW_PDF_DIR, TEXT_DIR, EXTRACTION_LOG

logger = logging.getLogger(__name__)
formatting = '%(asctime)s %(name)s %(levelname)s %(message)s'

logging.basicConfig(handlers=[logging.FileHandler(EXTRACTION_LOG), 
                              logging.StreamHandler(sys.stdout)],
                    encoding='utf-8', level=logging.DEBUG, format=formatting)

# old function using PymuPDF
def extract_all_text(pdf_path: os.PathLike, skip_pages=0):
    """Extracts all text from a PDF document."""
    with fitz.open(pdf_path) as doc:
        full_text = ""
        for page_num in range(skip_pages, doc.page_count):
            page = doc.load_page(page_num)
            full_text += page.get_text("text") 
    return full_text

# new method using Docling



if __name__ == "__main__":

    # read metadata sheet   
    metadata = pd.read_excel(METADATA_FILE)

    # make dirs for storing extracted text
    metadata.loc[:, ['company_name', 'filename', 'year']].apply(lambda row: 
                                                                os.makedirs(TEXT_DIR / row.company_name.strip().replace('/', '') / str(row.year), 
                                                                            exist_ok=True), 
                                                                axis=1)
    
    # iterate over metadata sheet
    for row in metadata.loc[:, ['company_name', 'filename', 'year']].itertuples():

        # try extracting text from pdf report using PyMuPDF
        try:
            full_text = extract_all_text(RAW_PDF_DIR / (row.filename + '.pdf'))
            logging.info(f"text extracted from {row.filename}..")
        except Exception as e:
            logging.error(f"text extraction failed for {row.filename} with error: {e.text}")
        
        # attempt saving text file to /data/extracted_text/<company_name>/<year>/<filename>.txt
        try: 
            with open(TEXT_DIR / row.company_name.strip().replace('/', '') / str(row.year) / (row.filename + '.txt'), 'w', encoding='utf-8') as txt_file:
                txt_file.write(full_text)
            logging.info(f"text file saved for {row.filename}..")
        except Exception as e:
            logging.error(f"text file save failed for {row.filename} with error: {e.text}")