# SkyRoute

## Descripción del proyecto

**SkyRoute** es un sistema de gestión de ventas de pasajes turísticos para una agencia de viajes. El proyecto permite la administración de clientes, destinos y ventas, incluyendo la funcionalidad del botón de arrepentimiento, todo integrado con una base de datos MySQL. Este sistema fue desarrollado como parte de la Evidencia 3 del módulo Programador del Trayecto de Saberes Contextuales de la Inteligencia Artificial (TSCDeIA) 2025 del ISPC.

## Integrantes del grupo


- Diaz Nievas, Carlos Fabricio - DNI 41481493 - [@fdiaznievas](https://github.com/fdiaznievas)
- Gutierrez Bernal, Adalia Scarlett - DNI 42439229 - [@adaliagutierrez](https://github.com/adaliagutierrez)


## Instrucciones básicas de ejecución del proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/adaliagutierrez/ispc-abp-skyroute.git
   cd skyroute
   ```

2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate    # En Linux/macOS
   venv\Scripts\activate.bat   # En Windows
   ```

3. Instalar las dependencias:
   ```bash
   pip install mysql-connector-python
   ```

4. Configurar los datos de conexión a la base de datos en el archivo `skyroute/config.py`.

5. Ejecutar la construcción de la BD con el archivo `db/db.sql` dentro de tu servidor MySQL.

6. Cargar de información las tablas con el archivo `db/insert-data.sql`.

7. Ejecutar el programa principal:
   ```bash
   python main.py
   ```
8. Navegar entre las opciones ingresando la opción deseada y presionando Enter.

## Estructura del repositorio

```
skyroute/
├── config.py               # Configuración de conexión a la base de datos
├── main.py                 # Archivo principal con menú de opciones
├── conexion_base_datos.py  # Conexión y operaciones con MySQL
├── gestion_clientes.py     # Alta, baja, modificación, listado de clientes
├── gestion_destinos.py     # Alta, baja, modificación, listado de destinos
├── gestion_ventas.py       # Registrar ventas y botón de arrepentimiento
└── README.md               # Documentación del proyecto (este archivo)

db/
├── db.sql                  # Archivo principal con menú de opcionesskyroute/
├── consultas.sql           # Sentencias DML personalizadas segun lo solicitado en el enunciado del proyecto
├── insert-3-registros.sql  # Segun lo solicitado, se incluyen 3 instrucciones INSERT
└── insert-data.sql         # Inserción masiva de datos a la BD

entregables/
├── video_presentacion.mp4             # Video de presentación del grupo
├── Poster-Defensa-en-el-Proyecto-ABP  # Configuración de conexión a la base de datos
└── Proyecto-SkyRoute-ABP              # Archivo principal con menú de opcionesskyroute/
```
