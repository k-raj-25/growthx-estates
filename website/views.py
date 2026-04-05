from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView

from .forms import SiteEnquiryForm
from .models import (
    AwardRecognition,
    BlogPost,
    CareersSettings,
    City,
    JobOpening,
    NewsEventsItem,
    Property,
)


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def support(request):
    return render(request, "support.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def terms(request):
    return render(request, "terms.html")


def site_sitemap(request):
    return render(request, "sitemap.html")


def careers(request):
    settings_row = CareersSettings.objects.first()
    hr_email = (
        settings_row.hr_email
        if settings_row
        else "hello@growthestates.com"
    )
    openings = list(
        JobOpening.objects.filter(is_published=True).order_by(
            "sort_order", "-created_at"
        )
    )
    opening_departments = sorted(
        {
            (o.department or "").strip()
            for o in JobOpening.objects.filter(is_published=True)
            if (o.department or "").strip()
        }
    )
    openings_payload = [
        {
            "id": o.pk,
            "title": o.title,
            "department": o.department or "",
            "location": o.location or "",
            "employmentType": o.get_employment_type_display(),
            "description": o.description,
            "responsibilities": o.responsibilities or "",
            "qualifications": o.qualifications or "",
        }
        for o in openings
    ]
    return render(
        request,
        "careers.html",
        {
            "openings": openings,
            "opening_departments": opening_departments,
            "openings_payload": openings_payload,
            "hr_email": hr_email,
        },
    )


def awards_recognitions(request):
    awards = AwardRecognition.objects.filter(is_published=True).filter(
        (Q(image__isnull=False) & ~Q(image="")) | ~Q(image_url="")
    )
    return render(request, "awards.html", {"awards": awards})


def news_updates_events(request):
    has_image = (Q(image__isnull=False) & ~Q(image="")) | ~Q(image_url="")
    base = NewsEventsItem.objects.filter(is_published=True).filter(has_image)
    news_items = base.filter(section=NewsEventsItem.Section.NEWS_UPDATES)
    event_items = base.filter(section=NewsEventsItem.Section.EVENTS_HIGHLIGHTS)
    return render(
        request,
        "news_updates.html",
        {"news_items": news_items, "event_items": event_items},
    )


def properties_list(request):
    base = Property.objects.filter(is_published=True).select_related("city")
    q = (request.GET.get("q") or "").strip()
    status_filters = [s for s in request.GET.getlist("status") if s]
    city_slug = (request.GET.get("city") or "").strip()
    project_type = (request.GET.get("project_type") or "").strip()

    valid_types = {c[0] for c in Property.PROJECT_TYPE_CHOICES}

    qs = base
    if q:
        qs = qs.filter(
            Q(name__icontains=q)
            | Q(location__icontains=q)
            | Q(city__name__icontains=q)
            | Q(project_type__icontains=q)
            | Q(developer_name__icontains=q)
            | Q(rera_id__icontains=q)
            | Q(description__icontains=q)
            | Q(project_size__icontains=q)
            | Q(amenities__icontains=q)
        )
    if status_filters:
        qs = qs.filter(status__in=status_filters)
    if city_slug:
        qs = qs.filter(city__slug=city_slug)
    if project_type in valid_types:
        qs = qs.filter(project_type=project_type)

    properties = qs.order_by("sort_order", "name")

    cities_with_listings = City.objects.annotate(
        listing_count=Count("properties", filter=Q(properties__is_published=True))
    ).filter(listing_count__gt=0).order_by("sort_order", "name")

    has_active_filters = bool(
        q or status_filters or city_slug or (project_type in valid_types)
    )

    return render(
        request,
        "properties/list.html",
        {
            "properties": properties,
            "cities_with_listings": cities_with_listings,
            "status_choices": Property.STATUS_CHOICES,
            "project_type_choices": Property.PROJECT_TYPE_CHOICES,
            "active_statuses": status_filters,
            "active_city_slug": city_slug,
            "active_project_type": project_type if project_type in valid_types else "",
            "active_q": q,
            "has_active_filters": has_active_filters,
        },
    )


def property_detail(request, slug):
    prop = get_object_or_404(
        Property.objects.select_related("city"),
        slug=slug,
        is_published=True,
    )
    return render(
        request,
        "properties/detail.html",
        {"property": prop, "similar_properties": Property.get_similar(prop)},
    )


@require_POST
def submit_enquiry(request):
    form = SiteEnquiryForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"ok": True})
    errors = {}
    for field, errs in form.errors.items():
        errors[field] = errs[0] if errs else ""
    if form.non_field_errors():
        errors["_error"] = form.non_field_errors()[0]
    return JsonResponse({"ok": False, "errors": errors}, status=400)


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).select_related("author")


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = "post"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).select_related("author")
