# Mostre a tabuada do número de 1 a 10

number = int(input("Qual número você quer saber a tabudada ?"))

for i in range(1, 10):
   result = number * i
   print(number, "x", i, "=", result)
