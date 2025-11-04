import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv("Figura4C.csv", sep=";", engine="python")
data.columns = data.columns.str.strip()

for col in ['Nocardioides', 'Streptomyces', 'pathogen']:
    data[col] = data[col].astype(str).str.replace(',', '.').astype(float)

mapping = {0: 'Control', 1: 'P', 2: 'N', 3: 'PN'}
data['Treatment'] = data['trt'].map(mapping)

model = ols('pathogen ~ C(Treatment)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\n=== ANOVA ===")
print(anova_table)

tukey = pairwise_tukeyhsd(endog=data['pathogen'],
                          groups=data['Treatment'],
                          alpha=0.05)
print("\n=== Tukey HSD ===")
print(tukey)

letters_map = {'Control': 'a', 'N': 'b', 'P': 'b', 'PN': 'c'}

sns.set_style("white")
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.linewidth"] = 1

plt.figure(figsize=(5, 4))
ax = sns.boxplot(
    data=data,
    x='Treatment',
    y='pathogen',
    hue='Treatment',
    palette='pastel',
    width=0.8,
    fliersize=0,
    linewidth=1,
    legend=False
)

sns.stripplot(
    data=data,
    x='Treatment',
    y='pathogen',
    color='black',
    size=3,
    jitter=True
)

for i, treatment in enumerate(['Control', 'P', 'N', 'PN']):
    y = data.loc[data['Treatment'] == treatment, 'pathogen'].max() + 0.15
    ax.text(
        i, y, letters_map[treatment],
        ha='center', va='bottom',
        fontsize=10,
        fontweight='normal'
    )


plt.title("Pathogen density in the rhizosphere under different treatments",
          fontsize=10, pad=20)
ax.set_xlabel("Treatment", fontsize=10)
ax.set_ylabel("Pathogen density (Log10 CFU g⁻¹ dW)", fontsize=10)

sns.despine()
plt.tight_layout()
plt.savefig("Figura4C.png", dpi=600)
plt.show()
