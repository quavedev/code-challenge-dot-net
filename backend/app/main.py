from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import communities, people, check_ins
from app.database import engine
from app.models import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quave Challenge API",
    description="Event Check-in System API",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(communities.router, prefix="/api")
app.include_router(people.router, prefix="/api")
app.include_router(check_ins.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Quave Challenge API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}