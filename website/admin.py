from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.db.models import Count, Q

from .models import (
    AwardRecognition,
    BlogPost,
    CareersSettings,
    City,
    JobOpening,
    NewsEventsItem,
    Property,
    SiteEnquiry,
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "sort_order", "listing_count")
    list_editable = ("sort_order",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order", "name")

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _listing_count=Count("properties", filter=Q(properties__is_published=True), distinct=True)
        )

    @admin.display(description="Listings", ordering="_listing_count")
    def listing_count(self, obj):
        return getattr(obj, "_listing_count", 0)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "project_type",
        "city",
        "location",
        "status",
        "rating",
        "is_published",
        "sort_order",
        "updated_at",
    )
    list_filter = ("is_published", "status", "project_type", "city")
    list_editable = ("is_published", "sort_order")
    search_fields = ("name", "location", "rera_id", "developer_name", "slug")
    autocomplete_fields = ("city",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order", "name")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "project_type",
                    "city",
                    "location",
                    "price_display",
                    "rating",
                    "status",
                    "is_published",
                    "sort_order",
                ),
            },
        ),
        (
            "Content",
            {
                "fields": ("description", "brochure_url", "map_embed_url"),
            },
        ),
        (
            "Lists (JSON)",
            {
                "description": "Use valid JSON arrays. See help text on each field.",
                "fields": ("images", "amenities", "videos", "faq"),
            },
        ),
        (
            "Developer & compliance",
            {
                "fields": ("developer_name", "about_developer", "rera_id", "project_size"),
            },
        ),
        (
            "Timestamps",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "is_published",
        "published_at",
        "updated_at",
    )
    list_filter = ("is_published",)
    search_fields = ("title", "excerpt", "body")
    readonly_fields = ("slug", "created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "body",
                    "featured_image",
                    "featured_image_url",
                    "author",
                    "is_published",
                    "published_at",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        ro = ["created_at", "updated_at"]
        if obj:
            ro.insert(0, "slug")
        return ro

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return (
                (
                    None,
                    {
                        "fields": (
                            "title",
                            "excerpt",
                            "body",
                            "featured_image",
                            "featured_image_url",
                            "author",
                            "is_published",
                            "published_at",
                        ),
                    },
                ),
                (
                    "Timestamps",
                    {
                        "classes": ("collapse",),
                        "fields": ("created_at", "updated_at"),
                    },
                ),
            )
        return super().get_fieldsets(request, obj)

    def save_model(self, request, obj, form, change):
        if not obj.author_id and request.user.is_authenticated:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(NewsEventsItem)
class NewsEventsItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "section",
        "is_published",
        "sort_order",
        "updated_at",
    )
    list_filter = ("section", "is_published")
    list_editable = ("is_published", "sort_order")
    search_fields = ("title", "summary")
    ordering = ("section", "sort_order", "-created_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "section",
                    "title",
                    "summary",
                    "image",
                    "image_url",
                    "link_url",
                    "is_published",
                    "sort_order",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(AwardRecognition)
class AwardRecognitionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "issuer",
        "year_label",
        "is_published",
        "sort_order",
        "updated_at",
    )
    list_filter = ("is_published",)
    list_editable = ("is_published", "sort_order")
    search_fields = ("title", "issuer", "summary")
    ordering = ("sort_order", "-created_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "issuer",
                    "year_label",
                    "summary",
                    "image",
                    "image_url",
                    "link_url",
                    "is_published",
                    "sort_order",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(CareersSettings)
class CareersSettingsAdmin(admin.ModelAdmin):
    list_display = ("hr_email",)

    def has_add_permission(self, request):
        return not CareersSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "department",
        "location",
        "employment_type",
        "is_published",
        "sort_order",
        "updated_at",
    )
    list_filter = ("is_published", "employment_type", "department")
    list_editable = ("is_published", "sort_order")
    search_fields = (
        "title",
        "department",
        "location",
        "description",
        "responsibilities",
        "qualifications",
    )
    ordering = ("sort_order", "-created_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "department",
                    "location",
                    "employment_type",
                    "description",
                    "responsibilities",
                    "qualifications",
                    "is_published",
                    "sort_order",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "classes": ("collapse",),
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(SiteEnquiry)
class SiteEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "enquiry_type",
        "name",
        "phone",
        "property",
        "message_preview",
    )
    list_filter = (
        "enquiry_type",
        ("created_at", DateFieldListFilter),
    )
    search_fields = ("name", "phone", "message", "property__name", "property__slug")
    readonly_fields = ("created_at",)
    autocomplete_fields = ("property",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    @admin.display(description="Message")
    def message_preview(self, obj):
        if not obj.message:
            return "—"
        t = obj.message.strip()
        return (t[:80] + "…") if len(t) > 80 else t
