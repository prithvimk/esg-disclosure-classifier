from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.chunking import HybridChunker

from pathlib import Path
from vector_service import create_embeddings, MilvusManager


def convert_document(file_path: Path):
    '''
    Convert documents using Docling and return chunked texts
    '''

    converter = DocumentConverter()
    chunker = HybridChunker()

    print("convert doc is running")

    try:
        doc = converter.convert(file_path).document
        chunked_texts = [chunk.text for chunk in chunker.chunk(doc)]
        return chunked_texts
    except Exception as e:
        return e.text
    
def ingest_pdf(file_path: Path):
    '''
    Performs the following steps:
    1. Converts PDF to DoclingDocument and chunks text
    2. Creates embeddings using Ollama
    3. Stores embeddings in MilvusDB
    '''

    chunked_texts = convert_document(file_path)

    embeddings = [create_embeddings(chunk) for chunk in chunked_texts]

    milvus = MilvusManager()
    collection = milvus.get_collection()

    data = [embeddings, chunked_texts]  
    collection.insert(data)
    collection.flush()