from fastapi import FastAPI
from api.upload import router as upload_router
from ingestion.loaders.pdf_loader import load_pdf
from api.search import router as search_router

app=FastAPI()

@app.get('/')
def home():
    return {"message":"Hello Homepage"}

#upload router
app.include_router(upload_router)
#search router
app.include_router(search_router)