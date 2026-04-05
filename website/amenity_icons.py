"""Map free-text amenity labels to icon keys for templates."""

# First matching substring wins; keep more specific phrases before generic ones.
_AMENITY_RULES: tuple[tuple[str, str], ...] = (
    ("infinity pool", "pool"),
    ("sky pool", "pool"),
    ("heated pool", "pool"),
    ("sun deck", "terrace"),
    ("wine wall", "wine"),
    ("wine storage", "wine"),
    ("outdoor kitchen", "kitchen"),
    ("electric shuttle", "shuttle"),
    ("co-working", "cowork"),
    ("coworking", "cowork"),
    ("package locker", "parcel"),
    ("bike storage", "bike"),
    ("bike workshop", "bike"),
    ("guest suite", "guest"),
    ("on-site", "staff"),
    ("pet spa", "pet"),
    ("dog run", "pet"),
    ("smart security", "security"),
    ("landscape lighting", "garden"),
    ("pool", "pool"),
    ("deck", "terrace"),
    ("terrace", "terrace"),
    ("rooftop", "rooftop"),
    ("wine", "wine"),
    ("dining", "dining"),
    ("kitchen", "kitchen"),
    ("yoga", "yoga"),
    ("fitness", "fitness"),
    ("gym", "fitness"),
    ("parcel", "parcel"),
    ("package", "parcel"),
    ("locker", "parcel"),
    ("dock", "dock"),
    ("garage", "garage"),
    ("ev", "ev"),
    ("charging", "ev"),
    ("concierge", "concierge"),
    ("lounge", "lounge"),
    ("pet", "pet"),
    ("dog", "pet"),
    ("spa", "spa"),
    ("security", "security"),
    ("generator", "power"),
    ("backup", "power"),
    ("landscape", "garden"),
    ("bike", "bike"),
    ("bicycle", "bike"),
    ("guest", "guest"),
    ("superintendent", "staff"),
    ("shuttle", "shuttle"),
    ("storage", "storage"),
    ("amphitheater", "venue"),
    ("cowork", "cowork"),
    ("residents", "lounge"),
)


def amenity_icon_key(label: str) -> str:
    t = label.lower()
    for needle, key in _AMENITY_RULES:
        if needle in t:
            return key
    return "default"
