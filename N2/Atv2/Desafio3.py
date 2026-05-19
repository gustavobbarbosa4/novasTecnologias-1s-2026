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

quantidade_produtos = df1.groupby('produto_id', as_index=False)['quantidade'].sum()
vendas_produto = df3.groupby('produto_id', as_index=False)['quantidade_vendida'].sum()

print("-------Tafera 1-------")
print("Tarefa ignorada kkkkk")

print("-------Tafera 2-------")
df_tarefa_2a = pd.merge(quantidade_produtos, df2, on='produto_id', how='inner')
df_tarefa_2b = pd.merge(quantidade_produtos, df3, on='produto_id', how='inner')
df_tarefa_2a['custo_total_estoque'] = df_tarefa_2['quantidade'] * df_tarefa_2['preco_custo']

print("-------Tafera 3-------")
produtos_zerados_ou_negativos = df[df['quantidade'] < df['quantidade_vendida']]

