import random
Departamentos = {
    "Amazonas": {"capital": "Leticia"},
    "Antioquia": {"capital": "Medellín"},
    "Arauca": {"capital": "Arauca"},
    "Atlántico": {"capital": "Barranquilla"},
    "Bogotá, D.C.": {"capital": "Bogotá"},
    "Bolívar": {"capital": "Cartagena"},
    "Boyacá": {"capital": "Tunja"},
    "Caldas": {"capital": "Manizales"},
    "Caquetá": {"capital": "Florencia"},
    "Casanare": {"capital": "Yopal"},
    "Cauca": {"capital": "Popayán"},
    "Cesar": {"capital": "Valledupar"},
    "Chocó": {"capital": "Quibdó"},
    "Córdoba": {"capital": "Montería"},
    "Cundinamarca": {"capital": "Bogotá"},
    "Guainía": {"capital": "Inírida"},
    "Guaviare": {"capital": "San José del Guaviare"},
    "Huila": {"capital": "Neiva"},
    "La Guajira": {"capital": "Riohacha"},
    "Magdalena": {"capital": "Santa Marta"},
    "Meta": {"capital": "Villavicencio"},
    "Nariño": {"capital": "Pasto"},
    "Norte de Santander": {"capital": "Cúcuta"},
    "Putumayo": {"capital": "Mocoa"},
    "Quindío": {"capital": "Armenia"},
    "Risaralda": {"capital": "Pereira"},
    "San Andrés y Providencia": {"capital": "San Andrés"},
    "Santander": {"capital": "Bucaramanga"},
    "Sucre": {"capital": "Sincelejo"},
    "Tolima": {"capital": "Ibagué"},
    "Valle del Cauca": {"capital": "Cali"},
    "Vaupés": {"capital": "Mitú"},
    "Vichada": {"capital": "Puerto Carreño"}
}
DepartamentosArray=[]
on=True
fallos=0
for x in Departamentos.keys():
    print(f"departamento de: {x}")
    DepartamentosArray.append(x)
while on==True:
    RandomNumber=random.randint(0,31)
    randomDepartamento=DepartamentosArray[RandomNumber]
    while fallos <3:
        pregunta=(input(f"cual es la capital de {randomDepartamento}: ")).upper()
        Busqueda=Departamentos[randomDepartamento].get(f"capital").upper()
        if(pregunta==Busqueda):
            print("correcto")
            fallos=1+fallos
        elif(pregunta!=Busqueda):
            print("incorrecto")
            fallos=1+fallos
            if fallos==3:
                print(f"incorrecto la capital correcta era {Busqueda}")
    continuar=(input("desea cerrar el programa? (1.si,2.no): "))
    on=True if continuar==1 else False
        
    
   
    
