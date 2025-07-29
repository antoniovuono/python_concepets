# IMC = peso / (altura x altura)

name = input("Qual o seu nome ?")
age = int(input("Digite a sua idade: "))
height = float(input("Digite sua altura: "))
weight = float(input("Digite o seu peso: "))

imc = weight / height * height

print("O seu IMC é de", imc, "%")
