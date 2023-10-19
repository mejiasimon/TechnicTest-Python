numbers = [1, 2, 3, 4, 5]

# Funciones lambda para operaciones
square = lambda x: x ** 2
cube = lambda x: x ** 3
is_even = lambda x: x % 2 == 0

# Usar map con las funciones lambda
squared_numbers = list(map(square, numbers))
cubed_numbers = list(map(cube, numbers))
even_numbers = list(filter(is_even, numbers))

# Imprimir resultados
print("Squared Numbers:", squared_numbers)
print("Cubed Numbers:", cubed_numbers)
print("Even Numbers:", even_numbers)