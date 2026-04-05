# GrowthX Estates — Project documentation

This document describes how the real-estate marketing site works, what visitors see, and how to manage content through the Django admin. Everything is consolidated in this file for staff and developers.

---

## 1. What this project is

A **Django 4.2** website for **GrowthX Estates**. It presents:

- A **home** page with marketing sections
- A **property catalog** with search and filters, plus **property detail** pages
- A **blog** (rich text, pagination)
- **News & updates** and **events** image galleries
- **Awards & recognitions**
- **Careers** (HR email + job listings)
- **Contact**, **support**, **privacy**, **terms**, and **HTML sitemap** pages

Visitors can submit **enquiries** (general contact or property callback) via AJAX; submissions are stored and reviewed in the admin.

---

## 2. Technology stack

| Piece | Role |
|--------|------|
| Django | Web framework, admin, ORM |
| SQLite (local) or PostgreSQL (`DATABASE_URL`) | Database |
| django-ckeditor-5 | Rich text for blog posts |
| Pillow | Image uploads (blog, news, awards) |
| WhiteNoise | Static files in production |
| Gunicorn | WSGI server for deployment |

Dependencies are listed in `requirements.txt`.

---

## 3. Local setup and running the site

### 3.1 Environment

- **Python 3** with a virtual environment is recommended.
- Install packages:

  ```bash
  pip install -r requirements.txt
  ```

- Optional environment variables (see also `config/settings.py`):
  - `SECRET_KEY` — required in production; defaults in development
  - `DEBUG` — `1` / `true` / `yes` for development
  - `DATABASE_URL` — if set, uses PostgreSQL via `dj-database-url`; otherwise SQLite (`db.sqlite3`)
  - `ALLOWED_HOSTS` — comma-separated hostnames
  - `CSRF_TRUSTED_ORIGINS` — comma-separated origins (important behind HTTPS / proxies)
  - `RENDER` / `RENDER_EXTERNAL_HOSTNAME` — used when deployed on Render

### 3.2 Database and static files

From the project root (where `manage.py` lives):

```bash
python manage.py migrate
python manage.py collectstatic --noinput   # mainly for production-style runs
```

### 3.3 Admin user

```bash
python manage.py createsuperuser
```

Log in at **`/admin/`** (e.g. `http://127.0.0.1:8000/admin/`).

### 3.4 Development server

```bash
python manage.py runserver
```

Uploaded **media** (blog images, etc.) is served from `MEDIA_ROOT` when `DEBUG` is on (`/media/...`).

---

## 4. Public URLs (sitemap for the site)

| URL path | Purpose |
|----------|---------|
| `/` | Home |
| `/properties/` | Property list (search + filters) |
| `/properties/<slug>/` | Property detail |
| `/blog/` | Blog index (paginated) |
| `/blog/<slug>/` | Blog article |
| `/about/` | About |
| `/contact/` | Contact |
| `/awards/` | Awards & recognitions |
| `/news-updates/` | News & events galleries |
| `/careers/` | Careers + job openings |
| `/support/`, `/privacy-policy/`, `/terms/` | Policy / support pages |
| `/sitemap/` | Human-readable sitemap page |
| `POST /enquiries/submit/` | Enquiry form API (JSON; used by front-end JS) |
| `/ckeditor5/` | CKEditor 5 URLs (admin/editor) |

Navigation in the header/footer follows these routes (see `templates/base.html` and `website/urls.py`).

---

## 5. Django admin overview

After logging in at **`/admin/`**, you manage all content models under the **Website** app (names may appear as “Cities”, “Properties”, “Blog posts”, etc.).

**Common patterns:**

- **`is_published`** — controls visibility on the public site for most content types.
- **`sort_order`** — lower numbers appear first in lists (properties, news tiles, awards, jobs).
- **List filters and search** — use the right sidebar and top search box to find records quickly.
- **Editing** — open a record, change fields, click **Save** (or **Save and continue editing**).

---

## 6. Cities

**Admin:** **Cities** (`City` model).

**Why cities matter:** Properties can be linked to a city. The properties page **only shows cities that have at least one published property** in the city filter dropdown.

**Fields:**

| Field | Usage |
|--------|--------|
| **Name** | Display name (unique). |
| **Slug** | URL-safe identifier; can be filled automatically from the name if left blank on save. |
| **Sort order** | Order in admin and in the site’s city filter (lower first). |

**Workflow — add a city:**

1. Admin → **Cities** → **Add city**.
2. Enter **Name** (and optionally **Slug**).
3. Set **Sort order** if you care about dropdown order.
4. **Save**.

Then assign properties to this city so the city appears on the public properties page.

---

## 7. Properties (listings)

**Admin:** **Properties** (`Property` model).

**Public behavior:**

- Only rows with **`is_published`** checked appear on `/properties/` and `/properties/<slug>/`.
- Ordering on the list page: **`sort_order`**, then **name**.
- **Similar properties** on a detail page prefer the same **status**, then others.

### 7.1 Main fields (first fieldset)

| Field | Notes |
|--------|--------|
| **Name** | Project title. |
| **Slug** | URL segment; auto-generated from name if empty. Must be unique. |
| **Project type** | Commercial, Residential, or SCO — used in filters. |
| **City** | Optional FK; autocomplete in admin. Drives “city” filter on the site when set. |
| **Location** | Area/address line on cards and detail. |
| **Price display** | Free-text label (e.g. “From ₹X Cr”). |
| **Rating** | Decimal shown on UI (default 4.5). |
| **Status** | Ready to move / Under construction / New launch — filterable on the site. |
| **Is published** | Uncheck to hide everywhere public. |
| **Sort order** | Lower = earlier in the list. Editable from the changelist. |

### 7.2 Content

| Field | Notes |
|--------|--------|
| **Description** | Plain text body for the property. |
| **Brochure URL** | Link to PDF or external brochure. |
| **Map embed URL** | Typically a Google Maps embed URL for the detail page map. |

### 7.3 Lists (JSON) — important

These fields must be **valid JSON** as described below. Invalid JSON or wrong shapes will fail **model validation** on save.

**Images** — JSON **array** of up to **10** image URL strings:

```json
["https://example.com/img1.jpg", "https://example.com/img2.jpg"]
```

**Amenities** — JSON **array** of strings:

```json
["Swimming pool", "Gym", "Clubhouse"]
```

**Videos** — JSON **array** of up to **2** objects with at least **`embed_url`** (and typically **`title`**):

```json
[
  {"title": "Walkthrough", "embed_url": "https://www.youtube.com/embed/VIDEO_ID"}
]
```

**FAQ** — JSON **array** of objects with **`q`** and **`a`**:

```json
[
  {"q": "Possession date?", "a": "Expected by Q4 2026."}
]
```

### 7.4 Developer & compliance

| Field | Usage |
|--------|--------|
| **Developer name**, **About developer** | Shown on the detail page. |
| **RERA ID** | Compliance ID; searchable in admin and from property search. |
| **Project size** | Short phrase (acres, towers, units, etc.). |

### 7.5 Guides — frequent tasks

**Add a new property**

1. Admin → **Properties** → **Add property**.
2. Fill **Name**; leave **Slug** blank to auto-fill, or set it manually.
3. Choose **Project type**, **City** (optional but recommended), **Location**, **Price display**, **Status**, **Rating**.
4. Check **Is published** when ready to go live.
5. Set **Sort order** if you need a fixed position in the catalog.
6. Complete **Content** and **Developer & compliance**.
7. Paste valid JSON for **images**, **amenities**, **videos**, **faq** (see examples above).
8. **Save**.

**Edit an existing property**

1. **Properties** → click the property → change fields → **Save**.
2. To temporarily hide: uncheck **Is published** (no need to delete).

**Unpublish vs delete**

- **Unpublish** keeps data and history; URL returns 404 for visitors.
- **Delete** removes the row (and can break bookmarks). Prefer unpublishing unless you are sure.

**Search on the public properties page**

The `q` query parameter searches (case-insensitive) across: name, location, city name, project type, developer name, RERA ID, description, project size, and amenities (JSON text). Filters:

- **`status`** — multiple values allowed (checkboxes).
- **`city`** — city **slug**.
- **`project_type`** — `commercial`, `residential`, or `sco`.

Changing city or project type or status checkboxes **auto-submits** the filter form (see `static/js/properties-filters.js`).

---

## 8. Blog posts

**Admin:** **Blog posts** (`BlogPost` model).

**Public:** `/blog/` lists published posts (6 per page). `/blog/<slug>/` shows one article.

### 8.1 Fields

| Field | Notes |
|--------|--------|
| **Title** | Headline. |
| **Slug** | On **create**, the slug is hidden from the main form and is auto-generated from the title when you save. On **edit**, **slug is read-only** — titles can change without breaking old URLs. |
| **Excerpt** | Short summary on the blog index. |
| **Body** | CKEditor 5 rich text (headings, lists, links, etc.). |
| **Featured image** | Upload to `media/blog/`. |
| **Featured image URL** | Optional; used when no file is uploaded (e.g. CDN). |
| **Author** | Optional FK to a user; if left empty on save, the **current admin user** may be set automatically (see `BlogPostAdmin.save_model`). |
| **Is published** | Must be checked for the post to appear publicly. |
| **Published at** | Shown on the article; when you first publish (`is_published` True) and this is empty, **it is set automatically** to the next save time. |

### 8.2 Guides

**Write a new post**

1. **Blog posts** → **Add blog post**.
2. Enter **Title**, **Excerpt**, compose **Body** in the editor.
3. Add **Featured image** and/or **FeaturedImage URL**.
4. Choose **Author** if needed; otherwise saving as yourself may assign you (staff user).
5. Set **Is published** and optionally **Published at** (or let the first publish fill it).
6. **Save** — slug is created in the background.

**Edit a post**

1. Open the post from the list.
2. Change **Title**, **Body**, images, publish flags, etc. **Slug stays fixed** to preserve the public URL.

**Unpublish**

Uncheck **Is published** and **Save**. The post disappears from `/blog/` and returns 404 on its detail URL.

**File uploads in CKEditor**

`CKEDITOR_5_FILE_UPLOAD_PERMISSION = 'staff'` — typically only staff users can upload through the editor.

---

## 9. News & events gallery

**Admin:** **News & events gallery** (`NewsEventsItem`).

**Public:** `/news-updates/`. Items appear in two blocks:

- **News & updates** (`section = news`)
- **Events highlights** (`section = events`)

**Important:** Only items that are **published** and have an **image** (uploaded file **or** non-empty **image URL**) appear on the site (`website/views.news_updates_events`).

**Fields:**

- **Section** — which block on the page.
- **Title**, **Summary** (summary is optional; not shown on the current image grid but kept for admin/future use).
- **Image** or **Image URL** — at least one must be present for the tile to show publicly.
- **External link** — optional click-through URL.
- **Is published**, **Sort order**.

**Workflow:** Add → choose section → add image or URL → set sort order → publish.

---

## 10. Awards & recognitions

**Admin:** **Awards & recognitions** (`AwardRecognition`).

**Public:** `/awards/`. Only **published** rows with an **image** (file or **image URL**) are shown.

**Fields:** Title, issuer, year/period, summary, image or image URL, external link, publish flag, sort order.

---

## 11. Careers

### 11.1 HR contact (singleton)

**Admin:** **Careers / HR contact** (`CareersSettings`).

- Only **one** row is intended: **Add** is disabled if a row already exists; **Delete** is disabled.
- **HR email** is shown on `/careers/` for applications.

If no row exists, the site falls back to a default email string in code (`website/views.careers` — verify in deployment if you rely on this).

### 11.2 Job openings

**Admin:** **Job openings** (`JobOpening`).

**Public:** Listed on `/careers/` when **is published** is true. Ordering: **sort order**, then newest.

**Fields include:** Title, department, location, employment type, description (plain text on site), **responsibilities** and **qualifications** (shown in a detail popup; one bullet per line, optional leading “- ”), publish flag, sort order.

---

## 12. Site enquiries

**Admin:** **Site enquiries** (`SiteEnquiry`).

**What gets stored:**

- **Enquiry type:** **Property callback** or **Contact us**.
- **Name**, **Phone** (validated as **10 digits**), optional **message**.
- **Property** — set automatically for **callback** when the visitor submits from a property page (matched by slug).

**Viewing:** Use list display columns, filters by type and date, date hierarchy, and search by name, phone, message, or property.

**Technical note:** Forms post to `POST /enquiries/submit/` with CSRF; responses are JSON (`{"ok": true}` or validation errors). Front-end logic lives in `static/js/enquiry.js`.

---

## 13. Static / policy pages

These views render templates only (no database content except global context):

- About, Contact, Support, Privacy policy, Terms, Sitemap HTML

To change wording or layout, edit the corresponding files under `templates/` (and any linked CSS/JS).

---

## 14. Security and production notes

- With **`DEBUG=False`**, Django enables SSL redirect and secure cookies as configured in `settings.py`.
- Set a strong **`SECRET_KEY`** and restrict **`ALLOWED_HOSTS`** / **`CSRF_TRUSTED_ORIGINS`** for your domain.
- **User accounts:** Only trusted staff should have admin access; blog author is linked to Django users.

---

## 15. Quick reference — admin models

| Admin section | Model | Primary public effect |
|---------------|--------|------------------------|
| Cities | `City` | Property city filter |
| Properties | `Property` | Catalog + detail pages |
| Blog posts | `BlogPost` | Blog |
| News & events gallery | `NewsEventsItem` | `/news-updates/` |
| Awards & recognitions | `AwardRecognition` | `/awards/` |
| Careers / HR contact | `CareersSettings` | Careers email |
| Job openings | `JobOpening` | Careers list |
| Site enquiries | `SiteEnquiry` | Leads / messages |

---

## 16. Where to look in the code

| Concern | Location |
|---------|-----------|
| URL routes | `website/urls.py`, `config/urls.py` |
| Views & blog classes | `website/views.py` |
| Models & validation | `website/models.py` |
| Admin registration | `website/admin.py` |
| Enquiry form | `website/forms.py` |
| Settings / CKEditor / DB | `config/settings.py` |
| Property filters (JS) | `static/js/properties-filters.js` |
| Enquiry AJAX (JS) | `static/js/enquiry.js` |

This file is the single reference for **how the product behaves** and **how to operate it from the admin**. For Django framework topics, see the [Django 4.2 documentation](https://docs.djangoproject.com/en/4.2/).
