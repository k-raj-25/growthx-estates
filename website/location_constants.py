"""Initial city names seeded by migration ``0010_city``.

Add or edit cities in Django admin (Website → Cities). Link each property to a city
there; the public site only lists cities that have at least one published property.
"""

INDIAN_CITY_LOCATIONS = frozenset(
    {
        "Mumbai, Maharashtra",
        "Bengaluru, Karnataka",
        "Hyderabad, Telangana",
        "Pune, Maharashtra",
        "Chennai, Tamil Nadu",
        "Delhi, NCR",
        "Gurugram, Haryana",
        "Noida, Uttar Pradesh",
        "Kolkata, West Bengal",
        "Ahmedabad, Gujarat",
        "Jaipur, Rajasthan",
        "Surat, Gujarat",
        "Lucknow, Uttar Pradesh",
        "Kochi, Kerala",
        "Indore, Madhya Pradesh",
        "Chandigarh, Chandigarh",
        "Goa (Panaji)",
    }
)
