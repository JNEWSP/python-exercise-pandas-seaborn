import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="dark")
url = 'https://api.rawg.io/api/games?key=a8d881fe00b74040a74b8959e7cefc54'
data = None

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Test 1 - Ok")
except requests.exceptions.HTTPError as errh:
    print(f"Erro: {errh}")
except requests.exceptions.RequestException as errh:
    print(f"Erro: {errh}")

try:
    games = data['results']
    df = pd.DataFrame(games)
    print("Test 2 - Ok")
except:
    print("Erro")

try:
    df_use = df[["name","released","ratings_count"]].copy()
    df_use["released"] = pd.to_datetime(df_use["released"], errors="coerce")
    df_use["year"] = df_use["released"].dt.year
    print("Test 3 - Ok")
except:
    print("Erro")

plt.figure(figsize=(9,5))

ax = sns.scatterplot(
    data = df_use,
    x="ratings_count",
    y="year"
)

for _, row in df_use.iterrows():
    ax.text(
        row["ratings_count"],
        row["year"],
        row["name"],
        fontsize=8,
        alpha=1
    )

plt.xlabel("Quantidade de avaliações")
plt.ylabel("Ano de lançamento")
plt.title("Avaliações vs Ano de lançamento")

plt.show()