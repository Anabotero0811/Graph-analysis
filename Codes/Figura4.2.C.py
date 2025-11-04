import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

tukey = pairwise_tukeyhsd(
    endog=data['pathogen'],
    groups=data['Treatment'],
    alpha=0.05
)
print("\n=== Tukey HSD ===")
print(tukey)

letters_map = {'Control': 'a', 'P': 'b', 'N': 'b', 'PN': 'c'}

sns.set_style("whitegrid")
plt.rcParams["font.family"] = "DejaVu Sans"

plt.figure(figsize=(6, 5))
ax = sns.stripplot(
    data=data,
    x="Treatment",
    y="pathogen",
    hue="Treatment",
    palette="pastel",
    dodge=False,
    size=6,
    jitter=True,
    legend=False
)

means = data.groupby('Treatment')['pathogen'].mean().reindex(['Control', 'P', 'N', 'PN'])
ax.plot(range(len(means)), means, 'k_', markersize=10, markeredgewidth=1.5)

for i, treatment in enumerate(['Control', 'P', 'N', 'PN']):
    y = data.loc[data['Treatment'] == treatment, 'pathogen'].max() + 0.15
    ax.text(
        i, y, letters_map[treatment],
        ha='center', va='bottom',
        fontsize=10,
        fontweight='normal'
    )

plt.title("Pathogen density under different treatments (Dot Plot)",
          fontsize=11, pad=20)
ax.set_xlabel("Treatment", fontsize=10)
ax.set_ylabel("Pathogen density (Log10 CFU g⁻¹ dW)", fontsize=10)
sns.despine()
plt.tight_layout()
plt.savefig("Figura4C.2.png", dpi=600)
plt.show()
