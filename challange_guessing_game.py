# Defina um número secreto (ex: 7)
# Peça ao usuário para tentar adivinhar até acertar
# Dê dicas: "maior" ou "menor"

print("🎯 Jogo de adivinhação: tente adivinhar o número da sorte!")

secret_number = 7
user_number = int(input("Digite um número: "))

while user_number != secret_number:
    if user_number > secret_number:
       user_number = int(input("Tente um outro número: (Dica: O número é menor)", ))
    else:
       user_number = int(input("Tente um outro número: (Dica: O número é maior)", ))

# Quando sair do loop, o número foi acertado
print("🎉 Parabéns, você acertou!")
