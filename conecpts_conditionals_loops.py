# Estruturas de decisões: if, elif, elese

age = int(input("Entre com sua idade: "))

if age >= 18:
    print("Maior de idade")
elif age <= 13:
    print("Criança")
else:
    print("Adolescente")

# Laço for (repetição controlada): Usamos for com objetos iteráveis, como range(), listas, strings etc.

for i in range(5):
    print(i)

# Laço while (repetição condicional): Roda enquanto a condição for verdadeira.

num = 0

while num < 5:
    print("Número", num)
    num += 1
