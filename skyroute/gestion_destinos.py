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

