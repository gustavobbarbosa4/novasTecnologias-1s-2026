import numpy as np

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

# brilho médio geral
brilho_medio = np.mean(imagem)

# médias por linha
media_linhas = np.mean(imagem, axis=1)

# médias por coluna
media_colunas = np.mean(imagem, axis=0)

# linha mais escura
linha_mais_escura = np.argmin(media_linhas)

# limiarização
imagem_binaria = imagem.copy()
imagem_binaria[imagem >= 128] = 255
imagem_binaria[imagem < 128] = 0

print("Brilho medio geral:", brilho_medio)
print("Media por linha:", media_linhas)
print("Media por coluna:", media_colunas)
print("Linha mais escura:", linha_mais_escura + 1)

print("\nImagem binaria:")
print(imagem_binaria)