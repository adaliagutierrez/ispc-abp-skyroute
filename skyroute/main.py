from gestion_ventas import gestionar_ventas
from gestion_destinos import gestionar_destinos
from gestion_clientes import gestionar_clientes


def main():
    menu_principal()


def menu_principal ():

    salir = False

    while not salir:
        print("\n\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Botón de Arrepentimiento")
        print("5. Acerca del Sistema")
        print("6. Salir")
        print("-------------------------------\n")
        opcion = input("Ingrese una opción del menú: ")

        print(f"Ingresó a la opción {opcion}")

        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_destinos()
        elif opcion == "3":
            gestionar_ventas()
        elif opcion == "4":
            gestionar_ventas()
        elif opcion == "5":
            acerca_del_sistema()
        elif opcion == "6":
            salir = True
            print("Saliendo del sistema ...")
        else:
            print("Opción inválida. Intente nuevamente.")


def acerca_del_sistema():
    print("Se ha mostrado información del sistema")
    input("Continuar ...")


main()