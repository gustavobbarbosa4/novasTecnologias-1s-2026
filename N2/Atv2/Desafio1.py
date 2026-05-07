
import pandas as pd
df = pd.read_csv(
    "vendas.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A","-"]
)

print("-------Tarefa 1-------")
print(df.head(10))
print(df.info())

print("-------Tarefa 2-------")
df["total_venda"] = df["quantidade"] * df["preco_unitario"]

print("-------Tarefa 3-------")
eletronicos_mais_vendidos = df.query("categoria == 'Eletrônicos' and total_venda > 1000")
print(eletronicos_mais_vendidos)

print("-------Tarefa 4-------")
media_total_venda_por_cidade = (
    df.groupby('cidade')['total_venda']
      .mean()
      .sort_values(ascending=False)
)
print(media_total_venda_por_cidade)