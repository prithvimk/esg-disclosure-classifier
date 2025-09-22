import ollama
from pymilvus import MilvusClient, Collection, connections, DataType, FieldSchema, CollectionSchema
import os

MILVUS_HOST = os.getenv('MILVUS_HOST', "localhost")
MILVUS_PORT = os.getenv('MILVUS_PORT', '19530')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'report_chunks')
EMBED_DIM = os.getenv('COLLECTION_NAME', 1024)   


class MilvusManager:
    _instance = None
    _collection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MilvusManager, cls).__new__(cls)
            cls._instance._connect()
            cls._instance._init_collection()
        return cls._instance

    def _connect(self):
        '''Establish a single connection to Milvus.'''
        connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
        print(connections.list_connections())

    def _init_collection(self):
        '''Initialize or load collection schema once.'''
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=EMBED_DIM),
            FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=2000)
        ]
        schema = CollectionSchema(fields, description="Report text chunks with embeddings")

        try:
            self._collection = Collection(COLLECTION_NAME)
        except Exception:
            self._collection = Collection(name=COLLECTION_NAME, schema=schema)

        # Create index if not already present
        if not self._collection.has_index():
            self._collection.create_index(
                field_name="embedding",
                index_params={"metric_type": "COSINE", "index_type": "IVF_FLAT", "params": {"nlist": 128}}
            )

    def get_collection(self) -> Collection:
        '''Return the active collection object.'''
        return self._collection
    

def create_embeddings(text_chunk: str):
    '''
    Create embeddings using Ollama APIs
    '''

    return ollama.embed(
        model='mxbai-embed-large',
        input=text_chunk
    )['embeddings'][0]



