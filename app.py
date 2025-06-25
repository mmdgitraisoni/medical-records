from fastapi import FastAPI
from database.db import Base, engine
from api.routes import router as api_router

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Medical Record System",
    description="A comprehensive medical record system."
)

app.include_router(api_router)
