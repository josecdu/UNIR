def ingresar_calificaciones():
    """Permite al usuario ingresar materias y sus calificaciones."""
    materias = []
    calificaciones = []

    print("Ingrese las materias y sus calificaciones.")
    print("Las calificaciones deben estar entre 0 y 10.")

    while True:
        nombre = input("\nIngrese el nombre de la materia: ").strip()
        while not nombre:
            print("El nombre de la materia no puede estar vacío.")
            nombre = input("Ingrese el nombre de la materia: ").strip()

        while True:
            try:
                calificacion = float(input("Ingrese la calificación: ").strip())
            except ValueError:
                print("La calificación debe ser un número.")
                continue

            if 0 <= calificacion <= 10:
                break
            print("La calificación debe estar entre 0 y 10.")

        materias.append(nombre)
        calificaciones.append(calificacion)

        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar not in {"s", "si", "sí", "y", "yes"}:
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """Devuelve el promedio de una lista de calificaciones."""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """Devuelve los índices de materias aprobadas y reprobadas."""
    aprobadas = []
    reprobadas = []

    for indice, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(indice)
        else:
            reprobadas.append(indice)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """Devuelve los índices de la calificación más alta y la más baja."""
    if not calificaciones:
        return None, None

    indice_max = max(range(len(calificaciones)), key=calificaciones.__getitem__)
    indice_min = min(range(len(calificaciones)), key=calificaciones.__getitem__)
    return indice_max, indice_min


def main():
    materias, calificaciones = ingresar_calificaciones()

    print("\n=== Resumen final ===")
    if not materias:
        print("No se ingresó ninguna materia.")
        print("Hasta pronto.")
        return

    print("Materias y calificaciones:")
    for indice, materia in enumerate(materias):
        print(f"{indice + 1}. {materia}: {calificaciones[indice]}")

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    print(f"\nPromedio general: {promedio:.2f}")
    print("Materias aprobadas:")
    if aprobadas:
        for indice in aprobadas:
            print(f"- {materias[indice]} ({calificaciones[indice]})")
    else:
        print("- Ninguna")

    print("Materias reprobadas:")
    if reprobadas:
        for indice in reprobadas:
            print(f"- {materias[indice]} ({calificaciones[indice]})")
    else:
        print("- Ninguna")

    print(f"\nMejor calificación: {materias[indice_max]} ({calificaciones[indice_max]})")
    print(f"Peor calificación: {materias[indice_min]} ({calificaciones[indice_min]})")
    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
