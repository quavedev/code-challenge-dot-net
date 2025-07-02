from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Community(Base):
    __tablename__ = "communities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship with people
    people = relationship("Person", back_populates="community")

class Person(Base):
    __tablename__ = "people"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    company_name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    community_id = Column(Integer, ForeignKey("communities.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    community = relationship("Community", back_populates="people")
    check_ins = relationship("CheckIn", back_populates="person")
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class CheckIn(Base):
    __tablename__ = "check_ins"
    
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    check_in_time = Column(DateTime(timezone=True), server_default=func.now())
    check_out_time = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    person = relationship("Person", back_populates="check_ins")