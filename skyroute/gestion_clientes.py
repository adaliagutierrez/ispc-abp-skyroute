from conexion_base_datos import mostrar_all_clientes, agregar_cliente, modificar_cliente, eliminar_cliente


def gestionar_clientes():
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
            print("\n\nListado de Clientes\n")
            mostrar_all_clientes()
            input("Continuar ...")


        elif opcion == "2":
            print("\nAgregar Cliente\n")
            agregar_cliente()
            input("Continuar ...")
            
                 
        elif opcion == "3":
            print("\nModificar Cliente\n")
            modificar_cliente()
            input("Continuar ...")


        elif opcion == "4":
            print("\nEliminar Cliente\n")
            eliminar_cliente()
            input("Continuar ...")


        elif opcion == "5":
                salir = True


        else: 
            print("Ingrese una opción válida")
            input("Continuar ...")                     

