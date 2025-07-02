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

# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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

# TODO: Implement the following endpoints:

# Communities (Events) endpoints
# GET /api/communities/ - List all events
# POST /api/communities/ - Create new event  
# GET /api/communities/{id} - Get specific event
# GET /api/communities/{id}/people - Get people registered for event

# People endpoints
# GET /api/people/ - List all people
# POST /api/people/ - Register new person
# GET /api/people/{id} - Get person details
# PUT /api/people/{id} - Update person information

# Check-ins endpoints  
# POST /api/check-ins/{person_id}/check-in - Check in person
# PUT /api/check-ins/{person_id}/check-out - Check out person
# GET /api/check-ins/events/{community_id}/summary - Get event summary