''' 
PROPÓSITO DEL SISTEMA:

    SkyRoute S.R.L. es una agencia ficticia dedicada a la comercialización de pasajes aéreos para clientes empresariales y particulares. Con el objetivo de optimizar su operativa, la empresa solicita el desarrollo de un sistema digital básico que permita gestionar sus operaciones de forma eficiente a través de un menú de opciones por consola.


CÓMO INSTALAR Y EJECUTAR EL PROGRAMA:

    Para instalar el programa, debe descargar el archivo "main.py" desde el repositorio de GitHub 
        https://github.com/Majo1782/ISPC-ABP.git  
        
        https://github.com/Majo1782/ISPC-ABP

    Deberá ejecutar el archivo "main.py" en una terminal de Python y navegar entre las opciones del menú ingresando el número de la opción deseada.


DATOS DE LOS INTEGRANTES:

    Diaz Nievas, Carlos Fabricio - DNI 41481493
    Garcia, Maria Jose - DNI 29757730
    Gutierrez Bernal, Adalia Scarlett - DNI 42439229



'''





def main():
    menu_principal()


def menu_principal ():

    opciones = ["Gestionar Clientes", "Gestionar Destinos", "Gestionar Ventas", "Consultar Ventas", "Botón de Arrepentimiento", "Ver Reporte General", "Acerca del Sistema", "Salir"]
    salir = False

    while not salir:
        print("\n\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Consultar Ventas")
        print("5. Botón de Arrepentimiento")
        print("6. Ver Reporte General")
        print("7. Acerca del Sistema")
        print("8. Salir")
        print("-------------------------------\n")
        opcion = input("Ingrese una opción del menú: ")

        print(f"Ingresó a la opción {opcion} - {opciones[int(opcion)-1]}")

        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_destinos()
        elif opcion == "3":
            gestionar_ventas()
        elif opcion == "4":
            consultar_ventas()
        elif opcion == "5":
            boton_de_arrepentimiento()
        elif opcion == "6":
            ver_reporte_general()
        elif opcion == "7":
            acerca_del_sistema()
        elif opcion == "8":
            salir = True
            print("Saliendo del sistema ...")
        else:
            print("Opción inválida. Intente nuevamente.")


def gestionar_clientes():

    clientes = []
    cliente1 = {
                "id": "1",
                "cuit": "20123456780",
                "razon": "Pepe Cuenca",
                "email": "correo@mail.com"
                }
    cliente2 = {
                "id": "2",
                "cuit": "20111111550",
                "razon": "Sebastian Zarate",
                "email": "correo2@mail.com"
                }
    cliente3 = {
                "id": "3",
                "cuit": "20988726230",
                "razon": "Emilia Navas",
                "email": "correo3@mail.com"
                }     
    clientes.append(cliente1)
    clientes.append(cliente2)
    clientes.append(cliente3)

    salir = False
    while not salir:
        print("\n\nGESTIONAR CLIENTES ")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        print("-------------------------------\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for cliente in clientes:
                print(f"Nro de Cliente: {cliente["id"]} - CUIT: {cliente["cuit"]} - Razon Social: {cliente["razon"]} - Email: {cliente["email"]}")

            input("Continuar ...")

        elif opcion == "2":
            print("Complete los siguientes datos")
            cuit = input ("CUIT: ")
            razon = input ("Razón Social: ")
            email= input ("Email: ")
            print ("-------------------------------\n")
            cliente = {
                "id": len(clientes)+1,
                "cuit": cuit,
                "razon": razon,
                "email": email
                }
            clientes.append(cliente)

            print ("Se ha agregado el siguiente cliente con éxito:")
            print (f"Nro. Cliente: {len(clientes)+1} - CUIT: {cuit} - Razon Social: {razon} - Email: {email}")
            input("Continuar ...")
            
                 
        elif opcion == "3":
            cuit = input ("Ingrese el CUIT del cliente a modificar: ")
            razon = input("Ingrese la nueva razón social: ") 
            email = input("Ingrese el nuevo email: ")
            print ("-------------------------------\n")
            print (f"CUIT: {cuit} - Razon Social: {razon} - Email: {email}")
            print ("Se han modificado los datos del cliente") 
            input("Continuar ...")

        elif opcion == "4":
            cuit= input ("Ingrese el cuit del cliente a eliminar: ")
            print ("-------------------------------\n")
            print(f"Se ha eliminado el cliente CUIT {cuit} con éxito")
            input("Continuar ...")


        elif opcion == "5":
                salir = True
        else: 
            print("Ingrese una opción válida")
            input("Continuar ...")                     


def gestionar_destinos():
    destinos = []

    salir = False
    while not salir:
        print("\n\nGESTIONAR DESTINOS ")
        print("1. Ver destinos")
        print("2. Agregar destino")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingresó a la opción 1. Ver destinos...")
            for destino in destinos:
                print(destino.pais_destino)
                print(destino.ciudad_destino)
            print("<Mostrar destinos aqui>")
            input("Continuar ...")


        elif opcion == "2":
            print("Ingresó a la opción 2. Agregar destino...")
            ciudad = input("Ciudad destino: ")
            pais = input("Pais destino: ")
            destinos.append((ciudad, pais))
            print (f"Ciudad destino: {ciudad} - Pais destino: {pais}\n")
            print ("Se ha agregado el destino con exito: ")
            input("Continuar ...")
                
        elif opcion == "3":
            print("Ingresó a la opción 3. Modificar destino...")
            ciudad = input ("Ingrese ciudad destino a modificar: ")

            se_encontró_destino = False

            for destino in destinos:
                if destino.ciudad_destino == ciudad:
                    destino.ciudad = ("Ingrese el nuevo nombre de ciudad: ")
                    destino.pais = ("Ingrese el nuevo nombre de pais: ")
                    print (f"Ciudad destino: {destino.ciudad} - Pais destino: {destino.pais}\n")
                    print ("Se ha modificado el destino con éxito")
                
                    se_encontró_destino = True
            
            if not se_encontró_destino:
                print("No se encontró el destino ingresado. Intentar de nuevo.")

            input("Continuar ...")


        elif opcion== "4":
            print("Ingresó a la opción 4. Eliminar destino...")
            ciudad = input ("Ingrese ciudad destino a eliminar: ")

            print("Se ha eliminado el destino correctamente")
            input("Continuar ...")
            
        elif opcion == "5":
            salir = True
        
        else:
            print("Opción inválida. Intente nuevamente.")


def gestionar_ventas():
    print("Se ha ingresado al Menú Gestionar Ventas... ")


def consultar_ventas():
    salir = False
    while not salir:
        print("\n\nCONSULTAR VENTAS")
        print("1. Consultar venta por vendedor")
        print("2. Volver al Menú Principal")
        print("-------------------------------\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingresó a la opción 1. Ver ventas por vendedor...")
            print("Se mostraron las ventas del vendedor")
            input("Continuar ...")

        elif opcion == "2":
            salir = True
            print("Saliendo...")

        else:
            print("Opción inválida. Intente nuevamente.")


def boton_de_arrepentimiento():
    print("Se ha ingresado al Menú Botón de Arrepentimiento...")
    input("Continuar ...")


def ver_reporte_general():
    salir = False
    while not salir:
        print("\n\nVER REPORTE GENERAL")
        print("1. Ver Ventas de la Semana")
        print("2. Ver Ventas del Mes")
        print("3. Volver al Menú Principal")
        print("-------------------------------\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ingresó a la opción 1. Ver ventas de la semana...")
            print("Se mostraron las ventas de la semana")
            input("Continuar ...")

        elif opcion == "2":
            print("Ingresó a la opción 2. Ver ventas del mes...")
            print("Se mostraron las ventas del mes")
            input("Continuar ...")

        elif opcion == "3":
            salir = True
            print("Saliendo...")

        else:
            print("Opción inválida. Intente nuevamente.")


def acerca_del_sistema():
    print("Se ha mostrado información del sistema")
    input("Continuar ...")


main()