#Figure 4C: Pathogen Density Under Treatments

##Figure Overview

This script generates Figure 4C, which analyzes and visualizes the density of the pathogen in the rhizosphere under different treatments using both statistical analysis (ANOVA + Tukey HSD) and a boxplot with significance letters.

##Dataset

-Input file: Figura4C.csv
-Columns used: Nocardioides, Streptomyces, pathogen → converted from comma to decimal (float)
-trt → numeric treatment codes (0, 1, 2, 3) are mapped to:
	.Code Treatment
	.0	Control
	.1	P
	.2	N
	.3	PN
	
##Type of Analysis

This script performs:
-One-way ANOVA to evaluate differences in pathogen abundance among treatments.
-Tukey HSD post-hoc test to identify pairwise significant differences.
-Assignment of significance letters (a, b, c) to each treatment group, based on Tukey results.

##Type of Plot

-Boxplot with jittered data points (stripplot)
-X-axis: Treatment groups
-Y-axis: Pathogen density (Log10 CFU g⁻¹ dry weight)
-Significance letters are displayed above each box, indicating statistical differences.

##Output File Generated

-Figura4C.png: Boxplot of pathogen density with statistical group letters

##Statistical Summary Printed in Console

The script prints:
-ANOVA table → F-value and p-value to detect overall differences.
-Tukey HSD results → Pairwise comparisons & significance.

##Key Libraries Used

-pandas: data processing
-statsmodels: ANOVA and Tukey analysis
-seaborn & matplotlib: visualization
-statsmodels.formula.api (ols): statistical model fitting

##Interpretation of the Figure

-Treatments are compared to see how they affect pathogen density in the rhizosphere.
-Lower values indicate better suppression of the pathogen.
-Different letters above the boxes (e.g., a, b, c) mean the groups are statistically different (p < 0.05).