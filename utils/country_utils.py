import pandas as pd
import pycountry
import re

# =====================================================
# 1. MANUAL COUNTRY ALIASES
# =====================================================

aliases = {

    # Australia
    "The Commonwealth of Australia (State) ": "Australia",

    # EU
    "the european union (international organization)": "European Union",
    "european union": "European Union",

    # Korea
    "republic of korea": "South Korea",

    # Turkey
    "republic of turkey": "Turkey",

    # Laos
    "lao people’s democratic republic": "Laos",

    # Kosovo
    "republic of kosovo": "Kosovo",
    "republic of kosovo and others": "Kosovo",

    # Ivory Coast
    "republic of côte d’ivoire": "Côte d'Ivoire",

    # North Macedonia
    "macedonia, former yugoslav republic of": "North Macedonia",

    # Trinidad
    "republic of trinidad & tobago": "Trinidad and Tobago",

    # Saint Kitts
    "federation of st. kitts and nevis": "Saint Kitts and Nevis",

    # Kyrgyzstan
    "kyrgyz republic": "Kyrgyzstan",

    # Gabon
    "gabonese republic": "Gabon",
}

# =====================================================
# 2. NON-COUNTRY KEYWORDS
# =====================================================

NON_COUNTRY_KEYWORDS = [
    "limited",
    "corporation",
    "company",
    "s.a.",
    "s.a.c.",
    "energy",
    "electric",
    "petroleum",
    "petroecuador",
    "camwater",
    "others"
]

# =====================================================
# 3. BUILD PYCOUNTRY LOOKUP
# =====================================================

country_lookup = {}

for country in pycountry.countries:

    country_lookup[country.name.lower()] = country.name

    if hasattr(country, "official_name"):
        country_lookup[country.official_name.lower()] = country.name

    if hasattr(country, "common_name"):
        country_lookup[country.common_name.lower()] = country.name

# =====================================================
# 4. HELPER FUNCTIONS
# =====================================================

def normalize_text(text):

    text = str(text).strip().lower()

    # normalize whitespace
    text = re.sub(r"\s+", " ", text)

    return text


def is_non_country(text):

    return any(
        keyword in text
        for keyword in NON_COUNTRY_KEYWORDS
    )

# =====================================================
# 5. MAIN EXTRACTION FUNCTION
# =====================================================

def extract_country(raw_value):

    if pd.isna(raw_value):
        return pd.Series([None, None, None])

    normalized = normalize_text(raw_value)

    # -------------------------------------------------
    # A. EXCLUDE NON-COUNTRIES
    # -------------------------------------------------

    if is_non_country(normalized):
        return pd.Series([None, None, "excluded"])

    # -------------------------------------------------
    # B. EXACT ALIAS MATCH
    # -------------------------------------------------

    if normalized in aliases:

        clean_country = aliases[normalized]

        country_obj = pycountry.countries.get(name=clean_country)

        iso3 = country_obj.alpha_3 if country_obj else None

        return pd.Series([
            clean_country,
            iso3,
            "alias"
        ])

    # -------------------------------------------------
    # C. EXACT PYCOUNTRY MATCH
    # -------------------------------------------------

    if normalized in country_lookup:

        clean_country = country_lookup[normalized]

        country_obj = pycountry.countries.get(name=clean_country)

        iso3 = country_obj.alpha_3 if country_obj else None

        return pd.Series([
            clean_country,
            iso3,
            "pycountry"
        ])

    # -------------------------------------------------
    # D. EMBEDDED COUNTRY MATCH
    # -------------------------------------------------

    for key, value in aliases.items():

        if key in normalized:

            country_obj = pycountry.countries.get(name=value)

            iso3 = country_obj.alpha_3 if country_obj else None

            return pd.Series([
                value,
                iso3,
                "embedded_alias"
            ])

    for key, value in country_lookup.items():

        if key in normalized:

            country_obj = pycountry.countries.get(name=value)

            iso3 = country_obj.alpha_3 if country_obj else None

            return pd.Series([
                value,
                iso3,
                "embedded_pycountry"
            ])

    # -------------------------------------------------
    # E. NO MATCH
    # -------------------------------------------------

    return pd.Series([
        None,
        None,
        "unmatched"
    ])