DROP DATABASE IF EXISTS libreria_artistica;
CREATE DATABASE IF NOT EXISTS libreria_artistica;
USE libreria_artistica;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,
    marca VARCHAR(50),
    categoria VARCHAR(50),
    presentacion VARCHAR(50),
    unidades_por_paquete INT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    dni VARCHAR(15) NOT NULL UNIQUE,
    fecha_nacimiento DATE,
    puntos_acumulados INT DEFAULT 0 NOT NULL
);

CREATE TABLE IF NOT EXISTS vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    dni VARCHAR(15) NOT NULL UNIQUE,
    fecha_nacimiento DATE,
    cargo VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS descuentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,
    marca VARCHAR(50),
    categoria VARCHAR(50),
    tipo INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    cliente_id INT NOT NULL,
    vendedor_id INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id)
);

CREATE TABLE IF NOT EXISTS detalle_ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    venta_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    descuento_aplicado DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (venta_id) REFERENCES ventas(id)
);

-- =========================================================
-- DATOS DE PRUEBA
-- tipo de descuento: 1 = PORCENTAJE, 2 = DOS_POR_UNO
-- =========================================================

INSERT INTO productos (descripcion, marca, categoria, presentacion, unidades_por_paquete, precio, stock) VALUES
('Lápices de colores Ecolápices x12',  'Faber-Castell',   'Lápices',    'Caja',    12, 4500.00, 40),
('Lápiz grafito 2B',                   'Faber-Castell',   'Lápices',    'Unidad',   1,  650.00, 120),
('Acuarelas escolares x12',            'Faber-Castell',   'Acuarelas',  'Estuche', 12, 6800.00, 25),
('Acuarelas Cotman x12 pastillas',     'Winsor & Newton', 'Acuarelas',  'Estuche', 12, 32000.00, 8),
('Pincel redondo N°4 sintético',       'Winsor & Newton', 'Pinceles',   'Unidad',   1, 3900.00, 30),
('Pincel plano N°10 sintético',        'Pelikan',         'Pinceles',   'Unidad',   1, 2100.00, 35),
('Acrílico 200ml blanco titanio',      'Alba',            'Acrílicos',  'Pomo',     1, 5200.00, 20),
('Acrílico 60ml set x6 colores',       'Alba',            'Acrílicos',  'Set',      6, 9800.00, 15),
('Block acuarela A4 300g x12 hojas',   'Canson',          'Papeles',    'Block',   12, 11500.00, 18),
('Block dibujo A4 160g x20 hojas',     'Canson',          'Papeles',    'Block',   20, 6300.00, 22),
('Marcadores Triplus x10',             'Staedtler',       'Marcadores', 'Estuche', 10, 14200.00, 12),
('Microfibra Pigment Liner 0.3',       'Staedtler',       'Marcadores', 'Unidad',   1, 2700.00, 50);

INSERT INTO descuentos (descripcion, marca, categoria, tipo, valor) VALUES
('15% en toda la marca Faber-Castell', 'Faber-Castell',   NULL,        1, 15.00),
('10% en Acuarelas',                   NULL,              'Acuarelas', 1, 10.00),
('2x1 en Pinceles',                    NULL,              'Pinceles',  2,  0.00),
('25% en Winsor & Newton',             'Winsor & Newton', NULL,        1, 25.00),
('20% en Canson',                      'Canson',          NULL,        1, 20.00),
('2x1 en Staedtler',                   'Staedtler',       NULL,        2,  0.00);

INSERT INTO clientes (nombre, apellido, dni, fecha_nacimiento, puntos_acumulados) VALUES
('Lucía',    'Fernández', '38456123', '1994-05-12', 0),
('Martín',   'Gómez',     '35987654', '1990-11-03', 12),
('Valentina','Ruiz',      '42111222', '2000-02-28', 5),
('Tomás',    'Herrera',   '40333444', '1997-08-19', 0);

INSERT INTO vendedores (nombre, apellido, dni, fecha_nacimiento, cargo) VALUES
('Carla',  'Méndez', '33222111', '1988-04-07', 'Encargada'),
('Julián', 'Sosa',   '39555666', '1996-09-15', 'Vendedor');