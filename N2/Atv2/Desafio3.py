import pandas as pd
df1 = pd.read_csv(
    "estoque_atual.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A", "-"]
)
df2 = pd.read_csv(
    "produtos.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A", "-"]
)
df3 = pd.read_csv(
    "vendas_mensal.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A", "-"]
)

print("-------Tafera 1-------")
df_temp = pd.merge(df1, df2, on="produto_id", how="inner")
df  = pd.merge(df_temp, df3, on="produto_id", how="inner")
print(f"{df}\n")

print("-------Tafera 2-------")
df['custo_total_estoque'] = df['quantidade'] * df['preco_custo']
df['valor_venda_mes'] = df['quantidade_vendida'] * df['preco_custo'] * 1.5
print(f"{df}\n")

print("-------Tafera 3-------")
produtos_zerados_ou_negativos = df