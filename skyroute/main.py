from gestion_ventas import gestionar_ventas
from gestion_ventas import consultar_ventas

from gestion_destinos import gestionar_destinos

from gestion_clientes import gestionar_clientes


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