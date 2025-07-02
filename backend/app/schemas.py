from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# Community schemas
class CommunityBase(BaseModel):
    name: str
    description: Optional[str] = None

class CommunityCreate(CommunityBase):
    pass

class Community(CommunityBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Person schemas
class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    company_name: str
    title: str

class PersonCreate(PersonBase):
    community_id: int

class PersonUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    company_name: Optional[str] = None
    title: Optional[str] = None

class Person(PersonBase):
    id: int
    community_id: int
    created_at: datetime
    full_name: str
    
    class Config:
        from_attributes = True

# CheckIn schemas
class CheckInBase(BaseModel):
    person_id: int

class CheckInCreate(CheckInBase):
    pass

class CheckOutUpdate(BaseModel):
    check_out_time: datetime

class CheckIn(CheckInBase):
    id: int
    check_in_time: datetime
    check_out_time: Optional[datetime] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

# Response schemas with relationships
class PersonWithCheckIns(Person):
    check_ins: List[CheckIn] = []
    current_check_in: Optional[CheckIn] = None

class CommunityWithPeople(Community):
    people: List[PersonWithCheckIns] = []

# Summary schemas
class CompanyBreakdown(BaseModel):
    company_name: str
    count: int

class EventSummary(BaseModel):
    total_registered: int
    current_attendees: int
    not_checked_in: int
    company_breakdown: List[CompanyBreakdown]