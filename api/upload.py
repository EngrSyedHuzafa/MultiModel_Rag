from fastapi import UploadFile, File, APIRouter
import shutil
import os

# from ingestion.loaders.pdf_loader import load_pdf
# from ingestion.chunking.text_chunker import chunk_text

router=APIRouter()

UPLOAD_DIR="data/raw"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    #for checking if the file is uploaded successfully and to test the pdf loader
    # text = load_pdf(file_path)
    # print(text[:500])
    # chunks = chunk_text(text)

    # print(chunks[0])
    # print(len(chunks))
    return {
        "filename": file.filename,
        "message": "File uploaded successfully"
    }

    

