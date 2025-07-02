from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Person, Community
from app.schemas import Person as PersonSchema, PersonCreate, PersonUpdate, PersonWithCheckIns
from app.services.check_in_service import CheckInService

router = APIRouter(prefix="/people", tags=["people"])

@router.get("/", response_model=List[PersonSchema])
def get_people(db: Session = Depends(get_db)):
    """Get all people."""
    people = db.query(Person).all()
    return people

@router.get("/{person_id}", response_model=PersonWithCheckIns)
def get_person(person_id: int, db: Session = Depends(get_db)):
    """Get a specific person with their check-in history."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    current_check_in = CheckInService.get_current_check_in(db, person.id)
    check_ins = CheckInService.get_person_check_ins(db, person.id)
    
    return PersonWithCheckIns(
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

@router.post("/", response_model=PersonSchema)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    """Create a new person."""
    # Verify community exists
    community = db.query(Community).filter(Community.id == person.community_id).first()
    if not community:
        raise HTTPException(status_code=400, detail="Community not found")
    
    # Check if email already exists
    existing_person = db.query(Person).filter(Person.email == person.email).first()
    if existing_person:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_person = Person(**person.model_dump())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

@router.put("/{person_id}", response_model=PersonSchema)
def update_person(person_id: int, person_update: PersonUpdate, db: Session = Depends(get_db)):
    """Update a person's information."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    # Update only provided fields
    update_data = person_update.model_dump(exclude_unset=True)
    
    # Check email uniqueness if email is being updated
    if "email" in update_data:
        existing_person = db.query(Person).filter(
            Person.email == update_data["email"],
            Person.id != person_id
        ).first()
        if existing_person:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    for field, value in update_data.items():
        setattr(person, field, value)
    
    db.commit()
    db.refresh(person)
    return person

@router.delete("/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    """Delete a person."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    db.delete(person)
    db.commit()
    return {"message": "Person deleted successfully"}