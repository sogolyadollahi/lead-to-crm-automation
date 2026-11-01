# Lead-to-CRM Automation

Milestone 1 project foundation for a lead processing and CRM automation system.

## Current scope

Implemented:
- FastAPI application initialization
- Centralized environment-based settings
- Health endpoint
- PostgreSQL service in Docker Compose
- Dockerfile
- Initial health endpoint test

Not implemented yet:
- Database connectivity, models, and migrations
- Lead creation and retrieval
- Validation and deduplication
- LLM categorization and email drafts
- CRM synchronization
- n8n workflow

## Requirements

- Python 3.12+
- Docker Desktop (for containerized execution)

## Local setup (PowerShell)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Open:
- Health: http://127.0.0.1:8000/health
- Swagger UI: http://127.0.0.1:8000/docs

Run tests:

```powershell
pytest -v
```

## Docker

```powershell
docker compose up --build -d
docker compose ps
docker compose logs api
```

Stop containers while preserving the database volume:

```powershell
docker compose down
```

## Important

The current `/health` endpoint checks application liveness only. It does not yet verify database readiness. The database container is started and health-checked by Docker Compose, but database integration belongs to Milestone 2.
