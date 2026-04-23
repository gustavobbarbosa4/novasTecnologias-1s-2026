while True:

    senha = input("Digite uma senha: ")

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    if not any(c.isdigit() for c in senha):
        print("A senha deve conter pelo menos um número.")
        continue

    if not any(c.isupper() for c in senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        continue

    break


tamanho = len(senha)
numeros = sum(c.isdigit() for c in senha)
letras = sum(c.isalpha() for c in senha)
especiais = sum(not c.isalnum() for c in senha)

if 8 <= tamanho <= 9:
    nivel = "Fraca"
elif 10 <= tamanho <= 12:
    nivel = "Média"
else:
    nivel = "Forte"


print("\nRELATÓRIO DE SEGURANÇA:")
print(f"Tamanho da senha: {tamanho}")
print(f"Letras: {letras}")
print(f"Números: {numeros}")
print(f"Caracteres especiais: {especiais}")
print(f"Nível da senha: {nivel}")