import mysql.connector 
from config import db_config


def obtener_conexion():
    return mysql.connector.connect(**db_config)


def mostrar_all_clientes():
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    
    for cliente in clientes:
                for clave in cliente:
                    if clave not in ["CreatedAt", "UpdatedAt"]:
                        print(f"{clave}: {cliente[clave]}", end=" | ")
                print()
    cursor.close()
    conexion.close()


def agregar_cliente():
    razon_social = input("Razón Social: ")
    cuit = input("CUIT: ")
    correo = input("Correo Electrónico: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO Clientes (CUIT, RazonSocial, Email) VALUES (%s, %s, %s)"
    valores = (cuit, razon_social, correo)

    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cliente agregado con éxito.")


def modificar_cliente():
    id_cliente = input("ID del cliente a modificar: ")
    nueva_razon = input("Nueva razón social: ")
    nuevo_cuit = input("Nuevo CUIT: ")
    nuevo_correo = input("Nuevo correo electrónico: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE clientes SET RazonSocial = %s, CUIT = %s, Email = %s WHERE ID = %s"
    valores = (nueva_razon, nuevo_cuit, nuevo_correo, id_cliente)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cliente modificado con éxito.")


def eliminar_cliente():
    id_cliente = input("ID del cliente a eliminar: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM clientes WHERE ID = %s"

    valor = (id_cliente,)
    cursor.execute(sql, valor)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cliente eliminado con éxito.")


def mostrar_all_destinos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM destinos")
    destinos = cursor.fetchall()

    for destino in destinos:
        for clave in destino:
            if clave not in ["CreatedAt", "UpdatedAt"]:
                print(f"{clave}: {destino[clave]}", end=" | ")
        print()

    cursor.close()
    conexion.close()


def agregar_destino():
    ciudad = input("Ciudad destino: ")
    pais = input("País destino: ")
    costo = input("Costo base: ")
    disponibilidad = True if input("Disponibilidad (1: disponible, 0:no disponible): ")=="1" else False
    

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO destinos (Ciudad, Pais, CostoBase, Disponible) VALUES (%s, %s, %s, %s)"
    valores = (ciudad, pais, costo, disponibilidad)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Destino agregado con éxito.")


def modificar_destino():
    id_destino = input("ID del destino a modificar: ")
    nueva_ciudad = input("Nueva ciudad: ")
    nuevo_pais = input("Nuevo país: ")
    nuevo_costo = input("Nuevo costo base: ")
    disponibilidad = True if input("Actualizar disponibilidad (1: disponible, 0:no disponible): ")=="1" else False

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE Destinos SET Ciudad = %s, Pais = %s, CostoBase = %s, Disponible = %s WHERE id = %s"
    valores = (nueva_ciudad, nuevo_pais, nuevo_costo, disponibilidad, id_destino)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Destino modificado con éxito.")


def eliminar_destino():
    id_destino = input("ID del destino a eliminar: ")

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM destinos WHERE ID = %s"
    cursor.execute(sql, (id_destino,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Destino eliminado con éxito.")
