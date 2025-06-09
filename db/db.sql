CREATE DATABASE SKYROUTE;


USE SKYROUTE;


CREATE TABLE Clientes (
	ID int AUTO_INCREMENT,
    CUIT varchar(13) NOT NULL UNIQUE,
    RazonSocial varchar(255) NOT NULL,
    Email varchar(255),
    CreatedAt timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ID)
);


CREATE TABLE Destinos (
	ID int AUTO_INCREMENT,
    Ciudad varchar(255) NOT NULL,
    Pais varchar(255) NOT NULL,
    CostoBase float NOT NULL,
    Disponible boolean NOT NULL,
    CreatedAt timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ID)
);


CREATE TABLE Ventas (
	ID int AUTO_INCREMENT,
    IdCliente int NOT NULL,
    IdDestino int NOT NULL,
    FechaVenta date,
    Costo float NOT NULL,
    Estado varchar(8) NOT NULL,  
    TimestampAnulacion timestamp,
    CreatedAt timestamp DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ID),
    FOREIGN KEY (IdCliente) REFERENCES Clientes(ID) ON DELETE CASCADE,
    FOREIGN KEY (IdDestino) REFERENCES Destinos(ID) ON DELETE CASCADE,
    CONSTRAINT CHKESTADO CHECK (Estado = 'Activa' OR Estado = 'Anulada')
);