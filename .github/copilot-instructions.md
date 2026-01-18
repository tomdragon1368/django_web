# Copilot instructions — Django web project (repo scan returned no direct project files)

Summary
- This repository currently contains no discoverable Django entrypoints (no `manage.py`, `settings.py`, `requirements.txt`, or `README.md` found by the initial workspace scan). These instructions describe what an AI coding agent should do to become productive if/when the project files are present.

Quick first steps (mandatory)
- Run a workspace scan to locate key files: `manage.py`, `<project>/settings.py`, `requirements.txt`, `pyproject.toml`, `Pipfile`, `Dockerfile`, `docker-compose.yml`, `.env.example`, and `README.md`.
- Example scan commands:
  - `dir /s manage.py` (Windows) or `rg --files | rg -n "manage.py|settings.py|requirements|pyproject|Dockerfile|docker-compose.yml|README.md"`
- If the repo contains Django files, run these to set up a dev env:
  - Create venv and activate: `python -m venv .venv` then `.venv\Scripts\activate` (Windows).
  - Install deps: `pip install -r requirements.txt` or `pip install -e .` / `pip install -r requirements/dev.txt` if available.

Project structure expectations (what to look for)
- Django entrypoint: `manage.py` at repo root.
- Django project package: a top-level folder containing `settings.py`, `wsgi.py`, `asgi.py`. Example: `django_web/settings.py`.
- Apps: folders with `models.py`, `views.py`, `admin.py`, and `migrations/` subfolders.
- Templates/static: `templates/` and `static/` directories, usually adjacent to apps or in a `core/` folder.

Common project-specific conventions to check before editing
- Settings management: check for a split `settings` package (e.g., `settings/base.py`, `settings/local.py`) or use of environment variables via `django-environ` / `python-decouple`. Adjust modifications to the correct settings file.
- Secrets: look for `.env` or `.env.example`. Do not hard-code secrets; prefer adding keys to `.env.example` and documenting required env vars in `README.md`.
- Migrations: keep DB schema changes isolated. If you modify models, run `python manage.py makemigrations` then `python manage.py migrate` and include migration files in the commit.
- Data flows: identify major integrations in `settings.py` (DATABASES, CACHES, CELERY_BROKER_URL, EMAIL_BACKEND). Update connection strings in `.env` instead of code.

Build, test, and debug workflows to try
- Dev server: `python manage.py runserver` (check for alternate commands in `README.md` or `Procfile`).
- Tests: `python manage.py test` (if `pytest` is used, prefer `pytest -q`).
- Lint / format: look for `pyproject.toml` or `setup.cfg` to detect `black`, `flake8`, `ruff` usage. Run `black .` and `flake8` if present.
- Docker: if `Dockerfile` or `docker-compose.yml` exist, prefer reading them to learn about service dependencies (postgres, redis, celery). Example: `docker-compose up --build`.

Integration points and external dependencies (how to find them)
- Search `settings.py` (or settings package) for `DATABASES`, `CACHES`, `CELERY`, `CHANNEL_LAYERS`, `REST_FRAMEWORK`, `SOCIAL_AUTH` keys.
- Look for environment-driven config via `os.environ` or `environ.Env` usage; those keys are the single source of truth for secrets and hostnames.

Codebase patterns and examples (what to prefer)
- Views: prefer class-based views under `views.py` or a `views/` package — match existing style when adding features.
- Serializers / API: if `rest_framework` or `serializers.py` exist, follow existing serializer patterns and reuse viewsets where present.
- Database access: prefer using Django ORM and model managers; when raw SQL exists, keep changes minimal and add tests.

What NOT to do
- Do not guess service credentials or modify production configs. If you need to run services, add `.env.example` keys and document steps in `README.md`.

If you can’t find project files
- Report back listing which files are missing (e.g., `manage.py`, `requirements.txt`). Ask the repo owner where the Django project lives or request a refreshed workspace with project files present.

When you finish changes
- Run the test suite and linters locally.
- Add/commit migrations with descriptive messages.
- Update `README.md` with any new developer commands you introduce.

Questions for the repo owner
- Please confirm the project root (where `manage.py` lives) if it’s not at workspace root.
- Provide `requirements.txt` or `pyproject.toml` if dependencies are missing from the workspace.

— End of instructions —

If you want this tailored further, re-run the scan or provide the path to the Django project inside the workspace and I will merge concrete file examples into this document.
