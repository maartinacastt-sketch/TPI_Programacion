import csv
import os

ARCHIVO = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

# ── ARCHIVO ──────────────────────────────────────────────────────────────────

def cargar_paises(archivo):
    # Lee el CSV y retorna una lista de diccionarios
    paises = []
    if not os.path.exists(archivo):
        print(f"Aviso: no se encontró '{archivo}'. Lista vacía.")
        return paises
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            if set(lector.fieldnames) != set(CAMPOS):
                print("Error: formato de CSV incorrecto.")
                return paises
            for i, fila in enumerate(lector, start=2):
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    }
                    if not pais["nombre"] or not pais["continente"]:
                        print(f"Aviso: fila {i} descartada (campo vacío).")
                        continue
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Aviso: fila {i} descartada (error de formato).")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return paises


def guardar_paises(paises, archivo):
    # Sobreescribe el CSV con la lista actual de países
    try:
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

# ── VALIDACIONES DE ENTRADA ───────────────────────────────────────────────────

def pedir_texto(mensaje):
    # Pide un texto no vacío
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el campo no puede estar vacío.")


def pedir_nombre(mensaje):
    # Pide un nombre que solo contenga letras, espacios y caracteres especiales (tildes, ñ)
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: el campo no puede estar vacío.")
        elif any(c.isdigit() for c in valor):
            print("Error: el nombre no puede contener números.")
        else:
            return valor


def pedir_entero_positivo(mensaje):
    # Pide un entero mayor a 0
    while True:
        try:
            n = int(input(mensaje).strip())
            if n > 0:
                return n
            print("Error: debe ser un número positivo.")
        except ValueError:
            print("Error: ingrese un número entero válido.")


def pedir_entero_no_negativo(mensaje):
    # Pide un entero mayor o igual a 0
    while True:
        try:
            n = int(input(mensaje).strip())
            if n >= 0:
                return n
            print("Error: el valor no puede ser negativo.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

# ── ALTA Y ACTUALIZACIÓN ──────────────────────────────────────────────────────

def agregar_pais(paises):
    # Solicita datos y agrega un nuevo país a la lista
    print("\n--- Agregar país ---")
    nombre = pedir_nombre("Nombre: ")
    if buscar_indice(paises, nombre) is not None:
        print(f"Error: ya existe '{nombre}'.")
        return
    paises.append({
        "nombre": nombre,
        "poblacion": pedir_entero_positivo("Población: "),
        "superficie": pedir_entero_positivo("Superficie (km²): "),
        "continente": pedir_nombre("Continente: "),
    })
    print(f"'{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    # Modifica la población y superficie de un país existente
    print("\n--- Actualizar país ---")
    if not paises:
        print("No hay países cargados.")
        return
    nombre = pedir_texto("Nombre exacto del país: ")
    i = buscar_indice(paises, nombre)
    if i is None:
        print(f"Error: no se encontró '{nombre}'.")
        return
    p = paises[i]
    print(f"Encontrado: {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
    p["poblacion"] = pedir_entero_positivo("Nueva población: ")
    p["superficie"] = pedir_entero_positivo("Nueva superficie (km²): ")
    print("Datos actualizados correctamente.")


def buscar_indice(paises, nombre):
    # Retorna el índice del país con ese nombre exacto, o None si no existe
    nombre = nombre.strip().lower()
    for i, p in enumerate(paises):
        if p["nombre"].lower() == nombre:
            return i
    return None

# ── BÚSQUEDA ──────────────────────────────────────────────────────────────────

def buscar_pais(paises):
    # Busca países por coincidencia parcial en el nombre
    print("\n--- Buscar país ---")
    if not paises:
        print("No hay países cargados.")
        return
    texto = pedir_texto("Nombre o parte del nombre: ").lower()
    resultados = [p for p in paises if texto in p["nombre"].lower()]
    if not resultados:
        print("No se encontraron coincidencias.")
    else:
        mostrar_paises(resultados)

# ── FILTROS ───────────────────────────────────────────────────────────────────

def filtrar_continente(paises):
    # Filtra países por continente (ignora mayúsculas, minúsculas y tildes)
    print("\n--- Filtrar por continente ---")
    if not paises:
        print("No hay países cargados.")
        return
    ingreso = pedir_texto("Continente: ").lower()
    continente_usuario = ingreso.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    
    def normalizar(texto):
        return texto.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

    resultados = [p for p in paises if normalizar(p["continente"]) == continente_usuario]
    if not resultados:
        print("No se encontraron países en ese continente.")
    else:
        mostrar_paises(resultados)


def filtrar_poblacion(paises):
    # Filtra países por rango de población
    print("\n--- Filtrar por población ---")
    if not paises:
        print("No hay países cargados.")
        return
    minimo = pedir_entero_no_negativo("Población mínima: ")
    maximo = pedir_entero_no_negativo("Población máxima: ")
    if minimo > maximo:
        print("Error: el mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    if not resultados:
        print("No se encontraron países en ese rango.")
    else:
        mostrar_paises(resultados)


def filtrar_superficie(paises):
    # Filtra países por rango de superficie
    print("\n--- Filtrar por superficie ---")
    if not paises:
        print("No hay países cargados.")
        return
    minimo = pedir_entero_no_negativo("Superficie mínima (km²): ")
    maximo = pedir_entero_no_negativo("Superficie máxima (km²): ")
    if minimo > maximo:
        print("Error: el mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    if not resultados:
        print("No se encontraron países en ese rango.")
    else:
        mostrar_paises(resultados)
        
# ── ORDENAMIENTO ──────────────────────────────────────────────────────────────

def ordenar_paises(paises):
    # Ordena la lista por nombre, población o superficie (asc/desc)
    print("\n--- Ordenar países ---")
    if not paises:
        print("No hay países cargados.")
        return

    print("Ordenar por: 1. Nombre  2. Población  3. Superficie")
    opcion = input("Opción (1-3): ").strip()
    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if opcion not in campos:
        print("Opción no válida.")
        return
    campo = campos[opcion]

    print("Orden: 1. Ascendente  2. Descendente")
    orden = input("Opción (1-2): ").strip()
    if orden not in ("1", "2"):
        print("Opción no válida.")
        return
    descendente = orden == "2"

    # Para nombre usamos minúsculas para no distinguir mayúsculas
    clave = (lambda p: p["nombre"].lower()) if campo == "nombre" else (lambda p: p[campo])
    mostrar_paises(sorted(paises, key=clave, reverse=descendente))

# ── ESTADÍSTICAS ──────────────────────────────────────────────────────────────

def mostrar_estadisticas(paises):
    # Muestra estadísticas generales del dataset
    print("\n--- Estadísticas ---")
    if not paises:
        print("No hay países cargados.")
        return

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print(f"Total de países      : {len(paises)}")
    print(f"Mayor población      : {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Menor población      : {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio población   : {prom_pob:.2f}")
    print(f"Promedio superficie  : {prom_sup:.2f} km²")

    # Conteo por continente usando diccionario
    conteo = {}
    for p in paises:
        conteo[p["continente"]] = conteo.get(p["continente"], 0) + 1
    print("\nPaíses por continente:")
    for continente, cantidad in conteo.items():
        print(f"  {continente}: {cantidad}")

# ── PRESENTACIÓN ──────────────────────────────────────────────────────────────

def mostrar_paises(lista):
    # Imprime la lista de países en formato tabla
    print(f"\n{'Nombre':<25}{'Población':>15}{'Superficie':>15}{'Continente':>15}")
    print("-" * 70)
    for p in lista:
        print(f"{p['nombre']:<25}{p['poblacion']:>15}{p['superficie']:>15}{p['continente']:>15}")

# ── MENÚ PRINCIPAL ────────────────────────────────────────────────────────────

def mostrar_menu():
    print("\n" + "=" * 40)
    print("   GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 40)
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar por continente")
    print("5. Filtrar por población")
    print("6. Filtrar por superficie")
    print("7. Ordenar países")
    print("8. Estadísticas")
    print("9. Mostrar todos")
    print("10. Guardar en CSV")
    print("0. Salir")
    print("=" * 40)


def main():
    paises = cargar_paises(ARCHIVO)
    print(f"Se cargaron {len(paises)} países.")

    opciones = {
        "1": agregar_pais,
        "2": actualizar_pais,
        "3": buscar_pais,
        "4": filtrar_continente,
        "5": filtrar_poblacion,
        "6": filtrar_superficie,
        "7": ordenar_paises,
        "8": mostrar_estadisticas,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion in opciones:
            opciones[opcion](paises)
        elif opcion == "9":
            mostrar_paises(paises) if paises else print("No hay países cargados.")
        elif opcion == "10":
            if guardar_paises(paises, ARCHIVO):
                print("Guardado correctamente.")
        elif opcion == "0":
            if input("¿Guardar antes de salir? (s/n): ").strip().lower() == "s":
                guardar_paises(paises, ARCHIVO)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
