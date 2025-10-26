# qPCR Plate Planner

## Table of Contents
- [Overview](#overview)
- [Quick Start](#quick-start)
- [Use Cases](#use-cases)
- [Key Features](#key-features)
- [Workflow](#workflow)
- [Calculation Methods](#calculation-methods)
- [Technical Requirements](#technical-requirements)
- [Libraries](#libraries)
- [License and Citation](#license-and-citation)

---

## Overview

*qPCR Plate Planner* is a browser-based tool for designing, executing, and analyzing quantitative PCR (qPCR) experiments. It integrates:

- 384-well plate layout design  
- Master mix volume calculation  
- Ct value entry and synchronization  
- ΔΔCt analysis with automated fold-change computation and visualization  

The tool applies the 2^−ΔΔCt method for relative quantification (Livak & Schmittgen, 2001. [DOI:10.1006/meth.2001.1262](https://doi.org/10.1006/meth.2001.1262)), adapted for CUT&RUN workflows assessing target enrichment.

Although originally developed for CUT&RUN, it is broadly applicable to ChIP-qPCR, CUT&Tag, gene expression profiling, and drug response assays.

---

## Quick Start

1. Open the planner: [Live Interface](https://mahmood-m-ali.github.io/qPCR-plate-planner/)  
2. Click **Import JSON** and select `example-import.json` from the repository  
3. Explore sample metadata, plate layout, and ΔΔCt analysis

## Demo: Using the Example JSON

![qPCR Planner Demo](assets/qPCR-demo.gif)
---

## Use Cases

Designed for molecular biologists conducting qPCR experiments involving:

- Multiple target genes and conditions  
- Distinct experimental groups co-plated on a single 384-well plate  
- Technical replicates  
- Comparative gene expression analysis using ΔΔCt  
- Chromatin profiling validation (e.g., CUT&RUN, ChIP-qPCR)

---

## Key Features

### Sample Management
- Auto-parsing of sample names (`Name_Target_Condition`)  
- Unique color assignment for visual clarity  
- Grouping by target, condition, and role (Control/Condition)

### Plate Layout Designer (Plate A)
- Interactive 384-well grid (16×24)  
- Sample assignment via click  
- Color-coded legend and real-time well tracking  
- Undo/redo and export as JPEG/PDF

### Master Mix Calculator
- Well count per target gene  
- Safety margin wells  
- Reagent definition and per-well volumes  
- Total volume calculation per target

### Ct Value Entry (Plate B)
- Spreadsheet-style input grid  
- Paste support from Excel/Google Sheets  
- Synchronization with Plate A layout

### ΔΔCt Analysis & Visualization
- Mean Ct calculation from replicates  
- ΔCt and ΔΔCt computation  
- Fold-change via 2^(-ΔΔCt)  
- Interactive bar chart and summary table  
- Export as JPEG/PDF

### Data Management
- Automatic local storage  
- JSON export/import for reproducibility  
- Metadata tracking (name, date, notes)
- Download your plate planning and ct results and the charts as PDF or JPEG

---

## Workflow

### Step 1: Define Samples
Use the naming convention `Name_Target_Condition` (e.g., `HeLa_CCNA2_IgG`). The tool automatically extracts the target gene and condition from each sample name. Assign each sample a unique color **ensure that no two samples share the same color**, as this may compromise visual clarity and downstream analysis. Specify the role (Control or Condition) and assign each sample to a group.

### Step 2: Design Plate Layout
Select samples and assign them to wells on Plate A. Supports multiplexing (up to 4 samples per well).

### Step 3: Plan Master Mix
Define reagents and volumes. The tool calculates total volumes per target gene.

### Step 4: Enter Ct Values
Paste Ct data from your instrument into Plate B. Supports single and block pasting.

### Step 5: Analyze Results
Configure control condition and reference gene. The tool performs ΔCt, ΔΔCt, and fold-change analysis.

---

## Calculation Methods

### Mean Ct  
The average of Ct values across all wells assigned to a given sample, accounting for technical replicates.

### ΔCt  
Calculated as:  
**ΔCt = Ct(sample) − Ct(control within same target)**  
This normalizes expression within each target gene relative to its control condition (e.g., IgG control).

### ΔΔCt  
Calculated as:  
**ΔΔCt = ΔCt(target gene) − ΔCt(reference gene)**  
This normalizes expression across different target genes using a reference gene (e.g., housekeeping gene).

### Fold Change  
Calculated as:  
**Fold Change = 2^(−ΔΔCt)**  
This represents relative gene expression or enrichment level.

**Interpretation:**
- Fold Change = 1 → No change  
- Fold Change > 1 → Upregulation or enrichment  
- Fold Change < 1 → Downregulation or depletion

---

## Technical Requirements

- Modern browser: Chrome, Firefox, Safari, Edge  
- No installation required  
- Data stored locally on your own device via `localStorage`  
- An internet connection is required only once to load external libraries via CDN; after that, all functionality runs locally in the browser without further connectivity.
  
---

## Libraries

- `Chart.js` – Data visualization  
- `jsPDF` – PDF export  
- `html2canvas` – Image capture

---

## License and Citation

Mahmood Mohammed Ali. *qPCR Plate Planner* (2025). GitHub. University of Grenoble Alpes – Institute of Advanced Bioscience (IAB). Licensed under **CC BY-NC 4.0**.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17410644.svg)](https://doi.org/10.5281/zenodo.17410644)

[LinkedIn Profile](https://www.linkedin.com/in/mahmood-mohammed-ali-20334b205)
