# 1. Variáveis e tipos de dados básicos

name = "Antonio" # str()
age = 30 # int()
height = 1.78 # float()
python_student = True # bool()

# Atribuindo valor a várias variáveis:
x,y,z = 2,4,6

# Função print(): Exibe um valor no console.

print("Olá mundo, bem vindo ao primeiro contato com Pyhton")
print("Nome:", name)
print("Idade:", age)

# Rodar um arquivo: Dentro da pasta onde o arquivo se encontra, rode:
# python3 concepts.py

# Função Input: Lê uma informação digitada pelo usuário e retorna uma str.

brother_name = input("Digite o nome do seu irmão: ")
brother_age = int(input("Digite a idade do seu irmão: "))
brother_height = float(input("Digite a altura do seu irmão: "))


# Dúvidas:
# 1. Qual o pattern recomendado para trabalhar com nomenclatura de variáveis ?
# Resposta: Sneak case
#  - todas as letras minúsculas.
#  - palavras separadas por underline (_)

dog_name = "Scooby"
has_tutor = True

# 2. Como atribuir um valor a uma variável ?
