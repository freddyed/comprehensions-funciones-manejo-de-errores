#Para permitir que una función devuelva un valor, use la declaración "return"

def suma_with_range(min, max):
  print(min, max)
  sum = 0

  for x in range(min, max):
    sum += x
  return sum


suma = suma_with_range(1, 10)

print(suma)

suma2 = suma_with_range(suma, suma + 100)

print(suma2)