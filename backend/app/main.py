from fastapi import FastAPI

app = FastAPI(
    title="FamilySphere API",
    description="Open Source Genealogy Platform",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "name": "FamilySphere",
        "status": "running",
        "version": "0.1.0"
    }
