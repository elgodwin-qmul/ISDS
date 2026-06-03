# Workflow Summary

This project builds a harmonized investor–state dispute settlement (ISDS) dataset by integrating arbitration case data from:

* ICSID
* UNCTAD ISDS Navigator
* Permanent Court of Arbitration (PCA)

The workflow performs the following steps:

1. **Data Extraction**

   * Retrieve ICSID case data from the ICSID API
   * Import UNCTAD and PCA datasets from structured Excel sources
   * Archive raw source data for reproducibility

2. **Data Normalization**

   * Expand nested JSON structures into flat analytical tables
   * Standardize respondent-state names using a reusable country-cleaning utility built with `pycountry`
   * Generate ISO3 country codes
   * Reconcile unresolved country entries through manual validation dictionaries

3. **Date Cleaning**

   * Parse and validate arbitration registration/commencement dates
   * Identify missing and malformed values
   * Apply reproducible manual corrections where necessary
   * Engineer year, month, and day variables for temporal analysis

4. **Mining-Sector Classification**

   * Identify mining-related disputes using:

     * ICSID mining-sector API filters
     * UNCTAD economic-sector labels
     * PCA sector classifications
   * Create harmonized binary mining indicators across datasets

5. **Dataset Crosswalking**

   * Match arbitration case numbers across ICSID, UNCTAD, and PCA datasets
   * Identify overlapping and institution-specific disputes
   * Recover missing PCA case identifiers using regex extraction

6. **Final Output**

   * Produce cleaned and analysis-ready datasets containing:

     * standardized respondent countries
     * ISO3 country codes
     * cleaned dates
     * mining indicators
     * institutional overlap indicators
     * harmonized arbitration identifiers

The resulting datasets are structured for empirical ISDS analysis, institutional comparison, and mining-sector dispute research.

# Final Dataset Harmonization and Merge

Following independent cleaning and standardization of the ICSID, UNCTAD, and PCA datasets, the project harmonizes all three sources into a single unified analytical dataset.

---

## 20. Column Harmonization

To ensure schema consistency across institutions, each dataset's key analytical columns were standardized into a shared structure.

The harmonized schema includes:

| Standardized Column | Description                          |
| ------------------- | ------------------------------------ |
| `country_clean`     | Standardized respondent-state name   |
| `case_number`       | Arbitration case identifier          |
| `year`              | Year of case registration/initiation |
| `mining_case`       | Mining-sector indicator              |

Institution-specific column mappings were defined for:

* ICSID
* UNCTAD
* PCA

This normalization step ensured interoperability across datasets prior to merging.

---

## 21. Cross-Institution Deduplication

To avoid duplicate arbitration proceedings across institutions, the workflow applied sequential dataset filtering:

* All ICSID cases were retained
* Only UNCTAD cases not already present in ICSID were retained
* Only PCA cases not already present in UNCTAD were retained

This produced a non-overlapping arbitration dataset while preserving institution-specific coverage.

Deduplication was performed using standardized arbitration case identifiers.

---

## 22. Unified ISDS Dataset Construction

The cleaned and deduplicated datasets were concatenated into a single master analytical dataframe.

The final merged dataset contains:

* harmonized country identifiers
* standardized arbitration case numbers
* year variables
* mining-sector indicators

The unified dataset was exported to:

```text
data/processed/MINING_CASES_202606.csv
```

This dataset represents a consolidated cross-institution ISDS database suitable for:

* mining-sector dispute analysis
* temporal trend analysis
* respondent-state analysis
* institutional comparison
* empirical ISDS research

# Economy Classification Integration

Following construction of the unified ISDS dataset, the workflow integrates UNCTAD country-level economy classifications to support comparative economic analysis.

---

## 23. UNCTAD Economy Classification Extraction

Country-level economy classifications were extracted from the UNCTAD country hierarchy dataset.

The workflow filtered the hierarchy table to retain only the top-level economy groupings:

* Developed economies
* Developing economies

These classifications were isolated into a dedicated interim dataset for downstream merging and reproducibility.

---

## 24. Country Name Harmonization and Merge

To ensure successful joins across datasets, country names in both datasets were standardized using:

* whitespace trimming
* title-case normalization

The unified ISDS dataset was then merged with the UNCTAD economy-classification dataset using standardized country names.

This merge added a new analytical variable:

| Column                   | Description                                  |
| ------------------------ | -------------------------------------------- |
| `economy_classification` | UNCTAD economy grouping for respondent state |

The merge was performed using a left join to preserve all arbitration cases.

---

## 25. Missing Classification Validation and Manual Reconciliation

Following the merge, the workflow audited all missing economy classifications.

Most unresolved matches were caused by:

* spelling inconsistencies
* alternate sovereign naming conventions
* geopolitical naming differences

Examples included:

* `Türkiye`
* `South Korea`
* `Laos`
* `Venezuela`

Manual reconciliation was performed using a dedicated mapping dictionary stored in:

```text
utils/constant_variables.py
```

through:

```text
ECONOMY_MAP_MANUAL
```

Manual mappings were applied only to rows missing an economy classification.

Following reconciliation, all arbitration cases were successfully assigned an economy classification.

---

## 26. Final Classification Cleanup

The final economy classification labels were standardized through additional string cleaning operations.

This included:

* removal of redundant text such as:

```text
economies
```

* trimming leading and trailing whitespace across all string columns

The resulting economy classification variable contains clean and analysis-ready labels suitable for:

* descriptive statistics
* comparative economic analysis
* grouped mining-dispute analysis
* visualization workflows

---

## Final Analytical Dataset

The final processed ISDS dataset now includes:

* harmonized arbitration case identifiers
* standardized respondent countries
* ISO3 country codes
* cleaned temporal variables
* mining-sector indicators
* institutional overlap indicators
* UNCTAD economy classifications

This produces a consolidated cross-institution investor–state dispute dataset ready for empirical analysis and research workflows.

# Visualization and Exploratory Analysis

The project includes reusable visualization utilities to support exploratory analysis and reproducible figure generation across the harmonized ISDS dataset.

Custom plotting functions were developed within:

```text
utils/bar_plot_utils.py
```

These utilities standardize:

* annual case visualizations
* grouped stacked-bar comparisons
* total-case annotations
* automatic figure export workflows

All plots are automatically saved to the project `plots/` directory for reproducibility and downstream reporting.

---

## 27. Annual ISDS Case Volume

The workflow generates annual counts of all investor–state dispute settlement cases across the unified dataset.

Cases are grouped by initiation year and visualized using a yearly bar chart with:

* annual case totals
* grand-total comparison bar
* automated annotations

The resulting figure is exported to:

```text
plots/annual_cases.png
```

This visualization supports:

* temporal trend analysis
* dispute-growth analysis
* institutional activity comparisons over time

---

## 28. Mining vs Non-Mining Dispute Analysis

The harmonized dataset is further analyzed by dispute sector classification.

Using the binary:

```text
mining_case
```

indicator, annual disputes are grouped into:

* mining-related disputes
* non-mining disputes

The workflow produces a stacked annual comparison chart containing:

* annual sector counts
* percentage annotations
* overall totals
* comparative yearly trends

The resulting figure is exported to:

```text
plots/annual_cases_mining.png
```

This visualization enables analysis of:

* mining-sector arbitration growth
* sectoral dispute composition
* long-run mining-dispute trends

---

## 29. Developed vs Developing Economy Analysis

The final visualization groups arbitration cases according to the respondent state's UNCTAD economy classification.

Using the:

```text
economy_classification
```

variable, annual disputes are classified into:

* developing economies
* developed economies

The workflow generates a stacked annual comparison chart with:

* yearly case totals
* proportional annotations
* aggregate institutional totals
* longitudinal economy-group comparisons

The resulting figure is exported to:

```text
plots/annual_cases_economies.png
```

This enables comparative analysis of:

* ISDS exposure by economic grouping
* dispute concentration trends
* developing versus developed economy participation in arbitration proceedings

---

## Reusable Visualization Framework

The plotting utilities were designed as reusable analytical components.

The visualization framework supports:

* configurable grouped comparisons
* reusable annual aggregation logic
* automated annotation workflows
* publication-ready figure export
* reproducible plotting pipelines

This modular structure allows additional comparative visualizations to be generated with minimal notebook code.

