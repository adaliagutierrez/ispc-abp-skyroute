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

