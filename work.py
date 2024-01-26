def aplicar_operacion(funcion, lista):
    return [funcion(x) for x in lista]

resultado = aplicar_operacion(lambda x: x**2, [1, 2, 3, 4, 5])
print(resultado)
