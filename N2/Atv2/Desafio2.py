import pandas as pd
df = pd.read_csv(
    "funcionarios.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A","-"]
)

print("-------Tarefa 1-------")
valores_nulos = df.isnull().sum()
print(f"Quantidade de valores nulos por coluna:\n{valores_nulos}")
print()

print("-------Tarefa 2-------")
df = df.dropna(subset=['salario'])
print(f"média das idades do dataframe {df['idade'].mean()}\n")
df['idade'] = df['idade'].fillna(df['idade'].mean())
print(df)

print("\n-------Tarefa 3-------")
df['data_admissao'] = pd.to_datetime(df['data_admissao'])

data_atual = pd.to_datetime('today').normalize()

df['anos_empresa'] = (
    (data_atual - df['data_admissao']) / pd.Timedelta(days=365.25)
    ).round(2)

media_salario_departamento = df.groupby(['departamento'])['salario'].transform('mean')

salarios_abaixo_media = df[
    (df['anos_empresa'] < 5) &
    (df['salario'] < media_salario_departamento)
    ]
print(salarios_abaixo_media)
