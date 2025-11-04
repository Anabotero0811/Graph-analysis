import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Figura1B.csv", sep=';')

df.columns = df.columns.str.strip()
df["audpc"] = df["audpc"].astype(str).str.replace(',', '.').astype(float)

sns.set_theme(style="whitegrid", context="talk")
palette = sns.color_palette("Set2", n_colors=df["trt"].nunique())

plt.figure(figsize=(6.5, 5), dpi=300)

sns.boxplot(
    data=df,
    x="trt",
    y="audpc",
    hue="trt",
    legend=False,
    palette=palette,
    width=0.5,
    fliersize=0,
    linewidth=1.3
)

sns.stripplot(
    data=df,
    x="trt",
    y="audpc",
    color="black",
    alpha=0.7,
    size=5,
    jitter=True
)

plt.title("Figura 1B – AUDPC según tratamiento", fontsize=14, weight="bold", pad=15)
plt.xlabel("Tratamiento", fontsize=12)
plt.ylabel("AUDPC", fontsize=12)

sns.despine()
plt.tight_layout()
#plt.savefig("Figura1B.png", dpi=600)
plt.show()
