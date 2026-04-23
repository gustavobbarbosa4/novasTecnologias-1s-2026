nome = input("Qual o seu nome? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura?(m) "))

def calcIMC(peso, altura):
   return peso / (altura ** 2)
   
def classIMC(imc):   
    print(f"Seu IMC é: {round(imc, 2)}")
    if imc < 18.5:
        return("Abaixo do peso!")
    elif 18.5 <= imc <= 24.9:
        return("Peso normal")
    elif 25 <= imc <= 29.9:
        return("Sobrepeso!")
    else:
        return("Obesidade")

imc = calcIMC(peso, altura)

print(f"\nNome: {nome}")
print(f"Peso: {peso}")
print(f"Altura: {altura}")
print(f"Classificação: {classIMC(imc)}")
