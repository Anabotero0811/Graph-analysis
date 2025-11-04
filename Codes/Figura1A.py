import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Figura_1A.csv", sep=';')

df.columns = df.columns.str.strip()
df.rename(columns={'trt': 'Tratamiento', 'day': 'Día', 'index': 'Índice'}, inplace=True)

df["Índice"] = df["Índice"].astype(str).str.replace(',', '.').astype(float).round(2)

sns.set_theme(style="whitegrid", context="talk")
palette = sns.color_palette("colorblind")

plt.figure(figsize=(7.5, 5), dpi=300)

sns.lineplot(
    data=df,
    x="Día",
    y="Índice",
    hue="Tratamiento",
    marker="o",
    linewidth=2.2,
    markersize=5,
    alpha=0.95,
    palette=palette,
    err_style="band",
    err_kws={"alpha": 0.15}
)

plt.title("Figura 1A – Evolución del índice según tratamiento", fontsize=14, weight="bold", pad=15)
plt.xlabel("Día del experimento", fontsize=12)
plt.ylabel("Índice promedio", fontsize=12)
plt.ylim(0, 1.05)
plt.xlim(df["Día"].min() - 0.5, df["Día"].max() + 0.5)

plt.legend(
    title="Tratamiento",
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0, 0.98),
    fontsize=10,
    title_fontsize=12,
)

sns.despine()
plt.tight_layout()
#plt.savefig("Figura1A", dpi=600)
plt.show()
