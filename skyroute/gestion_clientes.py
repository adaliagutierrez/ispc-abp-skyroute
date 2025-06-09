from conexion_base_datos import traer_all_clientes


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
            clientes = traer_all_clientes()
            for cliente in clientes:
                for clave in cliente:
                    if clave not in ["CreatedAt", "UpdatedAt"]:
                        print(f"{clave}: {cliente[clave]}", end=" | ")
                print()
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

