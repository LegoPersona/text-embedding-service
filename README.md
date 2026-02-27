# text-embedding-service
## Purpose
provides a simple api to interact with a text embedding model, which creates the required vectors to represent similarity between the request lego persona and the existing modules.

## Tech Stack
python, fastapi, `all-MiniLM-L6-v2` model.

## How to Run (Local)
```
source .venv/bin/activate
uvicorn app.main:app --reload
```