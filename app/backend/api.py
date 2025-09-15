from fastapi import FastAPI, Query
from fastapi import UploadFile, File

# import backend services
from backend.graph_service import run_cypher
from backend.vector_service import semantic_search
from backend.ingestion_service import convert_document

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
        # Process the file here
        # For demonstration, we'll save it to a temporary location
        # with open(f"temp_{file.filename}", "wb") as buffer:
        #     shutil.copyfileobj(file.file, buffer)
        
        # You can perform various operations on the file, e.g.,
        # - Read its content: file_content = await file.read()
        # - Analyze images, process text, etc.
        
        return {"filename": file.filename, "message": "File processed successfully!"}
    except Exception as e:
        return {"error": str(e)}
