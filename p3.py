import math
def obtener_lados(ladosA):
    for i in range (0,ladosA):
        lado=float(input(f"Ingrese el valor del ladon en cm {i+1}: "))
        lados.append(lado)
triangulo=lambda lados:(lados[1]*math.sqrt(lados[0]**2-(lados[1]**2/4)))/2
cuadrado=lambda lados:lados[0]*lados[1]
hexagono=lambda lados:(3 * math.sqrt(3) * lados[0]**2) / 2
pentagono=lambda lados:(5/4) * lados[0]**2 * (1 / math.tan(math.pi / 5))

estado=True 
while estado==True:
    lados=[]
    print("bienvenido a la calculadora de area de formas")
    opcion=int(input("\n 1.triangulo \n 2.cuadrado \n 3.hexagono \n 4.pentagono \n -a que tipo de figura desea calcular su Area solo con sus lados: "))
    cantidadLados=int(input("cuantos lados tiene tu figura en el caso de hexagono y pentagono solo es necesario 1: "))
    if opcion==1:
        obtener_lados(cantidadLados)
        print(f"el triangulo tiene un area de {round(triangulo(lados))} cm cuadrados")
    elif opcion==2:
        obtener_lados(cantidadLados)
        print(f"el cuadrado tiene un area de {round(cuadrado(lados))} cm cuadrados")     
    elif opcion==3:
        obtener_lados(cantidadLados)
        print(f"el hexagono tiene un area de {round(pentagono(lados))} cm cuadrados")
    elif opcion==4:
        obtener_lados(cantidadLados)
        print(f"el pentagono tiene un area de {round(hexagono(lados))} cm cuadrados")
    