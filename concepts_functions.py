# Funçoes permitem que você crie um bloco de código que execute uma tarefa

# Definindo funções

def greetings():
    print("Bem vindo a aula sobre funções!")

greetings()

# Funções com retorno e parâmetros

def sum(a: int, b: int):
    return a + b

print(sum(1, 1))


# Escopo de variáveis: Escopo é o que está dentro da função

def mostrar_idade():
    idade = 30
    print("A idade é", idade)


mostrar_idade()

# Verifique se o número é PendingDeprecationWarning

def even_odd(number: int):
    if(number % 2 == 0):
        print("O número é par")
    else:
        print("O número é impar")


even_odd(2)
