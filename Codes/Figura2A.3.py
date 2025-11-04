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

plt.figure(figsize=(8,6))
sns.heatmap(tabla[orden].T, cmap="Blues", norm=plt.matplotlib.colors.LogNorm(),
            cbar_kws={'label': 'Abundancia relativa (log)'})

plt.title("Abundancia relativa de filos bacterianos", fontsize=14, weight="bold")
plt.xlabel("Frecuencia de aplicación del cóctel de fagos", fontsize=12)
plt.ylabel("Phylum", fontsize=12)
plt.tight_layout()
plt.savefig("Figura2A.3.png", dpi=600)
plt.show()


