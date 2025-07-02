from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Community, Person
from app.schemas import Community as CommunitySchema, CommunityCreate, CommunityWithPeople, PersonWithCheckIns
from app.services.check_in_service import CheckInService

router = APIRouter(prefix="/communities", tags=["communities"])

@router.get("/", response_model=List[CommunitySchema])
def get_communities(db: Session = Depends(get_db)):
    """Get all communities/events."""
    communities = db.query(Community).all()
    return communities

@router.get("/{community_id}", response_model=CommunitySchema)
def get_community(community_id: int, db: Session = Depends(get_db)):
    """Get a specific community by ID."""
    community = db.query(Community).filter(Community.id == community_id).first()
    if not community:
        raise HTTPException(status_code=404, detail="Community not found")
    return community

@router.get("/{community_id}/people", response_model=List[PersonWithCheckIns])
def get_community_people(community_id: int, db: Session = Depends(get_db)):
    """Get all people registered for a community with their check-in status."""
    # Verify community exists
    community = db.query(Community).filter(Community.id == community_id).first()
    if not community:
        raise HTTPException(status_code=404, detail="Community not found")
    
    people = db.query(Person).filter(Person.community_id == community_id).all()
    
    # Add current check-in status to each person
    people_with_status = []
    for person in people:
        current_check_in = CheckInService.get_current_check_in(db, person.id)
        check_ins = CheckInService.get_person_check_ins(db, person.id)
        
        person_data = PersonWithCheckIns(
            id=person.id,
            first_name=person.first_name,
            last_name=person.last_name,
            email=person.email,
            company_name=person.company_name,
            title=person.title,
            community_id=person.community_id,
            created_at=person.created_at,
            full_name=person.full_name,
            check_ins=check_ins,
            current_check_in=current_check_in
        )
        people_with_status.append(person_data)
    
    return people_with_status

@router.post("/", response_model=CommunitySchema)
def create_community(community: CommunityCreate, db: Session = Depends(get_db)):
    """Create a new community/event."""
    db_community = Community(**community.model_dump())
    db.add(db_community)
    db.commit()
    db.refresh(db_community)
    return db_community