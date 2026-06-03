# Project Title
# How to set up environment (windows + mac - uv management)
# How to load requirements.txt
# Data sourcing
# Project Structure

# Overview

This project builds a cleaned and analysis-ready dataset of investor–state dispute settlement (ISDS) cases from the International Centre for Settlement of Investment Disputes (ICSID).

The workflow extracts raw ICSID case data from the ICSID API, standardizes respondent state names, validates and repairs registration dates, and identifies mining-sector disputes for downstream empirical analysis.

# Data Pipeline
## 1. ICSID API Extraction

All ICSID cases were retrieved directly from the ICSID API endpoint:

Full case dataset
Mining-sector subset (es=101)

Raw JSON responses were normalized into tabular format using Pandas and archived as raw CSV files for reproducibility.

## 2. Nested Data Expansion

The nested casedecisions and caseproceedings fields were parsed and expanded into flat tabular structures using:

ast.literal_eval
pandas.json_normalize

These fields were merged back into the main case dataset to create a denormalized analytical table.

Columns containing only null or empty values were removed during cleaning.

## 3. Country Name Standardization

Respondent-state names were extracted from the raw respondent field and standardized into canonical sovereign country names.

Country normalization was implemented through a custom utility module built with:

Python
Pandas
pycountry

The extraction pipeline included:

Manual alias mappings
Embedded-country matching
ISO3 country-code generation
Exclusion of non-sovereign entities and corporations
Match-method auditing for transparency

Examples:

Raw Input	Standardized Output
Republic of Korea	South Korea
Commonwealth of Australia	Australia
Republic of Turkey	Turkey

Cases where no sovereign respondent state could be identified were isolated into a separate review dataset.

## 4. Date Validation and Cleaning

The dateregistered field was converted into datetime format using Pandas.

The workflow identified:

Missing registration dates
Unparseable date values
Formatting inconsistencies

Manual corrections were applied only to missing entries using a reproducible dictionary-based cleanup process.

Additional temporal features were engineered from the cleaned date column:

Registration year
Registration month
Registration day
## 5. Mining-Sector Classification

Mining-sector disputes were identified using the filtered ICSID mining dataset.

Cases were labeled as:

Yes → mining-related dispute
No → non-mining dispute

using the ICSID case number (caseno) as the matching key.

## 6. Output

The final processed dataset includes:

Standardized respondent states
ISO3 country codes
Clean registration dates
Temporal variables
Mining-sector classification
Expanded procedural and decision data

The cleaned analytical dataset is exported to:

data/interim/icsid_clean_cases_202606_processed.csv
Technologies Used
Python
Pandas
Requests
PyCountry
Jupyter Notebook
Reproducibility

The workflow is fully reproducible and structured using:

Raw data snapshots
Utility modules (utils/)
Intermediate cleaned datasets
Deterministic transformation steps