# Django scaffold

Minimal Django project scaffold created in the workspace.

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

To push to GitHub:

```powershell
git remote add origin https://github.com/<your-username>/<repo>.git
git branch -M main
git push -u origin main
```

Files of interest:
- `manage.py` — Django entrypoint
- `mysite/settings.py` — main configuration
- `core/` — simple home page and site config model
- `blog/` — example posts app with templates and admin registration
