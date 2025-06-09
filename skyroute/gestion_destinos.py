from conexion_base_datos import mostrar_all_destinos, agregar_destino, modificar_destino, eliminar_destino
import os


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")  # Para Windows
    else:
        os.system("clear")  # Para sistemas Unix


def gestionar_destinos():
    salir = False
    while not salir:
        limpiar_pantalla()

        print("\n\nGESTIONAR DESTINOS ")
        print("1. Ver destinos")
        print("2. Agregar destino")
        print("3. Modificar destino")
        print("4. Eliminar destino")
        print("9. Volver al Menú Principal")
        print("-------------------------------\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n\nListado de Destinos\n")
            mostrar_all_destinos()
            input("Continuar ...")

        elif opcion == "2":
            print("\nAgregar Destino\n")
            agregar_destino()
            input("Continuar ...")

        elif opcion == "3":
            print("\nModificar Destino\n")
            modificar_destino()
            input("Continuar ...")

        elif opcion == "4":
            print("\nEliminar Destino\n")
            eliminar_destino()
            input("Continuar ...")

        elif opcion == "9":
            salir = True

        else:
            print("Opción inválida. Intente nuevamente.")
