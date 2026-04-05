# GrowthX Estates

Django marketing site for a real-estate brand: property catalog with search and filters, blog, news and events, awards, careers, contact flows, and enquiry capture.

## Requirements

- Python 3.10+ recommended
- See `requirements.txt` for packages (Django 4.2, CKEditor 5, Pillow, etc.)

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- **Site:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

For production, set `SECRET_KEY`, `DEBUG=false`, `ALLOWED_HOSTS`, and optionally `DATABASE_URL` (PostgreSQL). Details are in `config/settings.py` and **[DOCUMENTATION.md](DOCUMENTATION.md)**.

## Documentation

**[DOCUMENTATION.md](DOCUMENTATION.md)** is the full guide: every public URL, admin workflows (properties, blog, news, awards, careers, enquiries), JSON field formats for listings, and where to find code.

## Project layout

| Path | Purpose |
|------|---------|
| `config/` | Django project settings and root URLs |
| `website/` | App: models, views, admin, forms |
| `templates/` | HTML templates |
| `static/` | CSS, JavaScript, assets |
| `media/` | User uploads (created at runtime; not always in repo) |
