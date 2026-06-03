# Project Title
# How to set up environment (windows + mac - uv management)
# How to load requirements.txt
# Data sourcing
# Project Structure

## Overview

This project builds a cleaned and analysis-ready dataset of investor–state dispute settlement (ISDS) cases from the International Centre for Settlement of Investment Disputes (ICSID).

The workflow extracts raw ICSID case data from the ICSID API, standardizes respondent state names, validates and repairs registration dates, and identifies mining-sector disputes for downstream empirical analysis.

---

# Data Pipeline

## 1. ICSID API Extraction

All ICSID cases were retrieved directly from the ICSID API endpoint:

* Full case dataset
* Mining-sector subset (`es=101`)

Raw JSON responses were normalized into tabular format using Pandas and archived as raw CSV files for reproducibility.

---

## 2. Nested Data Expansion

The nested `casedecisions` and `caseproceedings` fields were parsed and expanded into flat tabular structures using:

* `ast.literal_eval`
* `pandas.json_normalize`

These fields were merged back into the main case dataset to create a denormalized analytical table.

Columns containing only null or empty values were removed during cleaning.

---

## 3. Country Name Standardization

Respondent-state names were extracted from the raw `respondent` field and standardized into canonical sovereign country names.

Country normalization was implemented through a custom utility module built with:

* Python
* Pandas
* `pycountry`

The extraction pipeline included:

* Manual alias mappings
* Embedded-country matching
* ISO3 country-code generation
* Exclusion of non-sovereign entities and corporations
* Match-method auditing for transparency

Examples:

| Raw Input                   | Standardized Output |
| --------------------------- | ------------------- |
| `Republic of Korea`         | `South Korea`       |
| `Commonwealth of Australia` | `Australia`         |
| `Republic of Turkey`        | `Turkey`            |

---

## 4. Missing Country Validation and Manual Cleanup

Following automated country extraction, the workflow identified all cases where a sovereign respondent state could not initially be extracted.

The pipeline:

* Counted all missing country entries
* Generated a review list of affected ICSID case numbers
* Exported unresolved cases for manual inspection and documentation

Manual country corrections were then applied using a reproducible dictionary-based lookup stored in:

```text
utils/constant_variables.py
```

This allowed unresolved cases to be mapped manually using independently verified respondent-state information.

Corrections were applied only to rows where:

* `country_clean` was missing
* the case number matched the manual cleanup dictionary

Following manual reconciliation, all cases in the dataset were associated with a standardized respondent country.

---

## 5. Date Validation and Cleaning

The `dateregistered` field was converted into datetime format using Pandas.

The workflow identified:

* Missing registration dates
* Unparseable date values
* Formatting inconsistencies

Manual corrections were applied only to missing entries using a reproducible dictionary-based cleanup process.

Additional temporal features were engineered from the cleaned date column:

* Registration year
* Registration month
* Registration day

---

## 6. Mining-Sector Classification

Mining-sector disputes were identified using the filtered ICSID mining dataset.

Cases were labeled as:

* `Yes` → mining-related dispute
* `No` → non-mining dispute

using the ICSID case number (`caseno`) as the matching key.

---

## 7. Output

The final processed dataset includes:

* Standardized respondent states
* ISO3 country codes
* Clean registration dates
* Temporal variables
* Mining-sector classification
* Expanded procedural and decision data

The cleaned analytical dataset is exported to:

```text
data/interim/icsid_clean_cases_202606_processed.csv
```

---

## Technologies Used

* Python
* Pandas
* Requests
* PyCountry
* Jupyter Notebook

---

## Reproducibility

The workflow is fully reproducible and structured using:

* Raw data snapshots
* Utility modules (`utils/`)
* Intermediate cleaned datasets
* Deterministic transformation steps
* Manual reconciliation dictionaries for unresolved country and date entries



# UNCTAD ISDS Dataset Integration

In addition to the ICSID API dataset, this project integrates dispute data from the UNCTAD ISDS Navigator to create a broader and cross-validated ISDS analytical dataset.

---

## 8. UNCTAD Dataset Extraction

The UNCTAD ISDS Navigator dataset was imported from a structured Excel workbook.

The workflow separates:

* Historical UNCTAD data up to and including 2023
* Manually collected post-2023 cases extracted directly from the UNCTAD website

Both datasets were loaded independently and combined into a unified working dataframe.

---

## 9. ICSID Case Number Extraction

ICSID arbitration case numbers were extracted from the `FULL CASE NAME` column using regular expressions.

The extraction pipeline supports:

* Standard ICSID arbitration numbers
* Additional Facility proceedings (`ARB(AF)`)

Example extracted formats:

```text
ARB/12/4
ARB(AF)/20/1
```

The extracted case numbers were stored in a standardized `CASE NO.` field.

The historical and post-2023 UNCTAD datasets were then concatenated into a single analytical dataset.

---

## 10. Country Standardization

Respondent-state names in the UNCTAD dataset were standardized using the same reusable country-normalization utility developed for the ICSID pipeline.

The extraction workflow:

* Parsed respondent-state names from the `RESPONDENT STATE` column
* Standardized sovereign country names
* Generated ISO3 country codes
* Recorded extraction methods for auditability

The cleaning pipeline used:

* `pycountry`
* Manual alias dictionaries
* Embedded-country extraction logic
* Regex-based normalization procedures

---

## 11. Manual Country Reconciliation

Cases where no country could initially be extracted were isolated into a separate review dataset.

Manual reconciliation was then performed using:

* `SHORT CASE NAME`
* `RESPONDENT STATE`

A manual mapping dictionary was created and applied only to unresolved rows.

All manually corrected entries were labeled with:

```text
extraction_method = "manual"
```

Following reconciliation, all UNCTAD cases were successfully assigned a standardized respondent country.

---

## 12. Mining-Sector Classification

Mining-sector disputes were identified using the `ECONOMIC SECTOR` column.

Cases were classified as mining-related if the sector description contained:

```text
Mining and quarrying
```

The workflow used regex-enabled string matching to handle inconsistent formatting patterns within the UNCTAD source data.

Cases were labeled as:

* `Yes` → mining-related dispute
* `No` → non-mining dispute

---

## 13. ICSID–UNCTAD Dataset Crosswalk

The UNCTAD dataset was cross-referenced against the cleaned ICSID dataset using arbitration case numbers.

Using the standardized `CASE NO.` field, the workflow identified:

* Cases already present in the ICSID dataset
* Cases unique to the UNCTAD dataset

This produced an overlap indicator column:

```text
IN ICSID DATA
```

with values:

* `Yes`
* `No`

This crosswalk enables comparative analysis between the two institutional datasets.

---

## 14. PCA Case Number Recovery

Some UNCTAD entries lacked standardized case numbers in the primary case-number field.

Additional Permanent Court of Arbitration (PCA) case numbers were recovered from the `Notes` column using regex extraction.

Example extracted format:

```text
PCA Case No. 2019-12
```

Recovered PCA identifiers were inserted into the `CASE NO.` column to improve dataset completeness and downstream matching reliability.

---

## Result

The integrated UNCTAD workflow produces a cleaned and harmonized ISDS dataset containing:

* Standardized respondent countries
* ISO3 country codes
* Mining-sector classification
* ICSID overlap indicators
* Extracted arbitration case numbers
* PCA case identifiers
* Audit trails for manual country reconciliation

The resulting dataset is structured for empirical ISDS analysis and institutional comparison across arbitration forums.

