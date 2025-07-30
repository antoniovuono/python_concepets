# Exercício: Cadastro de Carros
# 1. Permitir ao usuário cadastrar vários carros.
# 2. Armazenar cada carro como um dicionário.
# 3. Guardar todos os carros em uma lista.
# 4. Exibir os dados no final.

cars = []

car_quantity = int(input("Quantos carros você pretende cadastrar ?"))

for i in range(car_quantity):
    print(f"\nCadastro do carro {i+1}")

    brand = input("Marca: ")
    model = input("Modelo:  ")
    year =  int(input("Ano: "))
    color = input("Cor: ")

    car = {
        "marca": brand,
        "modelo": model,
        "ano": year,
        "cor": color
    }

    cars.append(car)


# Exibindo lista:
print("\n🚘 Carros cadastrados:")

for car in cars:
    print(car)
