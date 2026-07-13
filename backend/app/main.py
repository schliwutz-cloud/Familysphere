from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.person import Person

app = FastAPI(
   
    title="FamilySphere API",
    description="Open Source Genealogy Platform",
    version="0.1.0"
)
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {
        "name": "FamilySphere",
        "status": "running",
        "version": "0.1.0"
    }
