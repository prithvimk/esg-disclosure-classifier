import fitz
import pandas as pd
import sys
import os
import logging
from collections.abc import Iterable
from pathlib import Path

from docling.backend.docling_parse_v4_backend import DoclingParseV4DocumentBackend
from docling.datamodel.base_models import ConversionStatus, InputFormat
from docling.datamodel.document import ConversionResult
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

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
def export_documents(
    conv_results: Iterable[ConversionResult],
    output_dir: Path,
):

    success_count = 0
    failure_count = 0
    partial_success_count = 0

    for conv_res in conv_results:
        if conv_res.status == ConversionStatus.SUCCESS:
            success_count += 1
            doc_filename = conv_res.input.file.stem

            conv_res.document.save_as_markdown(
                output_dir / f"{doc_filename}.md"
            )


        elif conv_res.status == ConversionStatus.PARTIAL_SUCCESS:
            logger.info(
                f"Document {conv_res.input.file} was partially converted with the following errors:"
            )
            for item in conv_res.errors:
                logger.info(f"\t{item.error_message}")
            partial_success_count += 1
        else:
            logger.info(f"Document {conv_res.input.file} failed to convert.")
            failure_count += 1

    logger.info(
        f"Processed {success_count + partial_success_count + failure_count} docs, "
        f"of which {failure_count} failed "
        f"and {partial_success_count} were partially converted."
    )
    return success_count, partial_success_count, failure_count


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
            logger.info(f"text extracted from {row.filename}..")
        except Exception as e:
            logger.error(f"text extraction failed for {row.filename} with error: {e.text}")
        
        # attempt saving text file to /data/extracted_text/<company_name>/<year>/<filename>.txt
        try: 
            with open(TEXT_DIR / row.company_name.strip().replace('/', '') / str(row.year) / (row.filename + '.txt'), 'w', encoding='utf-8') as txt_file:
                txt_file.write(full_text)
            logger.info(f"text file saved for {row.filename}..")
        except Exception as e:
            logger.error(f"text file save failed for {row.filename} with error: {e.text}")