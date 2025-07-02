from sqlalchemy.orm import Session
from sqlalchemy import and_, desc
from app.models.models import CheckIn, Person, Community
from app.schemas import CheckInCreate, EventSummary, CompanyBreakdown
from datetime import datetime
from typing import Optional, List

class CheckInService:
    
    @staticmethod
    def check_in_person(db: Session, person_id: int) -> CheckIn:
        """Check in a person. Only allows check-in if not currently checked in."""
        # Check if person exists
        person = db.query(Person).filter(Person.id == person_id).first()
        if not person:
            raise ValueError("Person not found")
        
        # Check if already checked in (has check-in without check-out)
        existing_check_in = db.query(CheckIn).filter(
            and_(
                CheckIn.person_id == person_id,
                CheckIn.check_out_time.is_(None)
            )
        ).first()
        
        if existing_check_in:
            raise ValueError("Person is already checked in")
        
        # Create new check-in
        check_in = CheckIn(person_id=person_id)
        db.add(check_in)
        db.commit()
        db.refresh(check_in)
        
        return check_in
    
    @staticmethod
    def check_out_person(db: Session, person_id: int) -> CheckIn:
        """Check out a person. Only allows check-out if currently checked in."""
        # Find the current check-in (without check-out)
        current_check_in = db.query(CheckIn).filter(
            and_(
                CheckIn.person_id == person_id,
                CheckIn.check_out_time.is_(None)
            )
        ).first()
        
        if not current_check_in:
            raise ValueError("Person is not currently checked in")
        
        # Update check-out time
        current_check_in.check_out_time = datetime.utcnow()
        db.commit()
        db.refresh(current_check_in)
        
        return current_check_in
    
    @staticmethod
    def get_current_check_in(db: Session, person_id: int) -> Optional[CheckIn]:
        """Get the current check-in for a person (if any)."""
        return db.query(CheckIn).filter(
            and_(
                CheckIn.person_id == person_id,
                CheckIn.check_out_time.is_(None)
            )
        ).first()
    
    @staticmethod
    def get_person_check_ins(db: Session, person_id: int) -> List[CheckIn]:
        """Get all check-ins for a person, ordered by most recent."""
        return db.query(CheckIn).filter(
            CheckIn.person_id == person_id
        ).order_by(desc(CheckIn.check_in_time)).all()
    
    @staticmethod
    def get_event_summary(db: Session, community_id: int) -> EventSummary:
        """Get summary statistics for an event/community."""
        # Get all people registered for the event
        people = db.query(Person).filter(Person.community_id == community_id).all()
        total_registered = len(people)
        
        # Get currently checked in people
        current_attendees = db.query(CheckIn).join(Person).filter(
            and_(
                Person.community_id == community_id,
                CheckIn.check_out_time.is_(None)
            )
        ).count()
        
        not_checked_in = total_registered - current_attendees
        
        # Get company breakdown of current attendees
        company_breakdown_query = db.query(
            Person.company_name,
            db.func.count(Person.id).label('count')
        ).join(CheckIn).filter(
            and_(
                Person.community_id == community_id,
                CheckIn.check_out_time.is_(None)
            )
        ).group_by(Person.company_name).all()
        
        company_breakdown = [
            CompanyBreakdown(company_name=company, count=count)
            for company, count in company_breakdown_query
        ]
        
        return EventSummary(
            total_registered=total_registered,
            current_attendees=current_attendees,
            not_checked_in=not_checked_in,
            company_breakdown=company_breakdown
        )