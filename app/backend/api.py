from fastapi import FastAPI, Query
from fastapi import UploadFile, File

# import backend services
# from graph_service import run_cypher
from vector_service import create_embeddings
from ingestion_service import ingest_pdf
from paths import UPLOADS

app = FastAPI(title="ESG GraphRAG API")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:

        file_path = UPLOADS / file.filename

        with open(file_path, 'wb') as f:
            contents = await file.read()
            f.write(contents) 

        ingest_pdf(file_path)

        return {"filename": file.filename, "message": f"File uploaded successfully"}

    except Exception as e:
        return {"error": str(e)}

    