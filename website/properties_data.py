"""Initial property rows for migration 0009 (demo seed).

Live data is stored in ``website.Property`` and edited in Django admin.

Optional keys (used by migration ``0012``): ``city_name`` must match a row in
``location_constants.INDIAN_CITY_LOCATIONS``; ``project_type`` is one of
``residential``, ``commercial``, or ``sco``.
"""

_RAW_PROPERTIES = [
    {
        "slug": "skyline-residence",
        "name": "Skyline Residence",
        "location": "Hudson Yards, New York, NY",
        "price_display": "$1.25M — from",
        "rating": 4.9,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Skyline Residence pairs floor-to-ceiling glass with bespoke interiors and private elevator access. "
            "Residences feature wide-plank oak, chef kitchens with integrated appliances, and smart climate controls. "
            "The amenity stack includes a skyline pool deck, residents' lounge, and dedicated concierge—crafted for "
            "owners who want Midtown energy with a calm return home."
        ),
        "amenities": [
            "Sky pool & sun deck",
            "Private dining room",
            "Fitness studio + yoga",
            "Pet spa",
            "24/7 concierge",
            "EV charging",
            "Coworking suites",
            "Wine storage",
        ],
        "videos": [
            {"title": "Residence walkthrough", "embed_url": "https://www.youtube.com/embed/K_Krfwz41HU"},
            {"title": "Neighborhood spotlight", "embed_url": "https://www.youtube.com/embed/65swxlDZpPg"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3021.8605443960847!2d-73.99335892346696!3d"
            "40.75372357138981!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c258fafc6ebf91%3A0x7086e221a79e7605!2s"
            "Hudson%20Yards!5e0!3m2!1sen!2sus!4v1712345678901!5m2!1sen!2sus"
        ),
        "developer_name": "Apex Urban Partners",
        "about_developer": (
            "Apex Urban Partners has delivered over 6 million square feet of residential and mixed-use space across "
            "the Northeast over the last two decades. The studio is known for rigorous detailing, sustainable "
            "material choices, and long-term building performance."
        ),
        "faq": [
            {
                "q": "What is included in the base specification?",
                "a": "Premium appliances, wide-plank flooring, motorized shades in living areas, and smart thermostat "
                "are included. Upgrade palettes are available at the design center.",
            },
            {
                "q": "Are pets allowed?",
                "a": "Yes—two pets per residence with breed reasonable restrictions. A dedicated pet spa is on level 4.",
            },
            {
                "q": "Is parking available?",
                "a": "Deeded spaces can be purchased separately; EV-ready stalls are available in the garage.",
            },
        ],
        "rera_id": "P51900045231",
        "project_size": "2.1 acres · 1 tower · 180 residences",
        "images": [
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
        ],
    },
    {
        "slug": "azure-villa",
        "name": "Azure Villa",
        "location": "Coconut Grove, Miami, FL",
        "price_display": "$2.5M — from",
        "rating": 4.85,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Azure Villa is a low-rise coastal compound with expansive terraces, an infinity-edge pool, and mature "
            "landscaping for total privacy. Interiors emphasize lime plaster, teak, and natural stone with indirect "
            "lighting throughout. Perfect as a primary residence or a lock-and-leave second home minutes from the bay."
        ),
        "amenities": [
            "Heated infinity pool",
            "Outdoor kitchen",
            "Private dock access",
            "Smart security",
            "Temperature-controlled wine wall",
            "Generator backup",
            "Landscape lighting",
            "Two-car enclosed garage",
        ],
        "videos": [
            {"title": "Pool & terrace tour", "embed_url": "https://www.youtube.com/embed/HgzSlACMloI"},
            {"title": "Interior finishes", "embed_url": "https://www.youtube.com/embed/JvzZ9bqLYIY"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3594.7!2d-80.24!3d25.72!2m3!1f0!2f0!3f0!3m2!1i"
            "1024!2i768!4f13.1!3m3!1m2!1s0x88d9b7b8b8b8b8b9%3A0x1!2sCoconut%20Grove%2C%20Miami%2C%20FL!5e0!3m2!1sen!2sus"
        ),
        "developer_name": "Baylight Developments",
        "about_developer": (
            "Baylight Developments specializes in coastal Florida residences with a focus on resilience, native "
            "planting, and indoor–outdoor living. Their projects consistently exceed flood and wind-load standards "
            "while keeping architecture warm and human-scaled."
        ),
        "faq": [
            {
                "q": "What are annual carrying costs?",
                "a": "HOA covers landscaping, pool service, security monitoring, and shared infrastructure. "
                "Exact figures are in the disclosure package.",
            },
            {
                "q": "Can I lease the property short-term?",
                "a": "The community allows limited-term leases with board registration; many owners use a preferred "
                "management partner.",
            },
        ],
        "rera_id": "FL-RERA-AZV-7721",
        "project_size": "0.6 acres · 12 villas",
        "images": [
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
        ],
    },
    {
        "slug": "heritage-row",
        "name": "Heritage Row",
        "location": "Lincoln Park, Chicago, IL",
        "price_display": "$850K — from",
        "rating": 4.7,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Heritage Row reimagines the Chicago townhouse with brick-and-limestone facades, generous rear gardens, "
            "and flexible loft levels. Delivery is phased through 2027 with early design customization still available "
            "for a limited number of homes. Underground parking and private elevators are offered on select units."
        ),
        "amenities": [
            "Private terraces",
            "Rooftop option packages",
            "Parcel room",
            "Bike workshop",
            "Guest suite booking",
            "On-site superintendent",
        ],
        "videos": [
            {"title": "Construction progress", "embed_url": "https://www.youtube.com/embed/qqzYaWZ_8Js"},
            {"title": "Design philosophy", "embed_url": "https://www.youtube.com/embed/9p0jpiGT3Xs"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11880!2d-87.65!3d41.92!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x880fd33a8b9b8b9b%3A0x1!2sLincoln%20Park%2C%20Chicago%2C%20IL!5e0!3m2!1sen!2sus"
        ),
        "developer_name": "Northline Collective",
        "about_developer": (
            "Northline Collective is a Chicago-based builder-developer focused on infill neighborhoods. They "
            "prioritize craft masonry, durable envelopes, and energy-efficient mechanical systems on every project."
        ),
        "faq": [
            {
                "q": "When is the first occupancy date?",
                "a": "Phase A targets Q4 2026; Phase B follows mid-2027. Your purchase agreement includes a "
                "milestone schedule.",
            },
            {
                "q": "Can I combine units?",
                "a": "Select pairs can be joined during pre-construction; speak with sales for structural feasibility.",
            },
        ],
        "rera_id": "IL-2026-HR-0192",
        "project_size": "3.4 acres · 48 townhomes",
        "images": [
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1605146769289-440113cc3d00?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1605146769289-440113cc3d00?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
        ],
    },
    {
        "slug": "meridian-heights",
        "name": "Meridian Heights",
        "location": "East Austin, TX",
        "price_display": "$620K — from",
        "rating": 4.65,
        "status": "New launch",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Meridian Heights introduces mid-rise living with loft-style plans, collaborative workspaces, and a "
            "rooftop amphitheater facing the downtown skyline. Early buyers benefit from design allowances and "
            "assigned storage. The project targets LEED Silver certification."
        ),
        "amenities": [
            "Rooftop amphitheater",
            "Co-working pods",
            "Package lockers",
            "Bike storage",
            "Dog run",
            "Electric shuttle to downtown",
        ],
        "videos": [
            {"title": "Project reveal", "embed_url": "https://www.youtube.com/embed/ysz5S6PUM-U"},
            {"title": "Lifestyle edit", "embed_url": "https://www.youtube.com/embed/FV3nOGmXyqc"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3445!2d-97.71!3d30.28!2m3!1f0!2f0!3f0!3m2!1i1024!2i768"
            "!4f13.1!3m3!1m2!1s0x8644b5b5b5b5b5b5%3A0x1!2sEast%20Austin%2C%20Austin%2C%20TX!5e0!3m2!1sen!2sus"
        ),
        "developer_name": "Plateau Studio",
        "about_developer": (
            "Plateau Studio is an Austin firm merging hospitality design with residential buildings. Their work "
            "emphasizes community programming, shade and breeze in shared courts, and authentic local partnerships."
        ),
        "faq": [
            {
                "q": "What reservation amount is required?",
                "a": "A refundable reservation fee holds your plan type until contract; terms are outlined in the "
                "registration kit.",
            },
        ],
        "rera_id": "TX-RERA-MH-4402",
        "project_size": "1.8 acres · 2 buildings · 210 units",
        "images": [
            "https://images.unsplash.com/photo-1486304873000-235643847519?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
        ],
    },
    {
        "slug": "crest-mumbai",
        "name": "The Crest Mumbai",
        "city_name": "Mumbai, Maharashtra",
        "project_type": "residential",
        "location": "Worli Sea Face, Mumbai",
        "price_display": "₹4.2 Cr — from",
        "rating": 4.82,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "The Crest Mumbai is a sea-facing tower with corner living rooms, private decks, and understated luxury "
            "finishes. Residents enjoy a skyline lap pool, salon-style spa, and double-height lobby with curated art. "
            "Routes to BKC and the airport are quick, while Worli keeps dining and retail within a short drive."
        ),
        "amenities": [
            "Sky pool & spa",
            "Executive lounge",
            "Indoor golf simulator",
            "Children's play lab",
            "EV-ready parking",
            "Private dining salon",
            "Business centre",
        ],
        "videos": [
            {"title": "Residence tour", "embed_url": "https://www.youtube.com/embed/K_Krfwz41HU"},
            {"title": "Neighbourhood", "embed_url": "https://www.youtube.com/embed/65swxlDZpPg"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3773.5!2d72.81!3d19.01!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sWorli%2C%20Mumbai!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Lantern Bay Developers",
        "about_developer": (
            "Lantern Bay Developers focuses on coastal towers in Mumbai and Goa with strong structural cores, "
            "high-performance glazing, and calm, light-filled interiors."
        ),
        "faq": [
            {
                "q": "Is stamp duty extra?",
                "a": "Yes—stamp duty and registration are payable as per state norms; the sales team shares a sample "
                "cost sheet at booking.",
            },
            {
                "q": "Are modifications allowed?",
                "a": "Limited interior packages can be selected before slab milestones; structural changes are not "
                "permitted.",
            },
        ],
        "rera_id": "P51800077142",
        "project_size": "2.4 acres · 1 tower · 220 residences",
        "images": [
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
        ],
    },
    {
        "slug": "lotus-gardenia",
        "name": "Lotus Gardenia",
        "city_name": "Bengaluru, Karnataka",
        "project_type": "residential",
        "location": "Sarjapur Road, Bengaluru",
        "price_display": "₹1.1 Cr — from",
        "rating": 4.58,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Lotus Gardenia offers wide balconies, cross-ventilated plans, and a central landscaped courtyard that "
            "stays usable year-round. Coworking corners and a junior olympic pool appeal to young families; delivery "
            "is phased with clear milestone tracking."
        ),
        "amenities": [
            "Courtyard gardens",
            "Co-working lounge",
            "50m swimming pool",
            "Indoor sports court",
            "Walking track",
            "Senior citizen zone",
            "Rainwater harvesting",
        ],
        "videos": [
            {"title": "Project walkthrough", "embed_url": "https://www.youtube.com/embed/HgzSlACMloI"},
            {"title": "Floor plans", "embed_url": "https://www.youtube.com/embed/JvzZ9bqLYIY"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.9!2d77.67!3d12.91!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sSarjapur%20Road%2C%20Bengaluru!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Canopy Build Pvt Ltd",
        "about_developer": (
            "Canopy Build delivers mid-rise communities across Bengaluru with emphasis on light, ventilation, and "
            "low-maintenance landscapes."
        ),
        "faq": [
            {
                "q": "Expected possession?",
                "a": "Tower A targets Q2 2027; Tower B follows in early 2028 subject to monsoon windows.",
            },
        ],
        "rera_id": "PRM/KA/RERA/1251/308/PR-080426",
        "project_size": "6.8 acres · 4 towers · 640 units",
        "images": [
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1605146769289-440113cc3d00?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
        ],
    },
    {
        "slug": "cyber-pearl-plaza",
        "name": "Cyber Pearl Plaza",
        "city_name": "Hyderabad, Telangana",
        "project_type": "commercial",
        "location": "HITEC City, Hyderabad",
        "price_display": "₹8,200 / sq ft — from",
        "rating": 4.71,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Cyber Pearl Plaza is a Grade-A office asset with efficient floor plates, LEED-oriented MEP, and curated "
            "ground-floor F&B. Ideal for GCCs and scaled product teams needing 24/7 operations support and redundant "
            "power paths."
        ),
        "amenities": [
            "Double-height lobby",
            "Food court & café pavilions",
            "100% backup power",
            "High-speed lifts",
            "Visitor management",
            "End-of-trip facilities",
            "Sky bridge to transit",
        ],
        "videos": [
            {"title": "Building tour", "embed_url": "https://www.youtube.com/embed/qqzYaWZ_8Js"},
            {"title": "Location context", "embed_url": "https://www.youtube.com/embed/9p0jpiGT3Xs"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3806.2!2d78.37!3d17.45!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sHITEC%20City%2C%20Hyderabad!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Gridline Commercial",
        "about_developer": (
            "Gridline Commercial develops office and retail blocks in Hyderabad and Chennai with experience leasing "
            "to technology and BFSI tenants."
        ),
        "faq": [
            {
                "q": "Typical floor size?",
                "a": "Standard floors are ~42,000 sq ft carpet-efficient; subdivisions possible for 12,000+ sq ft blocks.",
            },
        ],
        "rera_id": "P02400008881",
        "project_size": "1.9 acres · 22 floors · ~9.8L sq ft leasable",
        "images": [
            "https://images.unsplash.com/photo-1486304873000-235643847519?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
            "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=1200&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
            "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&q=80",
        ],
    },
    {
        "slug": "aundh-prime",
        "name": "Aundh Prime",
        "city_name": "Pune, Maharashtra",
        "project_type": "residential",
        "location": "Aundh, Pune",
        "price_display": "₹95 L — from",
        "rating": 4.55,
        "status": "New launch",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Aundh Prime stacks efficient two- and three-bedroom plans above a vibrant high street podium. Early "
            "registrations include wardrobe and kitchen appliance credits, with flexible payment plans for "
            "first-time buyers."
        ),
        "amenities": [
            "Sky jogging track",
            "Multipurpose hall",
            "Toddler splash pool",
            "Grocery & pharmacy frontage",
            "Parcel lockers",
            "Amphitheatre lawn",
        ],
        "videos": [
            {"title": "Launch film", "embed_url": "https://www.youtube.com/embed/ysz5S6PUM-U"},
            {"title": "Amenities teaser", "embed_url": "https://www.youtube.com/embed/FV3nOGmXyqc"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.1!2d73.80!3d18.55!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sAundh%2C%20Pune!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Sahyadri Foundations",
        "about_developer": (
            "Sahyadri Foundations has delivered affordable-premium housing in Pune and Nashik with a reputation for "
            "transparent documentation."
        ),
        "faq": [
            {
                "q": "Booking amount?",
                "a": "A nominal booking with bank SUB registration locks the unit; balance follows the construction "
                "linked plan.",
            },
        ],
        "rera_id": "P52100077199",
        "project_size": "3.1 acres · 2 towers · 410 units",
        "images": [
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
        ],
    },
    {
        "slug": "marina-bay-towers",
        "name": "Marina Bay Towers",
        "city_name": "Chennai, Tamil Nadu",
        "project_type": "residential",
        "location": "OMR, Chennai",
        "price_display": "₹78 L — from",
        "rating": 4.63,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Marina Bay Towers fronts a calming water court with breeze stacks for Chennai's climate. Apartments have "
            "treated fresh air in common corridors, heat-reflective roofs, and shaded play zones for children."
        ),
        "amenities": [
            "Lagoon pool",
            "Indoor games",
            "Meditation deck",
            "Crèche room",
            "Organic waste composter",
            "CCTV perimeter",
        ],
        "videos": [
            {"title": "Walkthrough", "embed_url": "https://www.youtube.com/embed/K_Krfwz41HU"},
            {"title": "Developer interview", "embed_url": "https://www.youtube.com/embed/65swxlDZpPg"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3890.3!2d80.23!3d12.95!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sOld%20Mahabalipuram%20Road%2C%20Chennai!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Coromandel Living",
        "about_developer": (
            "Coromandel Living specialises in coastal-climate residences across Chennai and Puducherry with durable "
            "finishes and thoughtful services."
        ),
        "faq": [
            {
                "q": "How far to airport?",
                "a": "Chennai International Airport is typically 45–65 minutes depending on traffic via the express "
                "corridor.",
            },
        ],
        "rera_id": "TN/01/Building/0323/2026",
        "project_size": "4.4 acres · 3 towers · 520 units",
        "images": [
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
        ],
    },
    {
        "slug": "connaught-trade-arc",
        "name": "Connaught Trade Arc",
        "city_name": "Delhi, NCR",
        "project_type": "commercial",
        "location": "Connaught Place, New Delhi",
        "price_display": "₹14,500 / sq ft — from",
        "rating": 4.74,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Connaught Trade Arc revives a heritage ring with restored colonnades, boutique office floors, and a "
            "secured retail galleria. Floor-to-ceiling restoration meets modern fire and accessibility upgrades for "
            "long-term institutional tenants."
        ),
        "amenities": [
            "Heritage concierge",
            "Valet & loading bays",
            "Tenant storage vaults",
            "Rooftop meeting terraces",
            "Dedicated fibre meet-me room",
            "Retail F&B courtyard",
        ],
        "videos": [
            {"title": "Arcade tour", "embed_url": "https://www.youtube.com/embed/HgzSlACMloI"},
            {"title": "Delhi context", "embed_url": "https://www.youtube.com/embed/JvzZ9bqLYIY"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3501.2!2d77.21!3d28.63!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sConnaught%20Place%2C%20New%20Delhi!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Imperial Restorations LLP",
        "about_developer": (
            "Imperial Restorations LLP leads adaptive reuse in central Delhi with conservation consultants on every "
            "project."
        ),
        "faq": [
            {
                "q": "Lease or strata ownership?",
                "a": "Commercial floors are available on long-leasehold basis; terms vary by stack—request the "
                "offering memorandum.",
            },
        ],
        "rera_id": "DLRERA2026CTA0144",
        "project_size": "0.45 acres · mixed-use podium + 9 office levels",
        "images": [
            "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
            "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=1200&q=80",
            "https://images.unsplash.com/photo-1486304873000-235643847519?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
        ],
    },
    {
        "slug": "sector-79-boulevard",
        "name": "Sector 79 Boulevard",
        "city_name": "Gurugram, Haryana",
        "project_type": "sco",
        "location": "Sector 79, Gurugram",
        "price_display": "₹3.8 Cr — from",
        "rating": 4.61,
        "status": "New launch",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Sector 79 Boulevard brings double-height showrooms with office cores above—ideal for clinics, premium "
            "retail, and studio suites. Wide frontages and service cores keep daily operations smooth for owners "
            "and visitors."
        ),
        "amenities": [
            "Frontage boulevard",
            "Ample surface + basement parking",
            "Fire tender access",
            "Dual power feeders",
            "Signage alcoves",
            "Landscaped central spine",
        ],
        "videos": [
            {"title": "Masterplan", "embed_url": "https://www.youtube.com/embed/qqzYaWZ_8Js"},
            {"title": "Product film", "embed_url": "https://www.youtube.com/embed/9p0jpiGT3Xs"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3510.4!2d77.04!3d28.37!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sSector%2079%2C%20Gurugram!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Arcadia Frontage",
        "about_developer": (
            "Arcadia Frontage develops SCO and high-street assets along the Southern Peripheral Road corridor."
        ),
        "faq": [
            {
                "q": "Can I combine two plots?",
                "a": "Structural combining is evaluated case-by-case during shell stage; speak with the sales architect.",
            },
        ],
        "rera_id": "HRERA/PKL/AGC/890/2026/12",
        "project_size": "2.7 acres · 44 SCO units",
        "images": [
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1605146769289-440113cc3d00?w=1200&q=80",
        ],
    },
    {
        "slug": "express-noida-one",
        "name": "Express Noida One",
        "city_name": "Noida, Uttar Pradesh",
        "project_type": "residential",
        "location": "Sector 108, Noida",
        "price_display": "₹1.55 Cr — from",
        "rating": 4.59,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Express Noida One lines the expressway with noise-mitigating façades, extra-wide decks, and a clubhouse "
            "program inspired by resort layering. Towers step to protect views while keeping community courts sunlit."
        ),
        "amenities": [
            "Clubhouse with café",
            "Temperature-controlled pool",
            "Squash & badminton",
            "Guest suites",
            "Paved riverfront promenade access",
            "Shuttle to metro hub",
        ],
        "videos": [
            {"title": "Drone flyover", "embed_url": "https://www.youtube.com/embed/ysz5S6PUM-U"},
            {"title": "Interiors mood", "embed_url": "https://www.youtube.com/embed/FV3nOGmXyqc"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3507.8!2d77.38!3d28.57!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sSector%20108%2C%20Noida!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Yeida Skyline",
        "about_developer": (
            "Yeida Skyline builds premium housing along the Noida–Greater Noida corridor with IFC-aligned planning."
        ),
        "faq": [
            {
                "q": "Metro connectivity?",
                "a": "The nearest approved station is within a 12-minute shuttle; timelines follow NCRTC announcements.",
            },
        ],
        "rera_id": "UPRERAPRJ269988",
        "project_size": "5.5 acres · 5 towers · 980 units",
        "images": [
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
        ],
    },
    {
        "slug": "victoria-riverfront",
        "name": "Victoria Riverfront",
        "city_name": "Kolkata, West Bengal",
        "project_type": "residential",
        "location": "Action Area II, New Town",
        "price_display": "₹68 L — from",
        "rating": 4.52,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Victoria Riverfront opens to landscaped ghats with evening lighting, breeze-friendly towers, and Kolkata "
            "classical motifs translated into contemporary public art. Sizes range from efficient compact homes to "
            "corner sky residences."
        ),
        "amenities": [
            "Ghatside promenade",
            "Community library",
            "Open-air theatre",
            "Indoor heated pool",
            "Multi-faith quiet room",
        ],
        "videos": [
            {"title": "Site film", "embed_url": "https://www.youtube.com/embed/K_Krfwz41HU"},
            {"title": "Lifestyle cut", "embed_url": "https://www.youtube.com/embed/65swxlDZpPg"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3684.5!2d88.48!3d22.58!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sNew%20Town%2C%20Kolkata!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Hooghly Vista Homes",
        "about_developer": (
            "Hooghly Vista Homes delivers wetland-sensitive layouts in East Kolkata with elevated podiums and native "
            "planting."
        ),
        "faq": [
            {
                "q": "Flood preparedness?",
                "a": "Podium parking sits above design high-flood levels; pumps and grading are detailed in the "
                "disclosure addendum.",
            },
        ],
        "rera_id": "WBRERA/P/KOL/2026/000441",
        "project_size": "7.1 acres · 6 towers · 1,120 units",
        "images": [
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
        ],
    },
    {
        "slug": "sabarmati-heights",
        "name": "Sabarmati Heights",
        "city_name": "Ahmedabad, Gujarat",
        "project_type": "residential",
        "location": "SG Highway, Ahmedabad",
        "price_display": "₹82 L — from",
        "rating": 4.67,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Sabarmati Heights frames sunset views toward the river with vertical gardens, stack parking optimisers, "
            "and Jain-friendly kitchen options on plan. Cooling terraces and mist-cooled play areas handle Gujarat "
            "summers comfortably."
        ),
        "amenities": [
            "Sky meditation garden",
            "Stack parking systems",
            "Desert plant courtyard",
            "Indoor cricket nets",
            "Terrace pickleball",
        ],
        "videos": [
            {"title": "Construction update", "embed_url": "https://www.youtube.com/embed/qqzYaWZ_8Js"},
            {"title": "Architect speaks", "embed_url": "https://www.youtube.com/embed/9p0jpiGT3Xs"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3710.6!2d72.51!3d23.03!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sSG%20Highway%2C%20Ahmedabad!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Sabarmati Collective",
        "about_developer": (
            "Sabarmati Collective is an Ahmedabad team known for river-corridor towers with resilient envelopes."
        ),
        "faq": [
            {
                "q": "Solar readiness?",
                "a": "Roofs include conduit stubs for owner-led solar; common area solar is evaluated in phase two.",
            },
        ],
        "rera_id": "PR/GJ/AHMEDABAD/AHMEDABAD/CAA08709/250322",
        "project_size": "4.9 acres · 3 towers · 670 units",
        "images": [
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1605146769289-440113cc3d00?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
        ],
    },
    {
        "slug": "pink-city-arcade",
        "name": "Pink City Arcade",
        "city_name": "Jaipur, Rajasthan",
        "project_type": "sco",
        "location": "Tonk Road, Jaipur",
        "price_display": "₹2.9 Cr — from",
        "rating": 4.49,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Pink City Arcade layers retail vaults with studio offices above—patterned jaali screens shade walkways "
            "while keeping classic Jaipur pink sandstone accents. Ideal for jewellery houses, design ateliers, and "
            "specialty F&B."
        ),
        "amenities": [
            "Arcaded walkways",
            "Heritage façade lighting",
            "Service lifts to upper floors",
            "Basement inventory bays",
            "Central plaza events",
        ],
        "videos": [
            {"title": "Walkthrough", "embed_url": "https://www.youtube.com/embed/HgzSlACMloI"},
            {"title": "Retail story", "embed_url": "https://www.youtube.com/embed/JvzZ9bqLYIY"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3557.1!2d75.79!3d26.84!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sTonk%20Road%2C%20Jaipur!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Desert Front Retail",
        "about_developer": (
            "Desert Front Retail blends Rajasthan craft languages with resilient modern retail shells across Jaipur "
            "and Udaipur."
        ),
        "faq": [
            {
                "q": "Signage guidelines?",
                "a": "Heritage committee–approved templates keep a unified street experience while allowing brand "
                "flexibility at eye level.",
            },
        ],
        "rera_id": "RAJ/P/2026/1392",
        "project_size": "1.6 acres · 36 SCO bays",
        "images": [
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80",
        ],
    },
    {
        "slug": "textile-hub-one",
        "name": "Textile Hub One",
        "city_name": "Surat, Gujarat",
        "project_type": "commercial",
        "location": "Ring Road, Surat",
        "price_display": "₹6,400 / sq ft — from",
        "rating": 4.56,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Textile Hub One consolidates trading floors, sample showrooms, and back-office blocks with heavy floor "
            "load allowances for looms and inventory. Truck movement is separated from visitor drop-offs for safer "
            "operations."
        ),
        "amenities": [
            "High bay loading",
            "Fire-rated warehousing sleeves",
            "Goods lifts (4T capacity)",
            "Trading floor mezzanines",
            "Canteen commons",
        ],
        "videos": [
            {"title": "Logistics overview", "embed_url": "https://www.youtube.com/embed/ysz5S6PUM-U"},
            {"title": "Building shell", "embed_url": "https://www.youtube.com/embed/FV3nOGmXyqc"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3724.9!2d72.80!3d21.17!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sRing%20Road%2C%20Surat!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Tapi Industrial Estates",
        "about_developer": (
            "Tapi Industrial Estates partners with textile and diamond trade associations on-fit industrial shells "
            "in Gujarat."
        ),
        "faq": [
            {
                "q": "Floor loading specs?",
                "a": "Trading floors are designed for 5–7.5 kN/m² live loads; heavier zones can be reinforced on "
                "request during shell sale.",
            },
        ],
        "rera_id": "GJRERA/SRT/COMM/0336/0426",
        "project_size": "3.3 acres · 2 buildings · 11 floors each",
        "images": [
            "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
            "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=1200&q=80",
            "https://images.unsplash.com/photo-1486304873000-235643847519?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
        ],
    },
    {
        "slug": "gomti-terraces",
        "name": "Gomti Terraces",
        "city_name": "Lucknow, Uttar Pradesh",
        "project_type": "residential",
        "location": "Gomti Nagar Extension",
        "price_display": "₹1.25 Cr — from",
        "rating": 4.64,
        "status": "New launch",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Gomti Terraces steps back from the waterfront with terraced sky gardens, louvered sun-breaks, and "
            "spacious kitchens suited to Awadhi family cooking. Evening lighting along the Gomti edge creates a soft "
            "backdrop for community gatherings."
        ),
        "amenities": [
            "Riverside lawns",
            "Banquet with pre-function lawn",
            "Skating ribbon",
            "Library & study pods",
            "Ayurvedic spa",
        ],
        "videos": [
            {"title": "Reveal film", "embed_url": "https://www.youtube.com/embed/K_Krfwz41HU"},
            {"title": "Masterplan", "embed_url": "https://www.youtube.com/embed/65swxlDZpPg"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.6!2d81.00!3d26.87!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sGomti%20Nagar%20Extension%2C%20Lucknow!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Nawabi Sky Gardens",
        "about_developer": (
            "Nawabi Sky Gardens crafts river-adjacent housing in Lucknow with Chikankari-inspired interior palettes "
            "optional at fit-out."
        ),
        "faq": [
            {
                "q": "View corridors protected?",
                "a": "Stepped massing is submitted to NOIDA/Lucknow development bylaws; view studies are in the "
                "brochure addendum.",
            },
        ],
        "rera_id": "UPRERAPRJ451102",
        "project_size": "5.9 acres · 4 towers · 720 units",
        "images": [
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
        ],
    },
    {
        "slug": "vembanad-shores",
        "name": "Vembanad Shores",
        "city_name": "Kochi, Kerala",
        "project_type": "residential",
        "location": "Marine Drive, Kochi",
        "price_display": "₹1.95 Cr — from",
        "rating": 4.78,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Vembanad Shores captures backwater breezes with deep verandahs, teak-trim details, and salt-safe "
            "hardware. Shared canoe storage and a waterfront reading room celebrate Kochi's relationship with the "
            "lagoon."
        ),
        "amenities": [
            "Infinity horizon pool",
            "Kayak & canoe storage",
            "Ayurvedic therapy rooms",
            "Chefs' demo kitchen",
            "Guest apartments",
        ],
        "videos": [
            {"title": "Waterfront tour", "embed_url": "https://www.youtube.com/embed/HgzSlACMloI"},
            {"title": "Monsoon resilience", "embed_url": "https://www.youtube.com/embed/JvzZ9bqLYIY"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3928.6!2d76.28!3d9.97!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sMarine%20Drive%2C%20Kochi!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Backwater Atelier",
        "about_developer": (
            "Backwater Atelier delivers boutique waterfront housing in Kerala with climate-first envelopes and "
            "hand-worked timber joinery partnerships."
        ),
        "faq": [
            {
                "q": "Corrosion protection?",
                "a": "Marine-grade coatings, SS316 fasteners in exposed zones, and sacrificial anodes in pools are "
                "specified in the structural brief.",
            },
        ],
        "rera_id": "K-RERA/PRJ/KOC/078/2024",
        "project_size": "3.0 acres · 2 mid-rises · 190 residences",
        "images": [
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
        ],
    },
    {
        "slug": "sarafa-mixed-use",
        "name": "Sarafa Mixed Use",
        "city_name": "Indore, Madhya Pradesh",
        "project_type": "sco",
        "location": "Vijay Nagar, Indore",
        "price_display": "₹2.1 Cr — from",
        "rating": 4.53,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Sarafa Mixed Use pairs night-market-inspired lighting with daytime retail efficiency—double-height "
            "food-grade bays sit beneath efficient studio offices. Streets are sized for festival crowds yet keep "
            "fire lanes clear."
        ),
        "amenities": [
            "Night-market lighting toolkit",
            "Food court grease traps centralised",
            "Rooftop brand terraces",
            "EV charging for visitors",
            "Service corridors separated",
        ],
        "videos": [
            {"title": "Street animation", "embed_url": "https://www.youtube.com/embed/qqzYaWZ_8Js"},
            {"title": "Retail plan", "embed_url": "https://www.youtube.com/embed/9p0jpiGT3Xs"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3681.8!2d75.89!3d22.75!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sVijay%20Nagar%2C%20Indore!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Malwa Street Labs",
        "about_developer": (
            "Malwa Street Labs programmes mixed streets in Indore and Bhopal with safety-first crowd engineering "
            "and modern F&B infrastructure."
        ),
        "faq": [
            {
                "q": "Odour management?",
                "a": "Centralised exhaust risers and rooftop scrubbers are sized for dense F&B—details in MEP schedules.",
            },
        ],
        "rera_id": "P-IND-22-2026-0089",
        "project_size": "1.2 acres · 28 SCO + 2 anchor bays",
        "images": [
            "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=1200&q=80",
            "https://images.unsplash.com/photo-1605146769289-440113cc3d00?w=1200&q=80",
        ],
    },
    {
        "slug": "capitol-lakeview",
        "name": "Capitol Lakeview",
        "city_name": "Chandigarh, Chandigarh",
        "project_type": "residential",
        "location": "Sector 48, Chandigarh",
        "price_display": "₹1.72 Cr — from",
        "rating": 4.81,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Capitol Lakeview honours Corbusier legibility with crisp brise-soleil, shaded courts, and apartments "
            "that open toward Sukhna views. Brick-inlay motifs nod to Punjab craft without over-ornamenting modern "
            "lines."
        ),
        "amenities": [
            "Lake-view infinity deck",
            "Temperature-controlled squash",
            "Amphitheatre berm",
            "Cycling workshop",
            "Organic terrace farm",
        ],
        "videos": [
            {"title": "City edit", "embed_url": "https://www.youtube.com/embed/ysz5S6PUM-U"},
            {"title": "Residence gallery", "embed_url": "https://www.youtube.com/embed/FV3nOGmXyqc"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3429.4!2d76.74!3d30.72!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sSector%2048%2C%20Chandigarh!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Grid Garden Chandigarh",
        "about_developer": (
            "Grid Garden Chandigarh focuses on lake-adjacent residential towers with climate moderating courts and "
            "low-VOC interiors."
        ),
        "faq": [
            {
                "q": "Heritage view angles?",
                "a": "Height envelopes follow MC zoning maps; view studies from typical floors are in the sales gallery.",
            },
        ],
        "rera_id": "PBRERA-CHD-CHO-2206",
        "project_size": "3.8 acres · 3 towers · 420 units",
        "images": [
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
        ],
    },
    {
        "slug": "palolem-coast-homes",
        "name": "Palolem Coast Homes",
        "city_name": "Goa (Panaji)",
        "project_type": "residential",
        "location": "Canacona, South Goa",
        "price_display": "₹2.35 Cr — from",
        "rating": 4.86,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Palolem Coast Homes offers low-density villas and flats minutes from Palolem with cross-ventilated plans, "
            "outdoor showers, and roofs ready for solar thermal. On-site concierge curates monsoon-safe housekeeping."
        ),
        "amenities": [
            "Residents' beach shuttle",
            "Open-air yoga shala",
            "Infinity plunge pool",
            "Work-from-garden pods",
            "Bicycle library",
        ],
        "videos": [
            {"title": "Coastal tour", "embed_url": "https://www.youtube.com/embed/K_Krfwz41HU"},
            {"title": "Monsoon care", "embed_url": "https://www.youtube.com/embed/65swxlDZpPg"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.2!2d74.03!3d15.01!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sPalolem%20Beach%2C%20Goa!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Monsoon Shore Collective",
        "about_developer": (
            "Monsoon Shore Collective engineers coastal housing in Goa with elevated plinths, native landscape, and "
            "low-light ecology lighting."
        ),
        "faq": [
            {
                "q": "Short-term rental policy?",
                "a": "Managed leasing is encouraged through the in-house operator; blackout dates apply during peak "
                "festivals per HOA guidelines.",
            },
        ],
        "rera_id": "GOARERA-AGC17-6789",
        "project_size": "8.5 acres · 86 villas + 120 apartments",
        "images": [
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
        ],
    },
    {
        "slug": "manyata-tech-bay",
        "name": "Manyata Tech Bay",
        "city_name": "Bengaluru, Karnataka",
        "project_type": "commercial",
        "location": "Manyata Tech Park, Bengaluru",
        "price_display": "₹9,100 / sq ft — from",
        "rating": 4.69,
        "status": "Ready to move",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Manyata Tech Bay adds a side-core office slab with operable windows on alternate bays, generous "
            "ceilings, and acoustic isolation for trading floors. The campus loop shuttle plugs into existing Tech "
            "Park routes."
        ),
        "amenities": [
            "Side-core efficient floorplates",
            "Trading floor acoustic pods",
            "Café pavilion",
            "Mother's room on every alternate floor",
            "LEED Gold targeting",
        ],
        "videos": [
            {"title": "Campus connectivity", "embed_url": "https://www.youtube.com/embed/HgzSlACMloI"},
            {"title": "Interior standards", "embed_url": "https://www.youtube.com/embed/JvzZ9bqLYIY"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.5!2d77.62!3d13.05!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sManyata%20Embassy%20Tech%20Park%2C%20Bengaluru!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Embassy Next Offices",
        "about_developer": (
            "Embassy Next Offices extends flagship business park product to mid-size enterprises seeking predictable "
            "OpEx."
        ),
        "faq": [
            {
                "q": "Fit-out period?",
                "a": "Standard landlord contribution includes base HVAC; tenant fit-out timelines average 120–150 days.",
            },
        ],
        "rera_id": "PRM/KA/RERA/1251/446/PR-090526",
        "project_size": "1.4 acres · 18 floors · 6.2L sq ft",
        "images": [
            "https://images.unsplash.com/photo-1486304873000-235643847519?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
            "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=1200&q=80",
            "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
            "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1200&q=80",
        ],
    },
    {
        "slug": "hitec-skyline",
        "name": "HITEC Skyline",
        "city_name": "Hyderabad, Telangana",
        "project_type": "residential",
        "location": "Madhapur, Hyderabad",
        "price_display": "₹1.38 Cr — from",
        "rating": 4.6,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "HITEC Skyline targets young professionals with compact luxury—sound-insulated bedrooms, WFH alcoves, and "
            "a rooftop pickleball deck minutes from IT corridors. Cooling towers are screened for quieter nights."
        ),
        "amenities": [
            "Screened MEP yards",
            "Pickleball + padel deck",
            "Micro-theatre",
            "Laundry lounge",
            "Night courier desk",
        ],
        "videos": [
            {"title": "Walkthrough", "embed_url": "https://www.youtube.com/embed/qqzYaWZ_8Js"},
            {"title": "Skyline timelapse", "embed_url": "https://www.youtube.com/embed/9p0jpiGT3Xs"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3807.2!2d78.39!3d17.44!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sMadhapur%2C%20Hyderabad!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Deccan Loftworks",
        "about_developer": (
            "Deccan Loftworks specialises in efficient towers for Hyderabad's tech workforce with acoustic-first "
            "specifications."
        ),
        "faq": [
            {
                "q": "Noise mitigation?",
                "a": "Acoustic glazing specs exceed baseline STC; sample mock-up available at experience centre.",
            },
        ],
        "rera_id": "P02400010233",
        "project_size": "2.2 acres · 2 towers · 540 units",
        "images": [
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=1200&q=80",
            "https://images.unsplash.com/photo-1600210492493-0946911123ea?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509358-9dc75507daeb?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
        ],
    },
    {
        "slug": "worli-edge",
        "name": "Worli Edge",
        "city_name": "Mumbai, Maharashtra",
        "project_type": "residential",
        "location": "Worli, Mumbai",
        "price_display": "₹5.6 Cr — from",
        "rating": 4.88,
        "status": "Under construction",
        "brochure_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "description": (
            "Worli Edge rises as a sculptural glass stack with private sky cabanas, double-height living options, and "
            "a collector's garage showcase level. The lobby functions as a quiet gallery rotating Mumbai artists "
            "each season."
        ),
        "amenities": [
            "Sky cabanas",
            "Art lobby programme",
            "Collector parking gallery",
            "Spa & longevity clinic",
            "Helipad readiness (subject approvals)",
        ],
        "videos": [
            {"title": "Teaser film", "embed_url": "https://www.youtube.com/embed/ysz5S6PUM-U"},
            {"title": "Sky deck preview", "embed_url": "https://www.youtube.com/embed/FV3nOGmXyqc"},
        ],
        "map_embed_url": (
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3773.8!2d72.82!3d19.00!2m3!1f0!2f0!3f0!3m2!1i1024"
            "!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sWorli%2C%20Mumbai!5e0!3m2!1sen!2sin"
        ),
        "developer_name": "Lantern Bay Developers",
        "about_developer": (
            "Lantern Bay Developers focuses on coastal towers in Mumbai and Goa with strong structural cores, "
            "high-performance glazing, and calm, light-filled interiors."
        ),
        "faq": [
            {
                "q": "Sea-facing inventory?",
                "a": "Upper mid-tier stacks capture primary sea views; lower tiers emphasise framed city perspectives—"
                "request sightline drawings.",
            },
        ],
        "rera_id": "P51900088901",
        "project_size": "1.9 acres · 1 tower · 96 residences",
        "images": [
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=80",
            "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80",
            "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
        ],
    },
]
