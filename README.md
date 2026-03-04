# qPCR Plate Planner (Pro Version)

## Table of Contents
- [Overview](#overview)
- [Quick Start](#quick-start)
- [Professional Visualization](#professional-visualization)
- [Key Features](#key-features)
- [Workflow](#workflow)
- [Statistical & Calculation Methods](#statistical--calculation-methods)
- [Technical Requirements](#technical-requirements)
- [License and Citation](#license-and-citation)

---

## Overview

*qPCR Plate Planner* is a high-performance, browser-based suite for designing, executing, and analyzing quantitative PCR (qPCR) experiments with publication-ready outputs. It bridges the gap between raw Ct data and "Prism-style" scientific figures by integrating:

- **Intelligent 384-Well Layouts**: Optimized for spaced triplicates to minimize cross-contamination.
- **Advanced Statistics**: Automated t-tests and ANOVA with p-value significance mapping (*, **, ***).
- **Quality Control**: Real-time outlier detection using Z-score and IQR methods.
- **Publication-Ready Charts**: Clean, high-contrast "Prism-style" visualizations with SD/SEM error bars.

The tool implements the 2^−ΔΔCt method (Livak & Schmittgen, 2001) with enhanced mathematical validation and error propagation.

---

## Quick Start
1. **Download the Sample**: Get `qPCR_Pro_Example_Dataset.json` from this repository.
2. **Launch the App**: [Live Interface](https://mahmood-m-ali.github.io/qPCR-plate-planner/)  
3. **Import Data**: Click **Import JSON** and select the example file.
4. **Explore**: See how the tool handles 4 genes, calculates significance, and identifies a deliberate outlier in the QC summary.

---

## Professional Visualization (Prism-Style)
The latest version features a major aesthetic overhaul designed for direct inclusion in manuscripts:
- **Clean Aesthetics**: Solid high-contrast colors (Light Gray for Controls, Dark Gray for Conditions) with no distracting background gridlines.
- **Significance Mapping**: Automated horizontal brackets with centered bold stars for instant p-value recognition.
- **Optimized Layout**: 45° rotated X-axis labels and dynamic canvas scaling to prevent gene name collisions.
- **Publication Standards**: 2px bold black axes and standardized font sizing (Inter family).

---

## Key Features

### Statistical Analysis & QC
- **Multiple Test Support**: Choose between Student's t-test or one-way ANOVA.
- **Smart Outlier Detection**: Toggle between Z-score or Interquartile Range (IQR) to identify and exclude "jumpy" replicates.
- **Error Bars**: Select between Standard Deviation (SD) for spread or Standard Error of the Mean (SEM) for precision.
- **Proactive Warnings**: Detects insufficient replicates ($n < 2$) before they cause calculation failures.

### Intelligent Plate Designer
- **Spaced Triplicate Logic**: Built-in templates for 384-well plates that leave "white spacer" columns between samples.
- **Multi-Gene Stacking**: Support for complex layouts involving 10+ genes on a single plate.
- **Master Mix Calculator**: Automatic volume adjustments including safety margins (e.g., 1.1x).

### Data Management
- **JSON Portability**: Save entire experiments (layout + Ct data + analysis settings) in a single portable file.
- **High-Res Export**: Download charts and plate maps as JPEG or vector-quality PDF.
- **Local-First Security**: All calculations happen in your browser; no data is ever uploaded to a server.

---

## Workflow

### Step 1: Define Samples & Groups
Use the `Name_Target_Condition` convention. The tool handles grouping automatically. Assign roles (Control vs. Condition) and define your biological replicates.

### Step 2: Plan Plate Layout (Plate A)
Apply triplicates to the 384-well grid. The tool tracks well usage per target to feed the Master Mix calculator.

### Step 3: Input Ct Data (Plate B)
Paste Ct values directly from your qPCR instrument (LightCycler, QuantStudio, etc.). The grid supports block-pasting from Excel.

### Step 4: Refine Analysis
Select your **Control Target** (e.g., Gapdh) and **Control Condition** (e.g., IgG or Wildtype). Adjust the QC threshold to prune outliers.

### Step 5: Export for Publication
Download the final bar chart with significance stars and the detailed ΔΔCt summary table.

---

## Statistical & Calculation Methods

### Relative Quantification (ΔΔCt)
The tool calculates fold change using the standard formula:
1. **ΔCt** = Ct(Target) − Ct(Reference Gene)
2. **ΔΔCt** = ΔCt(Condition) − ΔCt(Control Condition)
3. **Fold Change** = 2^(−ΔΔCt)

### Statistical Testing
- **Unpaired t-test**: Used for comparing a single condition against the control.
- **ANOVA**: Used for experiments with multiple treatment groups to determine if at least one group differs significantly.
- **p-value levels**:
    - `ns`: p > 0.05
    - `*`: p ≤ 0.05
    - `**`: p ≤ 0.01
    - `***`: p ≤ 0.001

### Outlier Removal
- **Z-Score**: Identifies points more than $N$ standard deviations from the mean.
- **IQR**: Identifies points outside $1.5 \times$ the interquartile range (Tukey's Fences).

---

## Technical Requirements
- **Browser**: Modern versions of Chrome, Firefox, Edge, or Safari.
- **Dependencies**: Uses `Chart.js` (Visuals), `jsPDF` (PDFs), and `html2canvas` (Images) via secure CDNs.
- **No Install**: 100% static HTML/JS/CSS.

---

## License and Citation

Mahmood Mohammed Ali. *qPCR Plate Planner* (2026). GitHub. University of Grenoble Alpes – Institute of Advanced Bioscience (IAB). Licensed under **CC BY-NC 4.0**.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17410644.svg)](https://doi.org/10.5281/zenodo.17410644)

[LinkedIn Profile](https://www.linkedin.com/in/mahmood-mohammed-ali-20334b205)
