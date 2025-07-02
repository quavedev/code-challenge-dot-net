#!/usr/bin/env python3
"""
Seed script to populate the database with sample data.
Run this after setting up the database and running migrations.
"""

from sqlalchemy.orm import sessionmaker
from app.database import engine
from app.models.models import Community, Person

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_database():
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(Community).first():
            print("Database already contains data. Skipping seed.")
            return
        
        # Create sample communities (events)
        communities = [
            Community(
                name="Tech Conference 2024",
                description="Annual technology conference featuring the latest in software development"
            ),
            Community(
                name="Startup Meetup",
                description="Monthly meetup for startup founders and entrepreneurs"
            ),
            Community(
                name="Python Workshop",
                description="Hands-on Python programming workshop for beginners"
            )
        ]
        
        for community in communities:
            db.add(community)
        
        db.commit()
        
        # Get the created communities
        tech_conf = db.query(Community).filter(Community.name == "Tech Conference 2024").first()
        startup_meetup = db.query(Community).filter(Community.name == "Startup Meetup").first()
        python_workshop = db.query(Community).filter(Community.name == "Python Workshop").first()
        
        # Create sample people
        people = [
            # Tech Conference attendees
            Person(
                first_name="John",
                last_name="Doe",
                email="john.doe@techcorp.com",
                company_name="TechCorp",
                title="Senior Developer",
                community_id=tech_conf.id
            ),
            Person(
                first_name="Jane",
                last_name="Smith",
                email="jane.smith@innovate.io",
                company_name="Innovate.io",
                title="Product Manager",
                community_id=tech_conf.id
            ),
            Person(
                first_name="Mike",
                last_name="Johnson",
                email="mike.johnson@datatech.com",
                company_name="DataTech",
                title="Data Scientist",
                community_id=tech_conf.id
            ),
            Person(
                first_name="Sarah",
                last_name="Wilson",
                email="sarah.wilson@techcorp.com",
                company_name="TechCorp",
                title="UX Designer",
                community_id=tech_conf.id
            ),
            
            # Startup Meetup attendees
            Person(
                first_name="Alex",
                last_name="Brown",
                email="alex.brown@startup1.com",
                company_name="Startup One",
                title="CEO",
                community_id=startup_meetup.id
            ),
            Person(
                first_name="Emily",
                last_name="Davis",
                email="emily.davis@venture.co",
                company_name="Venture Co",
                title="CTO",
                community_id=startup_meetup.id
            ),
            
            # Python Workshop attendees
            Person(
                first_name="Tom",
                last_name="Anderson",
                email="tom.anderson@learner.edu",
                company_name="University",
                title="Student",
                community_id=python_workshop.id
            ),
            Person(
                first_name="Lisa",
                last_name="Garcia",
                email="lisa.garcia@newbie.com",
                company_name="Newbie Corp",
                title="Junior Developer",
                community_id=python_workshop.id
            )
        ]
        
        for person in people:
            db.add(person)
        
        db.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(communities)} communities and {len(people)} people.")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()