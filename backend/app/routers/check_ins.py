from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CheckIn as CheckInSchema, EventSummary
from app.services.check_in_service import CheckInService

router = APIRouter(prefix="/check-ins", tags=["check-ins"])

@router.post("/{person_id}/check-in", response_model=CheckInSchema)
def check_in_person(person_id: int, db: Session = Depends(get_db)):
    """Check in a person."""
    try:
        check_in = CheckInService.check_in_person(db, person_id)
        return check_in
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{person_id}/check-out", response_model=CheckInSchema)
def check_out_person(person_id: int, db: Session = Depends(get_db)):
    """Check out a person."""
    try:
        check_in = CheckInService.check_out_person(db, person_id)
        return check_in
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{person_id}/current", response_model=CheckInSchema)
def get_current_check_in(person_id: int, db: Session = Depends(get_db)):
    """Get current check-in status for a person."""
    check_in = CheckInService.get_current_check_in(db, person_id)
    if not check_in:
        raise HTTPException(status_code=404, detail="Person is not currently checked in")
    return check_in

@router.get("/events/{community_id}/summary", response_model=EventSummary)
def get_event_summary(community_id: int, db: Session = Depends(get_db)):
    """Get event summary with attendance statistics."""
    try:
        summary = CheckInService.get_event_summary(db, community_id)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")