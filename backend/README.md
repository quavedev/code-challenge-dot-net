# Quave Challenge API

Python backend for the Event Check-in System using FastAPI and PostgreSQL.

## Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. **Set up database:**
   - Create a PostgreSQL database named `quave_challenge`
   - Update the DATABASE_URL in `.env`

4. **Run the development server:**
   ```bash
   poetry run uvicorn app.main:app --reload --port 8000
   ```

The API will be available at http://localhost:8000
API documentation: http://localhost:8000/docs

## TODO

This is a skeleton implementation. You need to implement:

- [ ] Database relationships in models
- [ ] API endpoints for communities, people, and check-ins
- [ ] Database migrations with Alembic
- [ ] Business logic for check-in/check-out
- [ ] Event summary endpoints

## Database Schema

The basic models are defined in `app/models.py`:
- `Community` - Events/communities
- `Person` - Registered attendees  
- `CheckIn` - Check-in/check-out records

## API Documentation

- API Base URL: http://localhost:8000
- Interactive API Documentation: http://localhost:8000/docs
- Alternative API Documentation: http://localhost:8000/redoc

## API Endpoints

### Communities (Events)
- `GET /api/communities/` - List all events
- `POST /api/communities/` - Create new event
- `GET /api/communities/{id}` - Get specific event
- `GET /api/communities/{id}/people` - Get people registered for event

### People
- `GET /api/people/` - List all people
- `POST /api/people/` - Register new person
- `GET /api/people/{id}` - Get person details
- `PUT /api/people/{id}` - Update person information
- `DELETE /api/people/{id}` - Delete person

### Check-ins
- `POST /api/check-ins/{person_id}/check-in` - Check in person
- `PUT /api/check-ins/{person_id}/check-out` - Check out person
- `GET /api/check-ins/{person_id}/current` - Get current check-in status
- `GET /api/check-ins/events/{community_id}/summary` - Get event summary

## Development

### Running Tests
```bash
poetry run pytest
```

### Database Operations

**Create new migration:**
```bash
poetry run alembic revision --autogenerate -m "Description of changes"
```

**Apply migrations:**
```bash
poetry run alembic upgrade head
```

**Rollback migration:**
```bash
poetry run alembic downgrade -1
```

### Project Structure

```
backend/
├── app/
│   ├── models/
│   │   └── models.py          # SQLAlchemy models
│   ├── routers/
│   │   ├── communities.py     # Community/Event endpoints
│   │   ├── people.py          # People management endpoints
│   │   └── check_ins.py       # Check-in/out endpoints
│   ├── services/
│   │   └── check_in_service.py # Business logic
│   ├── database.py            # Database configuration
│   ├── schemas.py             # Pydantic models
│   └── main.py                # FastAPI application
├── alembic/                   # Database migrations
├── seed_data.py               # Sample data seeding
├── pyproject.toml             # Poetry dependencies
└── docker-compose.yml         # PostgreSQL setup
```

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
  - Default: `postgresql://postgres:password@localhost:5432/quave_challenge`