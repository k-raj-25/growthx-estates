from django import template

from ..amenity_icons import amenity_icon_key

register = template.Library()


@register.inclusion_tag("properties/partials/amenity_icon.html")
def amenity_icon(amenity_label):
    return {"icon": amenity_icon_key(amenity_label), "label": amenity_label}
