# Una variable solo está disponible desde dentro de la región en la que se crea. Esto se llama scope.
# Es  deiecr, se respetan las variables locales y globales

price = 100 # global
# result = 200

def increment():
  price = 200
  result = price + 10
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
# print(result)