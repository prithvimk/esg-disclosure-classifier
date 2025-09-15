from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.chunking import HybridChunker

def convert_document():
    '''
    Convert documents using Docling
    '''

    converter = DocumentConverter()
    chunker = HybridChunker()

    doc = converter.convert(r'..\..\config\esg_reveal_prompts.pdf').document

    texts = [chunk.text for chunk in chunker.chunk(doc)]