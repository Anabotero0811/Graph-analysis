#Figura 2A – Relative Abundance of Bacterial Phyla

##Overview

This project contains a Python script that analyzes microbial community composition and visualizes the relative abundance of bacterial phyla under different phage treatment frequencies. The output is a stacked bar chart, allowing easy comparison between treatments.

##Features

-Loads and cleans data from a .csv file
-Renames columns for clarity (phylum → Phylum, etc.)
-Converts abundance values from text (with commas) to numeric format
-Creates a pivot table, calculates relative abundance (%), and orders phyla
-Generates a stacked bar plot showing phylum composition per treatment
-Saves the figure as Figura2A.png in high resolution (600 dpi)

##File Structure

├── Figura2A.csv        # Input dataset
├── script_Figura2A.py  # Python script
├── Figura2A.png        # (Optional) Output figure
└── README.md

##Requirements

Install the necessary libraries using: pip install pandas seaborn matplotlib

##How to Use the Script

-Place Figura2A.csv in the same directory as the script.
-Make sure the CSV uses ; as separator and contains the columns: phylum, trt, value
-Run the script from terminal or an IDE: python script_Figura2A.py
-If you want to save the figure, keep the line: plt.savefig("Figura2A.png", dpi=600)

##What the Script Does

-Loads the dataset using pandas
-Cleans and renames columns (Phylum, Frequency, Abundance)
-Converts abundance values from string to float
-Creates a pivot table of mean abundance per treatment and phylum
-Normalizes each treatment row (relative abundance per phylum)
-Orders phyla for consistent legend display
-Generates a stacked bar chart using matplotlib and seaborn
-Adds titles, labels, legend, and saves the figure

#Output Description

The resulting stacked bar plot shows:
-The relative contribution of each bacterial phylum
-How phage application frequency affects microbial community structure
-Phyla are color-coded, with legend placed outside for clarity