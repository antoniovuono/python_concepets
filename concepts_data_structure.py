# Principais estruturas de dados embutidas em Python:

# list: Tem o objetivo de guardar vários valores.
# Equivalente a um array: Um conjunto de valores armazenados em uma variável.

frutas = ["maçã", "banana", "laranja"]

# Operações comuns:
# append: Adiciona um item

frutas.append("uva")

# remove: remover um item
frutas.remove("maçã")

print(frutas)

# Acessar item por index

frutas[2]

# for: Percorrer uma lista

for fruta in frutas:
    print(fruta)

# tamanho da lista

len(frutas)

# dict: Armazena dados no formato chave e valor
# parecido com o JSON no JS

person = {
   "name": "Antonio",
   "age": 30,
   "height": 1.78
}

print(person)

# manipulando estrutura
# Acessando dado específico
print(person['name'])

# Adicionando nova chave/valor

person["email"] = "antoniosvuono@gmail.com"

print(person)

# Lista com 3 carros
# carros é uma lista de 3 elementos.
# Cada elemento da lista é um dicionário com os dados de um carro.
carros = [
    {"marca": "Toyota", "modelo": "Corolla"},
    {"marca": "Ford", "modelo": "Ka"},
    {"marca": "Honda", "modelo": "Civic"}
]
