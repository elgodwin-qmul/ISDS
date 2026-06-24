# Investor-State Dispute Settlement System as a Barrier to Environmental Justice
## Table of Contents

- [Overview](#overview)
- [Contributions](#contributions)
- [Citation](#citation)
- [ISDS Mining Disputes Dataset](#isds-mining-disputes-dataset)
- [Workflow Summary](#workflow-summary)
  - [1. Data Extraction](#1-data-extraction)
  - [2. Data Cleaning and Standardization](#2-data-cleaning-and-standardization)
  - [3. Date Validation and Repair](#3-date-validation-and-repair)
  - [4. Mining-Sector Classification](#4-mining-sector-classification)
  - [5. Dataset Crosswalking and Deduplication](#5-dataset-crosswalking-and-deduplication)
  - [6. Economy Classification Integration](#6-economy-classification-integration)
  - [7. Unified Dataset Construction](#7-unified-dataset-construction)
- [Visualization and Exploratory Analysis](#visualization-and-exploratory-analysis)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation and Reproducibility Setup](#installation-and-reproducibility-setup)
- [Reproducibility](#reproducibility)

## Overview

This repository contains supplementary data analysis, visualisations, and reproducibility materials associated with the research paper:

> Investor-State Dispute Settlement System as a Barrier to Environmental Justice
>
> Godwin, E.L.
>
> TBC
>
> DOI: TBC

## Contributions

### Research

- Dr. E. Godwin

### Software and Data Analysis

- Dr. K. P. Bolton

Responsibilities:
- Data collection & processing
- Statistical analysis
- Visualisation
- Computational reproducibility

## Citation

If using the research findings, please cite the original paper.

If using the code or analysis workflow from this repository, please also cite this repository and acknowledge the software contribution.


# ISDS Mining Disputes Dataset

## Overview

This project builds a harmonised investor–state dispute settlement (ISDS) dataset by integrating arbitration case data from:

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
* Validating missing or malformed entries
* Applying reproducible manual reconciliation dictionaries where automated extraction fails

Country normalization is implemented using:

* Python
* Pandas
* `pycountry`
* Regex-based cleaning utilities

### Example Country Standardization

| Raw Input                   | Standardised Output |
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

Cases are standardised into a binary indicator:

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

The cleaned ICSID, UNCTAD, and PCA datasets are harmonised into a single analytical dataframe containing:

* standardised respondent countries
* ISO3 country codes
* harmonised case identifiers
* cleaned temporal variables
* mining-sector indicators
* economy classifications
* institutional overlap indicators

### Final Dataset Export

The final dataset exported and used in the analysis contains:
* standardised respondent countries
* harmonised case identifiers
* case year
* mining-sector indicators
* economy classifications

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

# Installation and Reproducibility Setup

This repository uses the Python package manager **uv** to provide a fully reproducible computational environment. The recommended approach is to recreate the environment directly from the provided `pyproject.toml` and `uv.lock` files.

## Prerequisites

### Install Python

This project requires:

```text
Python 3.12 or later
```

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

## Install uv

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

---

## Clone the Repository

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the repository URL.

---

## Create the Reproducible Environment

The repository includes:

```text
pyproject.toml
uv.lock
```

which define the exact software environment used in the study.

Create and synchronize the environment:

```bash
uv sync
```

This command:

* creates a local virtual environment (`.venv`)
* installs all required dependencies
* reproduces the exact package versions recorded in `uv.lock`

---

## Activate the Environment

### Windows

```powershell
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## Verify Installation

Run:

```bash
python -c "import pandas, matplotlib, pycountry, requests; print('Environment successfully configured')"
```

If no errors are returned, the environment has been recreated successfully.

---

## Running the Analysis

Execute notebooks or Python scripts within the activated environment.

For example:

```bash
jupyter notebook
```

or

```bash
python path/to/script.py
```

Generated datasets will be written to:

```text
data/processed/
```

Generated figures will be written to:

```text
plots/
```

---

## Reproducing the Original Environment

For exact computational reproducibility, users should rely on:

```text
pyproject.toml
uv.lock
```

rather than manually installing packages.

The `uv.lock` file records the precise dependency versions used when generating the results reported in the accompanying publication.

To recreate the environment at any time:

```bash
uv sync
```

No manual dependency installation is required.

---

## Alternative Installation Using pip

A pip-compatible requirements file is also provided.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

The uv workflow is recommended because it provides stronger reproducibility guarantees through dependency locking.

