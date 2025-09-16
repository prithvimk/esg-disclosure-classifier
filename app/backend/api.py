from fastapi import FastAPI, Query
from fastapi import UploadFile, File

# import backend services
# from graph_service import run_cypher
# from vector_service import semantic_search
from ingestion_service import convert_document

app = FastAPI(title="ESG GraphRAG API")

@app.get("/graph/query")
def graph_query(cypher: str):
    return run_cypher(cypher)

@app.get("/search")
def search(query: str):
    return semantic_search(query)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
              
        return {"filename": file.filename, "message": "File processed successfully!"}
    except Exception as e:
        return {"error": str(e)}
