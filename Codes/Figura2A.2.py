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

tabla_melt = tabla.reset_index().melt(id_vars="Frequency", var_name="Phylum", value_name="Abundance")
sns.barplot(data=tabla_melt, x="Frequency", y="Abundance", hue="Phylum", palette="Paired")
plt.title("Abundancia relativa de filos bacterianos", fontsize=14, weight="bold")
plt.ylabel("Abundancia relativa", fontsize=12)
plt.xlabel("Frecuencia de aplicación del cóctel de fagos", fontsize=12)
plt.legend(title="Phylum", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=9)
sns.despine()
plt.tight_layout()
plt.savefig("Figura2A.2.png", dpi=600)
plt.show()


