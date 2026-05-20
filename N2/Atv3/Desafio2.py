import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# leitura do dataset
df = pd.read_csv("commits_dataset.csv")

# converter coluna Data para datetime
df['Data'] = pd.to_datetime(df['Data'])

# título
st.title("Dashboard do Engenheiro de Qualidade")

# sidebar
desenvolvedores = df['Desenvolvedor'].unique()

dev_selecionado = st.sidebar.radio(
    "Selecione o Desenvolvedor",
    desenvolvedores
)

# filtrar dataframe
df_dev = df[df['Desenvolvedor'] == dev_selecionado]

# total de linhas adicionadas
total_linhas = df_dev['Linhas_Adicionadas'].sum()

st.subheader(f"Desenvolvedor Selecionado: {dev_selecionado}")

st.metric(
    "Total de Linhas Adicionadas",
    total_linhas
)

# agrupar bugs por data
bugs_por_data = df_dev.groupby(
    'Data',
    as_index=False
)['Bugs_Gerados'].sum()

# gráfico
fig, ax = plt.subplots(figsize=(8,4))

ax.plot(
    bugs_por_data['Data'],
    bugs_por_data['Bugs_Gerados'],
    marker='o'
)

ax.set_title("Evolução Temporal de Bugs")
ax.set_xlabel("Data")
ax.set_ylabel("Bugs Gerados")

plt.xticks(rotation=45)

st.pyplot(fig)

# botão extra
if st.button("Mostrar Dev com Maior Média de Bugs por Commit"):

    media_bugs = df.groupby(
        'Desenvolvedor'
    )['Bugs_Gerados'].mean()

    pior_dev = media_bugs.idxmax()
    maior_media = media_bugs.max()

    st.warning(
        f"{pior_dev} possui a maior média de bugs por commit: {maior_media:.2f}"
    )