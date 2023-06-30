# Los conjuntos se utilizan para almacenar varios elementos en una sola variable.

""" Set es uno de los 4 tipos de datos incorporados en Python 
que se utilizan para almacenar colecciones de datos, los otros 
3 son List , Tuple y Dictionary , todos con diferentes calidades y usos.
 """
# Un conjunto es una colección desordenada , inmutable y no indexada.
# No se pueden modificar, pero puede eliminar elementos y agregar elementos nuevos.

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)


