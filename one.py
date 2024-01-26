"""for i in range(3, 9):
    if i % 4 == 0:
        print(i)"""

"""edad = 15 

if edad <= 20 :
    print("Menor de edad")
else: 
    print("Mayor de edad")  """

"""palabras = ["gato", "perro", "oso", "elefante", "raton"]

for palabra in palabras:
    if len(palabra) > 3:
        print(palabra)"""

palabras = ["gato", "perro", "elefante", "raton", "zorro", "elefante", "león"]

indice = 0
while indice < len(palabras) and not palabras[indice].startswith("e"):
    print(palabras[indice])
    indice += 1
