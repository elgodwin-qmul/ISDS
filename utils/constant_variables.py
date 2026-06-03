# Manually looked up countries related to the individual cases in the original ICSID dataset
ICSID_MANUAL_COUNTRY_CLEANUP = {
    "ARB/24/39": "Bangladesh",
    "ARB/22/4": "Bangladesh",
    "ARB/19/18": "Bangladesh",
    'ARB/10/11': "Bangladesh",
    "ARB/10/18": "Bangladesh",
    "ARB/92/2": "Bangladesh",
    "CONC/19/1": "Cameroon",
    "ARB/25/12": "Ecuador",
    "ARB/05/12": "Ecuador",
    "ARB/01/10": "Ecuador",
    "ARB/08/10": "Ecuador",
    "ARB/06/21": "Ecuador",
    "ARB/76/1": "France",
    "ARB/07/3": "Indonesia",
    "ARB/20/50": "Kosovo",
    "ARB/22/19": "Peru",
    "ARB/26/5": "Peru",
    "ARB/12/28": "Peru",
    "ARB/13/24": "Peru",
    "ARB/25/43": "Tanzania",
    "ARB/25/44": "Tanzania",
    "ARB/10/20": "Tanzania",
    "ARB/98/8": "Tanzania",
    "ARB/14/35": "Turkey",
    "ARB/19/3": "Rwanda",
    "CONC(AF)/12/2": "United States"
}

# Manually looked up dates related to the individual cases in the original ICSID dataset
ICSID_MANUAL_DATE_CLEANUP = {
    "UNCT/23/4": "2023-11-30",
    "ADM/21/1": "2020-08-07"
}

PCA_MANUAL_DATE_CLEANUP ={
    "2023-03": "2023"
}

# Manually add economic classification for all missing cases in the dataset
ECONOMY_MAP_MANUAL = {

    # Bolivia
    "Bolivia, Plurinational State Of":
        "Developing economies",

    # Iran
    "Iran, Islamic Republic Of":
        "Developing economies",

    # Côte d'Ivoire
    "Côte D'Ivoire": "Developing economies",

    # Laos
    "Laos": "Developing economies",
    "Lao People'S Democratic Republic":
        "Developing economies",

    # St Kitts
    "Saint Kitts And Nevis":
        "Developing economies",

    # Tanzania
    "Tanzania": "Developing economies",
    "Tanzania, United Republic Of": "Developing economies",

    # Trinidad
    "Trinidad And Tobago": "Developing economies",

    # Venezuela
    "Venezuela": "Developing economies",
    "Venezuela, Bolivarian Republic Of": "Developing economies",

    # Türkiye / Turkey
    "Türkiye": "Developing economies",
    "Turkey": "Developing economies",
    
## Developed economies
    # Bosnia
    "Bosnia And Herzegovina": "Developed economies",

    # South Korea
    "Korea, Republic Of": "Developed economies",
    "South Korea": "Developed economies",

    # Moldova
    "Moldova": "Developed economies",
    "Moldova, Republic Of": "Developed economies",
    
    # Netherlands
    "Netherlands": "Developed economies",

    # Russia
    "Russia": "Developed economies",

    # EU
    "European Union": "Developed economies"
}