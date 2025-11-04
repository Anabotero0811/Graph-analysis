import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Figura2A.csv", sep=";", engine="python")
df = df.rename(columns={"phylum": "Phylum", "trt": "Frequency", "value": "Abundance"})
df["Abundance"] = df["Abundance"].astype(str).str.replace(",", ".").astype(float)

tabla = (
    df.pivot_table(values="Abundance", index="Frequency", columns="Phylum", aggfunc="mean", fill_value=0)
    .apply(lambda x: x / x.sum(), axis=1)
)

orden = ['Ralstonia', 'Proteobacteria', 'Gemmatimonadota', 'Actinobacteriota',
         'Acidobacteriota', 'Bacteroidota', 'Chloroflexi', 'Firmicutes', 'Myxococcota', 'Others']
orden = [p for p in orden if p in tabla.columns] + [p for p in tabla.columns if p not in orden]

tabla[orden].plot(kind="bar", stacked=True, figsize=(8,6), width=0.85,
                  color=sns.color_palette("Paired", len(tabla.columns)))

plt.title("Abundancia relativa de filos bacterianos", fontsize=14, weight="bold", pad=15)
plt.xlabel("Frecuencia de aplicación del cóctel de fagos", fontsize=12)
plt.ylabel("Abundancia relativa", fontsize=12)
plt.ylim(0, 1.05)
plt.xticks(rotation=0)
plt.legend(title="Phylum", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=9)
sns.despine()
plt.tight_layout()
plt.savefig("Figura2A.png", dpi=600)
plt.show()
