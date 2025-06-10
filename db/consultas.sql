-- A continuación se muestran algunas sentencias DML de consulta personalizadas (SELECT)


-- Lista todos los registros de la tabla Clientes
SELECT * FROM Clientes;



-- Ventas realizadas el 2025-06-01, podés cambiar la fecha por otra
SELECT * FROM Ventas
WHERE FechaVenta = '2025-06-01';



-- Muestra el ID del cliente, la venta más reciente y su fecha
SELECT v.IdCliente, MAX(v.FechaVenta) AS UltimaVenta
FROM Ventas v
GROUP BY v.IdCliente;



-- Destinos cuya ciudad empieza con la letra 'S'
SELECT * FROM Destinos
WHERE Ciudad LIKE 'S%';




-- Cuenta la cantidad de ventas agrupadas por país (relacionando ventas con destinos)
SELECT d.Pais, COUNT(*) AS CantidadVentas
FROM Ventas v
JOIN Destinos d ON v.IdDestino = d.ID
GROUP BY d.Pais;



