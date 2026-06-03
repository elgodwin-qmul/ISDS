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
