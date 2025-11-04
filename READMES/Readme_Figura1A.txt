#Figure 1A – Disease Index Evolution Plot

##Overview
- This repository contains a Python script that generates **Figure 1A**, which visualizes the evolution of a disease index over time under different treatments.
- The script uses **Pandas** for data processing and **Seaborn/Matplotlib** for data visualization.
- It is designed for academic and scientific purposes and can be easily adapted to similar experimental datasets.

---

##Data Input
- The script loads a CSV file named **`Figura_1A.csv`**.
- Column names are cleaned and standardized as follows:
  - `trt` → **Treatment**
  - `day` → **Day**
  - `index` → **Index**
- Numeric values with commas are converted to decimals (e.g., `"0,45"` → `0.45`) to ensure data consistency.

---

##What the Script Does
- Creates a **line plot with markers** showing the evolution of the disease index across treatments and days.
- Uses a **colorblind-friendly palette** for accessibility.
- Adds the following custom features:
  - Error bands (`err_style="band"`)
  - Title, axis labels, and clean font styling
  - Custom limits on x and y axes
  - Legend positioned in the top-left corner
  - Removes the top and right spines (`sns.despine()`)
- The plot is displayed on screen and can optionally be saved as a high-resolution image.

---

##Requirements
Install the required libraries using:

```bash
pip install pandas seaborn matplotlib

##How to Run

Place the file Figura_1A.csv in the same folder as the script.

Run the script using: python figura1A.py

##Output

A publication-ready line chart titled: "Figure 1A – Evolution of the index by treatment"
You can save the figure by uncommenting the following line in the script: plt.savefig("Figura1A", dpi=600)

#Notes

-This plot is suitable for thesis projects, research papers, or academic presentations.
-You can customize colors, fonts, titles, or export formats as needed.
-Contributions, forks, and improvements are always welcome!