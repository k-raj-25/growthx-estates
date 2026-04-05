from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from django_ckeditor_5.fields import CKEditor5Field


class City(models.Model):
    """Catalog of cities maintained in admin. Link properties to a city for geographic filters on the site."""

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Display order in admin and on filters (lower first).",
    )

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

    def _assign_unique_slug(self):
        base = (slugify(self.name) or "city")[:120]
        candidate = base
        n = 1
        while True:
            qs = City.objects.filter(slug=candidate)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if not qs.exists():
                self.slug = candidate
                return
            suffix = f"-{n}"
            candidate = f"{base[: 140 - len(suffix)]}{suffix}"
            n += 1

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self._assign_unique_slug()
        super().save(*args, **kwargs)


class Property(models.Model):
    """Residential / commercial listing shown on the public catalog and detail pages."""

    STATUS_READY = "Ready to move"
    STATUS_UNDER = "Under construction"
    STATUS_LAUNCH = "New launch"
    STATUS_CHOICES = [
        (STATUS_READY, STATUS_READY),
        (STATUS_UNDER, STATUS_UNDER),
        (STATUS_LAUNCH, STATUS_LAUNCH),
    ]

    TYPE_COMMERCIAL = "commercial"
    TYPE_RESIDENTIAL = "residential"
    TYPE_SCO = "sco"
    PROJECT_TYPE_CHOICES = [
        (TYPE_COMMERCIAL, "Commercial"),
        (TYPE_RESIDENTIAL, "Residential"),
        (TYPE_SCO, "SCO"),
    ]

    slug = models.SlugField(max_length=140, unique=True)
    name = models.CharField(max_length=200)
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
        help_text="When set, the project is grouped under this city in property filters (only cities with listings appear on the site).",
    )
    location = models.CharField(
        max_length=240,
        help_text="Address or area line shown on cards and detail (e.g. neighbourhood, full address).",
    )
    price_display = models.CharField(
        max_length=120,
        help_text='Shown on cards, e.g. "$1.25M — from"',
    )
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=4.5)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default=STATUS_READY)
    project_type = models.CharField(
        "Project type",
        max_length=20,
        choices=PROJECT_TYPE_CHOICES,
        default=TYPE_RESIDENTIAL,
        db_index=True,
    )
    brochure_url = models.URLField(max_length=500, blank=True)
    description = models.TextField()
    developer_name = models.CharField(max_length=200)
    about_developer = models.TextField()
    rera_id = models.CharField("RERA ID", max_length=120)
    project_size = models.CharField(
        max_length=200,
        help_text="E.g. acres, towers, unit count",
    )
    map_embed_url = models.URLField("Map embed URL", max_length=800)

    images = models.JSONField(
        default=list,
        help_text='Up to 10 image URLs as JSON list, e.g. ["https://...", "..."]',
    )
    amenities = models.JSONField(
        default=list,
        help_text='List of strings, e.g. ["Pool", "Gym"]',
    )
    videos = models.JSONField(
        default=list,
        help_text='Up to 2 objects: [{"title":"…","embed_url":"https://youtube.com/embed/…"}, …]',
    )
    faq = models.JSONField(
        default=list,
        help_text='List of objects: [{"q":"…","a":"…"}, …]',
    )

    is_published = models.BooleanField(default=True, db_index=True)
    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first on the properties page.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"slug": self.slug})

    @property
    def display_location(self) -> str:
        if self.city_id:
            return self.city.name
        return self.location

    @property
    def search_blob(self) -> str:
        blob_parts = [
            self.name,
            self.location,
            self.status,
            self.get_project_type_display(),
            self.project_type,
            self.developer_name,
            self.rera_id,
            self.project_size,
            " ".join(self.amenities) if isinstance(self.amenities, list) else "",
            self.description,
        ]
        if self.city_id:
            blob_parts.insert(1, self.city.name)
        return " ".join(str(p) for p in blob_parts if p).lower()

    def clean(self):
        super().clean()
        if not isinstance(self.images, list):
            raise ValidationError({"images": "Must be a JSON list of URLs."})
        if len(self.images) > 10:
            raise ValidationError({"images": "Maximum 10 images."})
        if not isinstance(self.amenities, list):
            raise ValidationError({"amenities": "Must be a JSON list of strings."})
        if not isinstance(self.videos, list):
            raise ValidationError({"videos": "Must be a JSON list."})
        if len(self.videos) > 2:
            raise ValidationError({"videos": "Maximum 2 videos."})
        for i, v in enumerate(self.videos):
            if not isinstance(v, dict) or "embed_url" not in v:
                raise ValidationError({"videos": f"Video {i + 1} needs title and embed_url keys."})
        if not isinstance(self.faq, list):
            raise ValidationError({"faq": "Must be a JSON list of {q, a} objects."})

    @classmethod
    def get_similar(cls, prop, limit=3):
        others = list(
            cls.objects.filter(is_published=True)
            .exclude(pk=prop.pk)
            .select_related("city")
            .order_by("sort_order", "name")
        )
        same = [p for p in others if p.status == prop.status]
        rest = [p for p in others if p.status != prop.status]
        return (same + rest)[:limit]

    def _assign_unique_slug(self):
        base = (slugify(self.name) or "property")[:120]
        candidate = base
        n = 1
        while True:
            qs = Property.objects.filter(slug=candidate)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if not qs.exists():
                self.slug = candidate
                return
            suffix = f"-{n}"
            candidate = f"{base[: 140 - len(suffix)]}{suffix}"
            n += 1

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self._assign_unique_slug()
        super().save(*args, **kwargs)


class SiteEnquiry(models.Model):
    """Contact form and property callback requests; distinguished by enquiry_type."""

    class EnquiryType(models.TextChoices):
        CALLBACK = "callback", "Property callback"
        CONTACT = "contact", "Contact us"

    enquiry_type = models.CharField(
        max_length=20,
        choices=EnquiryType.choices,
        db_index=True,
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    message = models.TextField(blank=True)
    property = models.ForeignKey(
        Property,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="site_enquiries",
        help_text="Set when the visitor requested a callback from a property page.",
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Site enquiry"
        verbose_name_plural = "Site enquiries"

    def __str__(self):
        label = self.get_enquiry_type_display()
        prop = f" — {self.property.name}" if self.property_id else ""
        return f"{label}: {self.name}{prop} ({self.phone})"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    excerpt = models.TextField(blank=True, help_text="Short summary shown on the blog index.")
    body = CKEditor5Field(config_name='default')
    featured_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    featured_image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Optional image URL (e.g. CDN). Shown when no file is uploaded above.",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog_posts",
    )
    is_published = models.BooleanField(default=False, db_index=True)
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Displayed on the article. Filled automatically when you first publish.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-pk"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def _assign_unique_slug(self):
        base = (slugify(self.title) or "post")[:200]
        candidate = base
        n = 1
        while True:
            qs = BlogPost.objects.filter(slug=candidate)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if not qs.exists():
                self.slug = candidate
                return
            suffix = f"-{n}"
            candidate = f"{base[: 220 - len(suffix)]}{suffix}"
            n += 1

    def save(self, *args, **kwargs):
        if self.title and not self.slug:
            self._assign_unique_slug()
        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)


class NewsEventsItem(models.Model):
    """Image tile for News & updates or Events highlights (published + image required on site)."""

    class Section(models.TextChoices):
        NEWS_UPDATES = "news", "News & updates"
        EVENTS_HIGHLIGHTS = "events", "Events highlights"

    section = models.CharField(
        max_length=16,
        choices=Section.choices,
        default=Section.NEWS_UPDATES,
        db_index=True,
        help_text="Which block on the News & updates page this item appears in.",
    )
    title = models.CharField(max_length=200)
    summary = models.TextField(
        blank=True,
        help_text="Optional caption; not shown on the image grid (for admin / future use).",
    )
    image = models.ImageField(upload_to="news-events/", blank=True, null=True)
    image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Optional image URL when no file is uploaded.",
    )
    link_url = models.URLField(
        "External link",
        max_length=500,
        blank=True,
        help_text="Optional related article or event page.",
    )
    is_published = models.BooleanField(
        default=True,
        db_index=True,
        help_text="Uncheck to hide this item from the website.",
    )
    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first within its section.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["section", "sort_order", "-created_at"]
        verbose_name = "News / event highlight"
        verbose_name_plural = "News & events gallery"

    def __str__(self):
        return self.title


class AwardRecognition(models.Model):
    """Award or recognition shown on the public page when marked published."""

    title = models.CharField(max_length=200)
    issuer = models.CharField(
        max_length=200,
        blank=True,
        help_text="Organization or publication that granted the recognition.",
    )
    year_label = models.CharField(
        "Year / period",
        max_length=40,
        blank=True,
        help_text='E.g. "2024" or "2023–2025".',
    )
    summary = models.TextField(
        blank=True,
        help_text="Short description on the awards page.",
    )
    image = models.ImageField(upload_to="awards/", blank=True, null=True)
    image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Optional image URL when no file is uploaded.",
    )
    link_url = models.URLField(
        "External link",
        max_length=500,
        blank=True,
        help_text="Optional link (press release, certificate, etc.).",
    )
    is_published = models.BooleanField(
        default=True,
        db_index=True,
        help_text="Uncheck to hide this item from the website.",
    )
    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first on the site.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "Award / recognition"
        verbose_name_plural = "Awards & recognitions"

    def __str__(self):
        return self.title


class CareersSettings(models.Model):
    """Singleton row: HR contact email shown on the public Careers page."""

    hr_email = models.EmailField(
        help_text="Address where candidates should email résumés (shown on the site).",
    )

    class Meta:
        verbose_name = "Careers / HR contact"
        verbose_name_plural = "Careers / HR contact"

    def __str__(self):
        return self.hr_email

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class JobOpening(models.Model):
    """Published role listed on the Careers page."""

    TYPE_FULL = "full_time"
    TYPE_PART = "part_time"
    TYPE_CONTRACT = "contract"
    TYPE_INTERN = "internship"
    EMPLOYMENT_TYPE_CHOICES = [
        (TYPE_FULL, "Full-time"),
        (TYPE_PART, "Part-time"),
        (TYPE_CONTRACT, "Contract"),
        (TYPE_INTERN, "Internship"),
    ]

    title = models.CharField(max_length=200)
    department = models.CharField(max_length=120, blank=True)
    location = models.CharField(
        max_length=200,
        blank=True,
        help_text="E.g. city, hybrid, or remote.",
    )
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default=TYPE_FULL,
    )
    description = models.TextField(
        help_text="Role summary and requirements (plain text on the site).",
    )
    responsibilities = models.TextField(
        blank=True,
        help_text="Shown in the role detail popup. One bullet per line (optional leading “- ”).",
    )
    qualifications = models.TextField(
        blank=True,
        help_text="Shown in the role detail popup. One bullet per line (optional leading “- ”).",
    )
    is_published = models.BooleanField(default=True, db_index=True)
    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "Job opening"
        verbose_name_plural = "Job openings"

    def __str__(self):
        return self.title
