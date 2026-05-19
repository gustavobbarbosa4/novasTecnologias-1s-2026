fraseUsuario = input("Digite uma frase: ")
fraseUsuario = fraseUsuario.lower().strip()

palavras = fraseUsuario.split()

cont = {}

for palavra in palavras:
    if palavra in cont:
        cont[palavra] += 1
    else:
        cont[palavra] = 1
        
total_palavras = len(palavras)

total_unicas = len(cont)

maior = 0
palavra_mais_frequente = ""

for palavra, quantidade in cont.items():
    if quantidade > maior:
        maior = quantidade
        palavra_mais_frequente = palavra
        
repetidas = []

for palavra, quantidade in cont.items():
    if quantidade > 1:
        repetidas.append(palavra)
        
print("\n--- Relatório ---")

print(f"Total de palavras: {total_palavras}")
print(f"Total palavras únicas: {total_unicas}")

print("\nPalavras que se repetem:")
if repetidas:
    for palavra in repetidas:
        print(f"- {palavra} ({cont[palavra]} vezes)")
else: 
    print("Nenhuma palavra repetida!")
    
print(f"\nPalavra mais frequente: {palavra_mais_frequente} ({maior} vezes)")
        