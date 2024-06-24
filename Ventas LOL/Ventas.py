
import os 
import pyfiglet
os.system("cls") 

print(pyfiglet.figlet_format("Venta de Helados"))
print("           Autores: Patricio Vergara y Matias Morales")

Productos=[#   id       producto      tamaño  stock precio 
            ["p001","Helado Vainilla","Normal", 40,  1800],
            ["p002","Helado Vainilla","Grande", 30,  1900],
            ["p003","Helado Fresa",   "Normal", 50,  1850],
            ["p004","Helado Fresa",   "Grande", 35,  2000],
            ["p005","Helado Chocolate","Normal",45,  1800],
            ["p006","Helado Chocolate","Grande",30,  1900],
            ["p007","Helado Lucuma",  "Normal", 40,  1700],
            ["p008","Helado Lucuma",  "Grande", 30,  1900],
            ["p009","Helado Maracuya","Normal", 50,  1700],
            ["p010","Helado Maracuya","Grande", 35,  1900]
          ]
folio= 10000
fecha="11-01-2024"

ventas= [# folio,   fecha,    id, cantidad, total
          [10001,"11-01-2024","p001",1,1800],  
          [10002,"12-01-2024","p002",1,1900],                   
          [10003,"10-02-2024","p003",1,1850],         
          [10004,"30-02-2024","p004",1,2000],
          [10005,"21-03-2024","p005",1,1800],
          [10006,"30-03-2024","p006",1,1900],                                 
          [10007,"07-04-2024","p007",1,1700],
          [10008,"28-04-2024","p008",1,1900],
          [10009,"03-05-2024","p009",1,1700],
          [10010,"06-05-2024","p010",1,1900],
          [10011,"23-06-2024","p001",2,3600],
          [10012,"27-06-2024","p002",2,3800],
          [10013,"18-07-2024","p003",2,3700],
          [10014,"02-08-2024","p004",2,4000],
          [10015,"05-08-2024","p005",2,3600],
          [10016,"09-09-2024","p006",2,3800],
          [10017,"01-10-2024","p007",2,3400],
          [10018,"14-11-2024","p008",2,3800],
          [10019,"20-11-2024","p009",2,3400],
          [10020,"17-12-2024","p010",2,3800]
        ]

def get_folio():
    if len(ventas)!=0:
        elemento = len(ventas)-1
        return (ventas[elemento])[0]
    else:
        return -1

Id=""
opcion=0
def buscar_id(Id):    
    for p in Productos:
        if p[0] == Id:           
           return p
    return -1   

def cargar_productos(archivo):
    with open(archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")

            Productos.append(datos)
    return -1

while opcion<=5: 

    print("")
    print("""
          
           Sistema de Ventas
        ------------------------
            1. Vender productos
            2. Reportes
            3. Mantenedores
            4. Administracion 
            5. Salir                                                         
          
          """) 
    
    op=int(input("Ingrese una opcion entre 1-5: "))
    match op:
            case 1:
                while True:
                    os.system("cls")
                    print("   Vender productos   \n")
                    Id=int(input("Ingrese el ID:"))
                    i=buscar_id(Id)
                    if i != -1:
                        print("Encontrado en el elemento", i)
                        producto=producto[i]
                        print(producto[0]," ",producto[1]," ",producto[4]," ",producto[5])
                        cantidad= int(input("Ingrese cantidad a comprar: "))
                        if cantidad <= producto[4]:
                            print("Stock disponible!\n")
                            total=cantidad*producto[5]
                            respuesta=input("Desea realizar la compra s/n: ")
                            print(f"El total a pagar por {cantidad} productos es {total}" )
                            if respuesta.lower() == "s":
                                producto[4]=producto[4]-cantidad  #stock actualizado 
                                #Grabar venta
                                ventas.append([get_folio()+1,fecha,Id,cantidad,total ])

                        else:
                            print("Error, la cantidad ingresada supera el stock,")
                    respuesta=input("Desea comprar otro producto s/n: ")
                    if respuesta.lower() == "n":
                        break                  

            case 2:
                os.system("cls")
                op=0
                print   ("""
                                   REPORTES
                        -----------------------------------
                        1. General de ventas (con total)
                        2. Ventas por fecha especifica (con total)
                        3. Ventas por rango de fecha (con total) 
                        4. Salir al menu pricipal
                        
                             """)
                op=int(input("Ingrese una opcion entre 1-4: "))

                match op:
                    case 1: 
                        for venta in ventas:
                            print(venta[0]," ",venta[1], " ",venta[2])
                            a=a+venta[2]
                        print("total= ", a)

                    case 2:
                        fecha_especifica = input("Ingrese la fecha (dd-mm-aaaa): ")
                        total_ventas = 0
                        for venta in ventas:
                            if venta[1] == fecha_especifica:
                                print(f"Folio {venta[0]}, Fecha {venta[1]}, ID {venta[2]}, Cantidad {venta[3]}, Total {venta[4]}")
                            total_ventas += venta[4]
                            print(f"Total de ventas en {fecha_especifica}: {total_ventas}")

                    case 3:
                        fecha_inicial = input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
                        fecha_final = input("Ingrese la fecha de fin (dd-mm-aaaa): ")
                        total_ventas = 0
                        for venta in ventas:
                            if fecha_inicial <= venta[1] <= fecha_final:
                                print(f"Folio {venta[0]}, Fecha {venta[1]}, ID {venta[2]}, Cantidad {venta[3]}, Total {venta[4]}")
                        total_ventas += venta[4]
                        print(f"Total de ventas entre {fecha_inicial} y {fecha_final}: {total_ventas}")

                if op==4:
                    break

                else:
                    print("Error, debe ingresar un valor entre 1 y 4")
                    os.system("pause")

            case 3:
                op=0
                while op <=6:
                    print("""
                        MANTENEDOR DE PRODUCTOS
                        1. Agregar
                        2. Buscar
                        3. Eliminar
                        4. Modificar
                        5. Listar
                        6. Salir al menu principal
                          
                        """)
                    op=int(input("Ingrese una opcion entre 1-6: "))

                    match op:
                        case 1:
                            print("\nAgregar\n")
                            Id = input("Ingrese el Id del producto: ")
                            Producto= input("Ingrese el nombre de producto: ")
                            Tamaño =(input("Ingrese el tamaño del producto: "))
                            Stock = int(input("Ingrese stock del producto: "))
                            Precio = int(input("Ingrese precio del producto: "))

                            Productos.append([Id,Producto,Tamaño,Stock,Precio])

                            print(Productos)

                        case 2:

                            Id=input("Ingrese el Id a buscar: ")
                            sw=0 #no existe
                            for p in Productos:
                                if p [0]== Id:
                                    sw=1 #existe, encontrado
                                    print(p[0]," ",p[1]," ",p[2]," ",p[3]," ",p[4])
                                    break 

                            if sw==0:
                                print("Error,Id no existe")
                        case 3:
                            Id=input("Ingrese Id a buscar: ")
                            lista=buscar_id(Id)

                            if lista != -1:
                                Productos.remove(lista)
                                print(Productos)
                            else:
                                print("Error, Id no existe")

                        case 4:
                            Id=input("Ingrese Id a buscar: ")
                            nuevo_producto=(input("Ingrese el nuevo producto: "))
                            nuevo_tamaño=(input("Ingrese el nuevo tamaño: "))
                            nuevo_stock= int(input("Ingrese el nuevo stock: "))
                            nuevo_precio= int(input("Ingrese el nuevo precio: "))

                            lista=buscar_id(Id)

                            if lista != -1:
                                lista[1]=nuevo_producto
                                lista[2]=nuevo_tamaño
                                lista[3]=nuevo_stock
                                lista[4]=nuevo_precio 
                                print(Productos)
                            else:
                                print("Error, Id no existe")

                        case 5:
                            for p in Productos:
                                print(p[0]," ",p[1]," ",p[2]," ",p[3]," ",p[4])
                            
                    if op==6:
                        break 
                    os.system("pause")
                else:
                    print("Error, debe ingresar un valor entre 1 y 6")
                    os.system("pause")
                print("Fin del menu")

            case 4:
                op=0
                while op <=3:
                    cargar_productos
                    print(""" 
                        MENU ADMINISTRACION
                      ----------------------
                        1. Cargar datos 
                        2. Respaldar datos (Grabar Actualizar)
                        3. Salir al menu pricipal 
                        """)
                op=int(input("Ingrese una opcion entre 1-3: "))               

                match opcion:
                    case 1:pass


                    case 2:pass


                if op==3:
                    break
                else:
                    print("Error, debe ingresar un valor entre 1 y 3")
                    os.system("pause") 

    if op==5:
        break 
else:
    print("Error, debe ingresar un valor entre 1 y 5")
    os.system("pause")
        
print("Fin del menú")