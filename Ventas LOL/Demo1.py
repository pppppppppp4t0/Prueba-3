import os
os.system("cls")


mi_tupla = (1,"dos",3.0)
mi_lista = [1,"dos",3.0]

print(mi_tupla)
print(mi_lista)

print(mi_tupla[1])
#mi_tupla[1]="tres"   No se puede modificar porque las tuplas son inmutables

os.system("pause")

print("\n------------------------------------------\n")

mi_lista = [1, 2, 3]
mi_tupla = tuple(mi_lista)
# Imprimir la tupla
print(mi_tupla)


os.system("pause")
print("\n------------------------------------------\n")

diccionario = {"nombre": "Cesar Huispe", 
                "fonos": [
                        988778882, 
                        988877776, 
                        877666333], 
                "activo": True}

print(diccionario)

diccionario['edad']=22            #si el elemento NO EXISTE... lo agrega
diccionario['nombre'] = "Susana"  # si el elemento existe lo MODIFICA

print(diccionario)



print("\n------------------------------------------\n")

#recorrer e imprimir un diccionario
print("recorrer diccionario")
for e in diccionario:
    print(e,":",diccionario[e])  # agregar al final end=" "





print("\n------------------------------------------\n")  


#lista de lista  ->matriz
alumnos=[
          ["1-1","Susana",22],
          ["2-2","David",19],
          ["3-3","Sandra",20]
        ]

#print(alumnos)
for e in alumnos:
    print(e)

os.system("pause")





#buscar el rut 2-2 e imprimir sus datos
print("\n------------------------------------------\n")

rut=input("Ingrese rut a buscar: ")
sw=0 #no existe
for a in alumnos:
    if a[0] == rut:
        sw=1 #existe, encontrado
        print(a[0]," ",a[1]," ",a[2])
        break

if sw==0:
    print("Error, rut no existe")

print("\n------------------------------------------\n")

#Crea un función de búsqueda y aplicar al
#ejercicio anterior, a partir de la linea 94

#print(alumnos.index("2-2"))

def buscar_rut(rut):    
    for a in alumnos:
        if a[0] == rut:           
           return a
    return -1   
     
def buscar_indice_rut(rut):  
    i=0  
    for a in alumnos:
        if a[0] == rut:           
           return i
        i=i+1
    return -1 

  
print("Buscar con función")
lista=buscar_rut("10-3")
if lista != -1:
    print(lista)
else:
    print("Error, rut no existe")


os.system("pause")
print("\n------------------------------------------\n")

#Buscar el rut 2-2 y modificar la edad por 25
#luego imprimir la lista alumnos.

rut=input("Ingrese rut a buscar: ")
nueva_edad= int(input("Ingrese la nueva edad: "))

lista=buscar_rut(rut)

if lista != -1:
    lista[2]=nueva_edad #actualizar/ modificar
    print(alumnos)
else:
    print("Error, rut no existe")


print("\n------------------------------------------\n")
# elimnar por un rut
#versión 1
print("Eliminar por rut")
rut=input("Ingrese rut a buscar: ")
lista=buscar_rut(rut)

if lista != -1:
    alumnos.remove(lista)
    print(alumnos)
else:
    print("Error, rut no existe")


# elimnar por un rut
#versión 2
print("Eliminar por rut")
rut=input("Ingrese rut a buscar: ")
indice=buscar_indice_rut(rut)

if indice != -1:
    alumnos.pop(indice)
    print(alumnos)
else:
    print("Error, rut no existe")


# Agregar
print("\nAgregar\n")
rut = input("Ingrese su rut: ")
nombre= input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

alumnos.append([rut, nombre, edad])

print(alumnos)