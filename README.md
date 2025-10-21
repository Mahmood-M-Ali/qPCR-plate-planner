**qPCR Plate Designer - README**

**Overview**

qPCR Plate Designer is a comprehensive web-based tool for planning, executing, and analyzing quantitative PCR (qPCR) experiments. It provides an all-in-one solution for designing 384-well plate layouts, calculating master mix volumes, recording Ct values, and performing ΔΔCt analysis with automated fold-change calculations and visualizations.
An example file (example-import.json) is included to illustrate expected input structure. Users can import it via the Import JSON button to explore sample metadata, plate layout, and ΔΔCt analysis logic.
This tool applies the 2^−ΔΔCt method for relative quantification, as described by (Livak & Schmittgen, 2001. DOI:10.1006/meth.2001.1262), adapted for CUT&RUN workflows where qPCR is used to assess enrichment at target loci.


License: CC BY-NC 4.0 — Free to use and adapt for non-commercial purposes with attribution.

**What is this tool for?**

This tool is designed for molecular biologists and researchers conducting qPCR experiments, particularly those involving:

- Multiple target genes
- Multiple experimental conditions (e.g., different treatments, antibodies, or time points)
- Multiple experimental groups (e.g., distinct cell lines or treatment conditions co-plated on the same 384-well plate, each requiring independent analysis)
- Technical replicates across 384-well plates
- Comparative gene expression analysis using the ΔΔCt method
- Primarily used to assess the success of CUT&RUN experiments and similar chromatin profiling techniques by quantifying target enrichment

**Key Features**

**1. Sample Management**

- Define samples with automatic parsing of naming convention (Name_Target_Condition)
- Assign unique colors to each sample for visual identification (do not assign the same color to multiple samples)
- Assign groups
- Organize samples by target gene, condition, role (Control/Condition) and group.

**2. Plate Layout Designer (Plate A)**

- Visual 384-well plate grid (16 rows × 24 columns)
- Click to assign samples in wells
- Color-coded legend for easy sample identification
- Real-time well count tracking per sample
- Undo/redo functionality
- Export plate layout as JPEG or PDF

**3. Master Mix Calculator**

- Track assigned wells per target gene
- Add extra wells for pipetting safety margin
- Define reagents with volumes per well
- Automatic calculation of total reagent volumes needed per target
- Separate master mix calculations for each target gene

**4. Ct Value Entry (Plate B)**

- Spreadsheet-style input grid matching the 384-well layout
- Paste support from Excel/Google Sheets (column or block paste)
- Maintains synchronization with Plate A layout

**5. ΔΔCt Analysis & Visualization**

- Automatic calculation of mean Ct values from replicates
- ΔCt calculation relative to control condition within each target
- ΔΔCt calculation relative to control target gene
- Fold-change calculation using 2^(-ΔΔCt) method
- Interactive bar chart showing fold changes
- Comprehensive summary table with all calculations
- Export analysis and charts as JPEG or PDF

**6. Data Management**

- Automatic local storage of all data
- Export entire project as JSON
- Import JSON to restore previous experiments
- Experiment metadata tracking (name, date, notes)

**How It Works**

**Step 1: Define Your Samples**

Create samples using the naming convention Name_Target_Condition (e.g., "HeLa_CCNA2_IgG"). The tool automatically extracts the target gene and condition. Assign each sample a unique color and specify whether it's a control or experimental condition and assign a group.

**Step 2: Design Your Plate Layout**

Select a sample from the color selector and click wells on Plate A to assign samples. You can assign up to 4 samples per well for multiplexed assays. The legend shows all samples and their colors.

**Step 3: Plan Your Master Mix**

The tool counts assigned wells per target automatically. Add extra wells for pipetting margin, then define your reagents (e.g., primers, SYBR Green) with per-well volumes. The calculator shows total volumes needed for each target's master mix.

**Step 4: Enter Ct Values**

After running your qPCR, paste Ct values from your instrument's export directly into Plate B. The tool accepts single values or blocks of data pasted from spreadsheets.

**Step 5: Analyze Results**

The tool automatically calculates ΔCt and ΔΔCt values and generates fold-change charts. Configure your control condition and control target gene to customize the analysis.

**Calculations Explained**

**Mean Ct**

For each sample, the tool averages Ct values across all wells assigned to that sample, accounting for technical replicates.

**ΔCt (Delta Ct)**

ΔCt = Ct(sample) - Ct(control within same target)

This normalizes expression within each target gene relative to its control condition (e.g., IgG control).

**ΔΔCt (Delta Delta Ct)**

ΔΔCt = ΔCt(target gene) - ΔCt(control target gene)

This normalizes expression across different target genes using a reference gene (e.g., housekeeping gene).

**Fold Change**

Fold Change = 2^(-ΔΔCt)

This represents the relative gene expression or enrichment of epigenetic mark level, where:

- FC = 1: No change in enrichment/expression
- FC > 1: Enrichment/Upregulation
- FC < 1: Less enriched/Downregulation

**Technical Requirements**

- Modern web browser (Chrome, Firefox, Safari, Edge)
- No installation required - runs entirely in browser
- All data stored locally in browser localStorage
- Internet connection required only for initial loading of CDN libraries

**Libraries Used**

- Chart.js for data visualization
- jsPDF for PDF export
- html2canvas for image capture

**Use Cases**

- ChIP-qPCR experiments with multiple antibodies and genomic regions
- CUT&RUN experiments to validate chromatin immunoprecipitation efficiency
- Gene expression studies with multiple conditions and time points

**License**

Created by Mahmood Mohammed Ali PhD student in the university of Grenoble Alpes (Institute of Advanced Bioscience)
