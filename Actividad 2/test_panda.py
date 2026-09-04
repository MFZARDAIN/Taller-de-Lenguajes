import pandas as pd
import matplotlib.pyplot as plt

# https://www.kaggle.com/datasets/zkskhurram/programming-language-tiobe-index-february-2026

index = pd.read_csv("data/archive/tiobe_index_feb_2026.csv")
history = pd.read_csv("data/archive/tiobe_historical_yearly.csv")
hof = pd.read_csv("data/archive/tiobe_hall_of_fame.csv")

# print(index.head(5))

history.plot(x="Year", marker="o", colormap="turbo").invert_yaxis()

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('top.png', bbox_inches='tight')
# plt.show()

top = index[index["Rating_Pct"] > 2]
#top = index.head(5)

top.set_index("Language").plot.bar(y="Rating_Pct", legend=False, colormap="turbo")

plt.title("Cuota de Mercado - Grafico por Barras")
plt.savefig('mercado1.png', bbox_inches='tight')
# plt.show()

top.set_index("Language").plot.pie(y="Rating_Pct", legend=False, colormap="turbo", autopct="%1.1f%%")

plt.title("Cuota de Mercado - Grafico Porciones")
plt.savefig('mercado2.png', bbox_inches='tight')
# plt.show()

paradigma_var = index[["Paradigm", "Typing"]]
# print(paradigma_var)

print(paradigma_var["Paradigm"].value_counts())
print(paradigma_var["Typing"].value_counts())

# paradigma_var.plot()
# plt.title("Paradigma y Almacenamientos de Variables")
# plt.savefig('paradigma_var.png', bbox_inches='tight')
# plt.show()