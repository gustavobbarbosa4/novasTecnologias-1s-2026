import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "bugs_dataset.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A", "-"]
)

# negativos viram 0
df.loc[df['Tempo_Resolucao_Horas'] < 0, 'Tempo_Resolucao_Horas'] = 0

# 0 vira NaN
df['Tempo_Resolucao_Horas'] = df['Tempo_Resolucao_Horas'].replace(0, np.nan)

# preencher NaN com média
df['Tempo_Resolucao_Horas'] = df['Tempo_Resolucao_Horas'].fillna(
    df['Tempo_Resolucao_Horas'].mean()
)

# média por módulo
tempo_medio_resolucao_por_modulo = df.groupby(
    'Módulo',
    as_index=False
)['Tempo_Resolucao_Horas'].mean()

# ordenar do maior para o menor
tempo_medio_resolucao_por_modulo = tempo_medio_resolucao_por_modulo.sort_values(
    by='Tempo_Resolucao_Horas',
    ascending=False
)

# gráfico
plt.figure(figsize=(8,5))

plt.bar(
    tempo_medio_resolucao_por_modulo['Módulo'],
    tempo_medio_resolucao_por_modulo['Tempo_Resolucao_Horas']
)

plt.title('Tempo Médio de Resolução por Módulo')
plt.xlabel('Módulo')
plt.ylabel('Tempo Médio (horas)')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()