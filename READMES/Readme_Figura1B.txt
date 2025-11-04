#Figura 1B – AUDPC Analysis by Treatment

##Overview

This project contains a Python script that reads experimental data from a CSV file and generates a boxplot combined with individual data points to visualize AUDPC (Area Under Disease Progress Curve) across different treatments.

##Features

-Loads and cleans data from a .csv file
-Converts numeric values formatted with commas into floats
-Creates a boxplot + stripplot to show treatment comparisons
-Customizes style, labels, and layout for publication-ready figures
-Allows optional saving of the plot as an image file

##File Structure
├── Figura1B.csv        # Dataset used for plotting
├── script_Figura1B.py  # Python code
├── Figura1B.png        # (Optional) Saved figure output
└── README.md

##Requirements

Make sure you have the following libraries installed: pip install pandas seaborn matplotlib

##How to Use This Script

-Place the file Figura1B.csv in the same folder as the script.
-Ensure the CSV uses semicolons (;) as separators.
-Run the script in a terminal or IDE: python script_Figura1B.py
-To save the figure instead of only showing it: plt.savefig("Figura1B.png", dpi=600)

##What the Code Does – Step by Step

-Imports required libraries (pandas, seaborn, matplotlib)
-Reads the dataset and cleans column names
-Converts the audpc column from string to float (replacing commas with dots)
-Sets a clean visual theme using Seaborn
-Creates a boxplot per treatment, with a stripplot to show individual values
-Adds title, labels, and adjusts layout for a clean output

##Output

The script produces a visualization showing:
-Distribution of AUDPC values by treatment
-Differences between treatments
-Variability and individual data points