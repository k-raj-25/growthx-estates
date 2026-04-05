from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("enquiries/submit/", views.submit_enquiry, name="submit_enquiry"),
    path("properties/", views.properties_list, name="properties_list"),
    path("properties/<slug:slug>/", views.property_detail, name="property_detail"),
    path("about/", views.about, name="about"),
    path("awards/", views.awards_recognitions, name="awards_recognitions"),
    path(
        "news-updates/",
        views.news_updates_events,
        name="news_updates",
    ),
    path("contact/", views.contact, name="contact"),
    path("support/", views.support, name="support"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms/", views.terms, name="terms"),
    path("sitemap/", views.site_sitemap, name="site_sitemap"),
    path("careers/", views.careers, name="careers"),
    path("blog/", views.BlogPostListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", views.BlogPostDetailView.as_view(), name="blog_detail"),
]
