# Librería Artística

Trabajo práctico de Programación Orientada a Objetos: una aplicación de consola en Python para gestionar una librería artística (clientes, vendedores, productos, descuentos y ventas), organizada en N-capas y con una base de datos MySQL.

## Funcionalidades

- **Clientes y Vendedores:** alta, listado, consulta por ID, búsqueda, modificación y baja. No se pueden eliminar si tienen ventas asociadas.
- **Productos:** alta, listado, consulta por ID, búsqueda, modificación y baja. No se pueden eliminar si fueron vendidos.
- **Descuentos:** por marca o por categoría, de tipo porcentaje o 2x1. Incluye una opción para **simular el descuento** de un producto según la cantidad, sin registrar una venta.
- **Ventas:**
  - Crear una venta con uno o más productos. Se valida el stock, se aplica automáticamente el mejor descuento disponible para cada producto y se pide confirmación antes de guardar.
  - Ver todas las ventas, buscar por número de factura o por DNI del cliente.
  - Eliminar una venta, reponiendo el stock de los productos.

## Estructura del proyecto

```
├── base_de_datos/
│   └── script.sql        # Creación de la base, tablas y datos de prueba
├── objetos/              # Clases del dominio y lógica de negocio
├── datos/                # Acceso a la base de datos (consultas SQL)
├── presentacion/         # Menús de consola y validación de entradas
│   └── app.py            # Punto de entrada
└── requirements.txt
```

Cada capa solo depende de las que están debajo: `presentacion` usa `datos` y `objetos`, `datos` usa `objetos`, y `objetos` no depende de ninguna.

## Requisitos

- Python 3.10 o superior
- MySQL Server 8.x (y opcionalmente MySQL Workbench)

## Instalación

1. **Clonar el repositorio**

   ```
   git clone https://github.com/rrousso/TP_libreria_artistica.git
   cd TP_libreria_artistica
   ```

2. **Instalar dependencias**

   ```
   py -m pip install -r requirements.txt
   ```

3. **Crear la base de datos**

   Abrir `base_de_datos/script.sql` en MySQL Workbench y ejecutarlo completo. El script crea la base `libreria_artistica` con sus tablas y carga datos de prueba.

   > ⚠️ El script empieza con `DROP DATABASE IF EXISTS`, así que al volver a ejecutarlo se borran todos los datos cargados y se restaura el estado inicial.

4. **Configurar la conexión**

   La contraseña de MySQL se lee de la variable de entorno `DB_PASSWORD`. En Windows:

   ```
   setx DB_PASSWORD "tu_contraseña"
   ```

   Después hay que cerrar y volver a abrir la terminal. Si hace falta, también se pueden definir `DB_HOST` (por defecto `localhost`) y `DB_USER` (por defecto `root`).

## Ejecución

Desde la carpeta raíz del proyecto:

```
py presentacion/app.py
```

## Decisiones de diseño

- **Las ventas no se modifican.** Igual que una factura, una venta registrada no se edita.
- **Las ventas se eliminan, no se anulan.** Anular con nota de crédito quedó fuera del alcance del trabajo. Al eliminar una venta se repone el stock y el detalle se borra en cascada.
- **Transacciones.** Crear y eliminar una venta tocan varias tablas (ventas, detalle y stock de productos). Todo se hace en una sola transacción: si algún paso falla, se hace `rollback` y no queda nada a medias.
- **Precio histórico.** El detalle de cada venta guarda el precio unitario y el descuento del momento, así un cambio de precio posterior no altera las ventas pasadas.
- **El cálculo del descuento vive en los objetos** (`Descuento.calcularMonto`, `DetalleVenta.aplicarMejorDescuento`). La simulación y la venta real usan el mismo código, por lo que siempre dan el mismo resultado.
- **Número de factura.** Se usa el ID autoincremental de la venta.
- **Montos con `Decimal`** en lugar de `float`, para evitar errores de redondeo con dinero.

## Autor

Rafael Rousso