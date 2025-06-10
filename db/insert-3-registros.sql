-- Sentencia DML que inserta clientes en la tabla Clientes
INSERT INTO Clientes (RazonSocial, CUIT, Email) VALUES
('Tech Global SRL', '30-12345678-9', 'contacto@techglobal.com'),
('Logística Sur SA', '30-87654321-0', 'ventas@logisticasur.com'),
('Viajes Mendoza', '30-11223344-5', 'info@viajesmendoza.com');

-- Sentencia DML que inserta destinos en la tabla Destinos
INSERT INTO Destinos (Ciudad, Pais, CostoBase, Disponible) VALUES
('Buenos Aires', 'Argentina', 45000, true),
('Santiago', 'Chile', 60000, false),
('Lima', 'Perú', 55000, true);

-- Sentencia DML que inserta 3 registros en la tabla Ventas (estado inicial: Activa)
INSERT INTO Ventas (IdCliente, IdDestino, FechaVenta, Costo, Estado) VALUES
(1, 2, '2025-06-01', 60000, 'Activa'),
(2, 3, '2025-06-02', 55000, 'Activa'),
(3, 1, '2025-06-03', 45000, 'Activa');
