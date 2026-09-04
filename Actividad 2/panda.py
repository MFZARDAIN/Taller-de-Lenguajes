import pandas as pd
import matplotlib.pyplot as plt

# Data Set Popularidad Lenguajes desde Julio de 2004 a Diciembre 2024
# https://www.kaggle.com/datasets/muhammadkhalid/most-popular-programming-languages-since-2004

data = pd.read_csv("data/archive2/Popularity of Programming Languages from 2004 to 2024.csv")

# print(data.head(10))

#Grafico Popularidad Python
data.plot(x="Date", y="Python", legend=False, colormap="turbo")

plt.title("Grafico Popularidad Python")
plt.xticks(rotation=45)
plt.savefig('his_py.png', bbox_inches='tight')
# plt.show()

#Grafico Popularidad Java
data.plot(x="Date", y="Java", legend=False, colormap="turbo")

plt.title("Grafico Popularidad Java")
plt.xticks(rotation=45)
plt.savefig('his_ja.png', bbox_inches='tight')
#plt.show()

#Grafico Popularidad C/C++
data.plot(x="Date", y="C/C++", legend=False, colormap="turbo")

plt.title("Grafico Popularidad C/C++")
plt.xticks(rotation=45)
plt.savefig('his_c.png', bbox_inches='tight')

#Grafico Popularidad JavaScript
data.plot(x="Date", y="JavaScript", legend=False, colormap="turbo")

plt.title("Grafico Popularidad JavaScript")
plt.xticks(rotation=45)
plt.savefig('his_js.png', bbox_inches='tight')

#Grafico Popularidad Python vs Java
data.plot(x="Date", y=["Java", "Python"], colormap="turbo")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Grafico Popularidad Python vs Java")
plt.xticks(rotation=45)
plt.savefig('his_ja_VS_py.png', bbox_inches='tight')
# plt.show()

#Grafico Popularidad Python vs Java vs C/C++ vs JavaScript
data.plot(x="Date", y=["Java", "Python", "C/C++", "JavaScript"], colormap="turbo")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Grafico Popularidad Python vs Java vs C/C++ vs JavaScript")
plt.xticks(rotation=45)
plt.savefig('his_versus.png', bbox_inches='tight')
# plt.show()

#Grafico Popularidad Top 30
data.plot(x="Date", colormap="turbo")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Grafico Popularidad")
plt.xticks(rotation=45)
plt.savefig('his_all.png', bbox_inches='tight')
# plt.show()

dataPy = data[["Date", "Python"]]

dataJava = data[["Date", "Java"]]

print(dataPy[data["Python"] > 20])

print(dataJava[data["Java"] > 20])