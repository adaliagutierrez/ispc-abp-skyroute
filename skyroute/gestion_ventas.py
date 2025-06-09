from conexion_base_datos import mostrar_all_ventas, registrar_venta, anular_venta
import os


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")  # Para Windows
    else:
        os.system("clear")  # Para sistemas Unix


def gestionar_ventas():
    salir = False
    while not salir:
        limpiar_pantalla()

        print("\n\nGESTIONAR VENTAS ")
        print("1. Ver ventas")
        print("2. Registrar venta")
        print("3. Anular venta (botón de arrepentimiento)")
        print("9. Volver al Menú Principal")
        print("-------------------------------\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n\nListado de Ventas\n")
            mostrar_all_ventas()
            input("Continuar ...")

        elif opcion == "2":
            print("\nRegistrar Venta\n")
            registrar_venta()
            input("Continuar ...")

        elif opcion == "3":
            print("\nAnular Venta\n")
            anular_venta()
            input("Continuar ...")

        elif opcion == "9":
            salir = True

        else:
            print("Opción inválida. Intente nuevamente.")
