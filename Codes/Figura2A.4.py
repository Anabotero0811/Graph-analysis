import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

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

palette = sns.color_palette("coolwarm", n_colors=len(tabla.columns)).as_hex()

tabla_reset = tabla.reset_index().melt(id_vars="Frequency", var_name="Phylum", value_name="Abundance")

fig = px.bar(
    tabla_reset,
    x="Frequency",
    y="Abundance",
    color="Phylum",
    category_orders={"Phylum": orden},
    color_discrete_sequence=palette,
    title="Abundancia relativa de filos bacterianos"
)

fig.update_layout(
    title=dict(
        text="Abundancia relativa de filos bacterianos",
        x=0.5,
        xanchor='center',
        font=dict(size=18, family="Arial", color="black")
    ),
    barmode='stack',
    yaxis_title="Abundancia relativa (%)",
    xaxis_title="Frecuencia de aplicación del cóctel de fagos",
    legend_title="Phylum",
    template="simple_white"
)

fig.update_yaxes(tickformat=".0%")

fig.show()
fig.write_html("Figura2A.4_interactiva.html")
plt.show()
