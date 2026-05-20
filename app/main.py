from fastapi import FastAPI
from api.upload import router as upload_router
from ingestion.loaders.pdf_loader import load_pdf

app=FastAPI()

app.get('/')
def home():
    return {"message":"Hello Homepage"}

app.include_router(upload_router)
