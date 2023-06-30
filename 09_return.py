# Valores por defecto en los argumentos
# y multiples returns
def find_volume(length, width, depth):
  return length * width * depth


result = find_volume(10, 20, 30)

print(result)

def find_volume(length = 1, width = 1, depth = 1):
  return length * width * depth, width, 'hola'


result = find_volume(width = 10)

print(result[0])


result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)
