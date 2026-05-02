# qPCR Plate Planner (Pro Version 3.0)

## Table of Contents
- [Overview](#overview)
- [Quick Start](#quick-start)
- [Key Features](#key-features)
- [Workflow](#workflow)
- [Statistical & Calculation Methods](#statistical--calculation-methods)
- [Technical Requirements](#technical-requirements)
- [License and Citation](#license-and-citation)

---

## Overview

*qPCR Plate Planner* is a high-performance, browser-based suite for designing, executing, and analyzing quantitative PCR (qPCR) experiments. It provides a unified environment for generating high-quality, publication-ready scientific figures directly in your browser. 

Version 3.0 introduces a massive update handling multi-omic workflows, including standard relative expression, CUT&RUN / CUT&TAG enrichment, and absolute quantification with standard curves.

---

## Quick Start
1. **Launch the App**: [Live Interface](https://mahmood-m-ali.github.io/qPCR-plate-planner/)
2. **Start Planning**: Add your samples and targets using the intuitive interface.
3. **Save and Load**: You can export your entire experimental setup as a JSON file and import it back anytime.

---

## Key Features

### 🔬 Advanced Analysis Modes
- **Relative Expression**: Calculate standard ΔΔCt or Fold Change (2^-ΔΔCt) for gene expression.
- **Enrichment / Occupancy**: Specially designed terminology and scaling for CUT&RUN and CUT&TAG experiments (e.g., Fold Enrichment over IgG).
- **Absolute Quantification**: Built-in standard curve generation with regression analysis, R², and efficiency calculations.
- **Multi-Reference Normalization**: Select multiple housekeeping/reference genes, and the app will automatically use their geometric mean for stable baseline normalization.
- **Inter-Run Calibrator (IRC)**: Normalize variation across multiple 384-well plates seamlessly.
- **Pfaffl Adjustments**: Adjust for variable primer efficiencies directly in your calculations.

### 📊 Scientific-Grade Visualization
- **Group-Based Analysis**: Split complex plates into logical biological groups, generating individual charts for each comparison.
- **Automated Significance Mapping**: Automatically computes t-tests/ANOVA (with FDR corrections) and plots horizontal brackets with standardized p-value stars (*, **, ***) directly onto the charts.
- **Dynamic Heatmaps**: View Ct and ΔCt heatmaps overlaid directly on your 384-well plate to spot technical gradients at a glance.
- **Clean Aesthetics**: High-contrast, publication-ready vector charts built with Chart.js.

### ⚙️ Statistical Analysis & QC
- **Multiple Test Support**: Choose between Student's t-test or one-way ANOVA. Includes False Discovery Rate (FDR/Benjamini-Hochberg) corrections.
- **Smart Outlier Detection**: Toggle between Z-score or Interquartile Range (IQR) to identify and exclude technical replicates that deviate from the mean.
- **Error Bars**: Select between Standard Deviation (SD) for data spread or Standard Error of the Mean (SEM) for statistical precision.

### 📝 Intelligent Plate Designer
- **Spaced Triplicate Logic**: Built-in templates for 384-well plates that leave "white spacer" columns between samples to minimize cross-talk.
- **Master Mix Calculator**: Automatic volume adjustments including configurable safety margins.
- **Bench Protocol Export**: Export a clean, printable PDF summarizing your plate layout and master mix recipes for use at the lab bench.

### 📁 Data Management & Export
- **JSON Portability**: Save entire experiments (layout + Ct data + analysis settings) in a single portable file.
- **Batch Export**: Download all generated charts instantly as a single ZIP file or a combined PDF.
- **High-Res Export**: Download individual charts and plate maps as JPEG or PDF.
- **Local-First Security**: All calculations happen in your browser; no data is ever uploaded to a server.

---

## Workflow

### Step 1: Define Samples & Groups
Input your genes, cell lines, and conditions. Assign roles (Control, Condition, or Standard). Group them to keep complex analyses cleanly separated.

### Step 2: Plan Plate Layout (Plate A)
Apply triplicates to the 384-well grid. The tool tracks well usage per target to feed the Master Mix calculator. Use the Heatmap tools to verify your layouts.

### Step 3: Input Ct Data (Plate B)
Paste Ct values directly from your qPCR instrument. The grid supports block-pasting from spreadsheet applications.

### Step 4: Refine Analysis
Select your **Control Target** (reference gene) and **Control Condition**. Choose your calculation mode (e.g. ΔΔCt, Pfaffl, Fold Change) and adjust the QC thresholds to prune technical outliers automatically.

### Step 5: Export Data
Download your publication-ready charts (PNG/PDF) and the Bench Protocol for your records.

---

## Statistical & Calculation Methods

### Relative Quantification
- **ΔCt** = Ct(Target) − Ct(Reference)
- **ΔΔCt** = ΔCt(Condition) − ΔCt(Control Condition)
- **Fold Change** = 2^-ΔΔCt

### Statistical Testing
- **Unpaired t-test**: Used for comparing a single condition against the control.
- **ANOVA**: Used for experiments with multiple treatment groups.
- **FDR Correction**: Benjamini-Hochberg procedure available for multiple comparisons.

### Outlier Removal
- **Z-Score**: Identifies points more than a configurable number of standard deviations from the mean.
- **IQR**: Identifies points outside 1.5 × the interquartile range.

---

## Technical Requirements
- **Browser**: Modern versions of Chrome, Firefox, Edge, or Safari.
- **Dependencies**: Uses `Chart.js` (Visuals), `jsPDF` (PDFs), `html2canvas` (Images), and `JSZip` (Archiving) via secure CDNs.
- **No Install**: 100% static HTML/JS/CSS.

---

## License and Citation

Mahmood Mohammed Ali. *qPCR Plate Planner* (v3.0.0, 2026). GitHub. University of Grenoble Alpes – Institute of Advanced Bioscience (IAB). Epigenetics of Regeneration and Cancer Group. Licensed under **CC BY-NC 4.0**.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17410644.svg)](https://doi.org/10.5281/zenodo.17410644)

[LinkedIn Profile](https://www.linkedin.com/in/mahmood-mohammed-ali-20334b205)
