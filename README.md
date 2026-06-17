# TPI - Gestión de Datos de Países en Python

Trabajo Práctico Integrador de la materia **Programación 1**
Tecnicatura Universitaria en Programación a Distancia - UTN

## Descripción

Este programa permite gestionar información de países (nombre, población,
superficie y continente) almacenada en un archivo CSV. Mediante un menú
interactivo en consola, el usuario puede agregar nuevos países, actualizar
datos existentes, realizar búsquedas, aplicar filtros, ordenar el listado
y consultar estadísticas generales del dataset.

El proyecto fue desarrollado aplicando los conceptos de **listas,
diccionarios, funciones, estructuras condicionales y repetitivas,
ordenamientos y estadísticas básicas**, vistos en la materia.

## Estructura del proyecto

```
.
├── main.py        # Código fuente principal
├── paises.csv     # Dataset base de países
└── README.md      # Este archivo
```

## Estructura de datos

Cada país se representa como un diccionario con la siguiente forma:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}
```

Todos los países se almacenan en una **lista de diccionarios**.

## Requisitos

- Python 3.x (no requiere librerías externas, solo módulos estándar:
  `csv` y `os`)

## Cómo ejecutar el programa

1. Cloná o descargá este repositorio.
2. Asegurate de que el archivo `paises.csv` esté en la misma carpeta que
   `main.py`.
3. Ejecutá desde la consola:

```bash
python3 main.py
```

(En Windows puede ser `python main.py`, dependiendo de tu instalación).

## Menú de opciones

Al iniciar, el programa carga los datos desde `paises.csv` y muestra el
siguiente menú:

```
========================================
   GESTIÓN DE DATOS DE PAÍSES
========================================
1. Agregar país
2. Actualizar población y superficie
3. Buscar país por nombre
4. Filtrar por continente
5. Filtrar por rango de población
6. Filtrar por rango de superficie
7. Ordenar países
8. Mostrar estadísticas
9. Mostrar todos los países
10. Guardar cambios en el archivo CSV
0. Salir
========================================
```

### Detalle de funcionalidades

- **Agregar país**: solicita nombre, población, superficie y continente.
  No permite campos vacíos ni nombres duplicados.
- **Actualizar país**: permite modificar la población y superficie de un
  país existente, identificándolo por su nombre exacto.
- **Buscar por nombre**: admite coincidencia parcial (no distingue
  mayúsculas/minúsculas).
- **Filtrar**: por continente, por rango de población o por rango de
  superficie.
- **Ordenar**: por nombre, población o superficie, en orden ascendente o
  descendente, sin modificar el orden original de la lista.
- **Estadísticas**: país con mayor y menor población, promedio de
  población, promedio de superficie y cantidad de países por continente.
- **Guardar**: escribe los cambios realizados (altas/actualizaciones) en
  el archivo `paises.csv`. También se ofrece la opción de guardar al
  salir del programa.

## Ejemplo de uso

### Ejemplo: Filtrar por continente

```
Seleccione una opción: 4

--- Filtrar por continente ---
Ingrese el continente: Asia

Países en Asia: (5)
Nombre                         Población    Superficie (km²)     Continente
---------------------------------------------------------------------------
Japón                          125800000              377975           Asia
China                         1444216107             9596961           Asia
India                         1380004385             3287263           Asia
Corea del Sur                   51269185              100210           Asia
Indonesia                      273523615             1904569           Asia
```

### Ejemplo: Mostrar estadísticas

```
Seleccione una opción: 8

--- Estadísticas ---
Cantidad total de países: 20
País con mayor población: China (1444216107 habitantes)
País con menor población: Nueva Zelanda (4822233 habitantes)
Promedio de población: 237793621.55
Promedio de superficie: 3075223.60 km²

Cantidad de países por continente:
  - América: 5
  - Asia: 5
  - Europa: 5
  - África: 3
  - Oceanía: 2
```

### Ejemplo: Agregar un país (validación de campos vacíos)

```
Seleccione una opción: 1

--- Agregar nuevo país ---
Nombre del país:
Error: el campo no puede estar vacío. Intente nuevamente.
Nombre del país: Chile
Población: 19116209
Superficie (km²): 756102
Continente: América
País 'Chile' agregado correctamente.
```

## Dataset incluido

El archivo `paises.csv` incluye un dataset base de 20 países con sus
respectivos valores de población, superficie y continente, cubriendo
América, Asia, Europa, África y Oceanía.

## Documentación

- Informe teórico y técnico (PDF): https://drive.google.com/file/d/1wgSYPtaBRifzUYfMbKoKsJaXKjzX6uqs/view?usp=sharing
  
## Video demostrativo

- Link al video: https://youtu.be/Jk8Cgwm0iec?si=pDYpTls1Y1xE4k36
  
## Integrantes

- Castro Martina [GRUPO_243]

## Materia

Programación 1 - Tecnicatura Universitaria en Programación a Distancia
(UTN)
