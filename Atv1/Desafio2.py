NUMERO_SECRETO = 1000000
MAX_TENTATIVAS = 5
cont = 1

print("ADIVINHE O NÚMERO\n:")

while cont <= MAX_TENTATIVAS:
    
    tentativa = int(input(f"\nTentativa {cont}/{MAX_TENTATIVAS}: "))
    
    if tentativa < NUMERO_SECRETO:
        print(f"Muito baixo! Tente maior")
    
    elif tentativa > NUMERO_SECRETO:
        print(f"Muito alto! Tente menor")

    else:
        print(f"Correto!")
        break
        
    cont += 1

if tentativa != NUMERO_SECRETO:
    print("\nVocê perdeu!")