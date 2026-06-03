# ISDS Mining Disputes Dataset

## Overview

This project builds a harmonized investor–state dispute settlement (ISDS) dataset by integrating arbitration case data from:

* ICSID
* UNCTAD ISDS Navigator
* Permanent Court of Arbitration (PCA)

The workflow produces a cleaned and analysis-ready dataset for empirical analysis of ISDS disputes, mining-sector arbitration, and respondent-state trends.

---

# Workflow Summary

## 1. Data Extraction

The pipeline ingests data from multiple institutional sources:

* ICSID case data retrieved directly from the ICSID API
* UNCTAD ISDS Navigator data imported from Excel workbooks
* PCA investor–state arbitration data imported from Excel workbooks

Raw source files are archived for reproducibility.

---

## 2. Data Cleaning and Standardization

The workflow standardizes and harmonizes datasets across institutions by:

* Expanding nested JSON structures into flat analytical tables
* Cleaning respondent-state names using reusable country utilities
* Standardizing sovereign country names
* Generating ISO3 country codes
* Validating missing or malformed entries
* Applying reproducible manual reconciliation dictionaries where automated extraction fails

Country normalization is implemented using:

* Python
* Pandas
* `pycountry`
* Regex-based cleaning utilities

### Example Country Standardization

| Raw Input                   | Standardized Output |
| --------------------------- | ------------------- |
| `Republic of Korea`         | `South Korea`       |
| `Republic of Turkey`        | `Turkey`            |
| `Commonwealth of Australia` | `Australia`         |

---

## 3. Date Validation and Repair

The workflow validates arbitration registration and commencement dates by:

* Parsing datetime values
* Identifying missing or malformed entries
* Applying manual date repairs through reusable cleanup dictionaries
* Engineering temporal variables including:

  * year
  * month
  * day

This ensures consistent longitudinal analysis across all institutional datasets.

---

## 4. Mining-Sector Classification

Mining-sector disputes are identified using:

* ICSID mining-sector API filters
* UNCTAD economic-sector labels
* PCA sector classifications

Cases are standardized into a binary indicator:

| Value | Meaning                |
| ----- | ---------------------- |
| `Yes` | Mining-related dispute |
| `No`  | Non-mining dispute     |

Regex-enabled matching is used to handle inconsistent sector-label formatting across datasets.

---

## 5. Dataset Crosswalking and Deduplication

The workflow cross-references arbitration case numbers across institutions to identify:

* overlapping disputes
* institution-specific disputes
* missing arbitration identifiers

The harmonization process:

* retains all ICSID cases
* keeps only UNCTAD cases not already present in ICSID
* keeps only PCA cases not already present in UNCTAD

This produces a unified non-overlapping ISDS dataset.

---

## 6. Economy Classification Integration

The final merged dataset integrates respondent-state economy classifications using UNCTAD country hierarchy data.

The workflow:

* extracts developed and developing economy labels
* standardizes country names across datasets
* merges classifications into the unified ISDS dataset
* manually reconciles unresolved country-label mismatches

This produces a new analytical variable:

| Column                   | Description                              |
| ------------------------ | ---------------------------------------- |
| `economy_classification` | Developed or Developing economy grouping |

---

## 7. Unified Dataset Construction

The cleaned ICSID, UNCTAD, and PCA datasets are harmonized into a single analytical dataframe containing:

* standardized respondent countries
* ISO3 country codes
* harmonized case identifiers
* cleaned temporal variables
* mining-sector indicators
* economy classifications
* institutional overlap indicators

### Final Dataset Export

```text
data/processed/MINING_CASES_202606.csv
```

---

# Visualization and Exploratory Analysis

The project includes reusable visualization utilities located in:

```text
utils/bar_plot_utils.py
```

These utilities generate publication-ready figures for:

* annual ISDS case volumes
* mining vs non-mining disputes
* developed vs developing economy comparisons

Generated figures are automatically exported to:

```text
plots/
```

### Generated Figures

| Figure                       | Description                              |
| ---------------------------- | ---------------------------------------- |
| `annual_cases.png`           | Total ISDS cases per year                |
| `annual_cases_mining.png`    | Mining vs non-mining disputes            |
| `annual_cases_economies.png` | Developed vs developing economy disputes |

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Requests
* PyCountry
* Jupyter Notebook

---

# Project Structure

```text
project/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── notebooks/
│
├── plots/
│
├── utils/
│   ├── country_utils.py
│   ├── constant_variables.py
│   └── bar_plot_utils.py
│
├── requirements.txt
└── README.md
```

---

# Reproducibility

The workflow is fully reproducible through:

* archived raw datasets
* reusable utility modules
* deterministic transformation pipelines
* intermediate cleaned datasets
* manual reconciliation dictionaries
* automated plotting utilities
