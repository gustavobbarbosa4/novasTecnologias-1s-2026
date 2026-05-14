import pandas as pd
import numpy as np

df = pd.read_csv(
    "bugs_dataset.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A","-"]
)

df.loc[df['Tempo_Resolucao_Horas'] < 0, 'Tempo_Resolucao_Horas'] = 0
df.replace(0, np.nan, inplace=True)

df['Tempo_Resolucao_Horas'] = df['Tempo_Resolucao_Horas'].fillna(df['Tempo_Resolucao_Horas'].mean())

tempo_medio_resolucao_por_modulo = df.groupby('Módulo', as_index=False)['Tempo_Resolucao_Horas'].mean()