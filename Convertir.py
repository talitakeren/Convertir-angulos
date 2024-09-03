import math


def grados_a_radianes(grados):
    """Convierte un ángulo de grados a radianes."""
    return grados * (math.pi / 180)


def radianes_a_grados(radianes):
    """Convierte un ángulo de radianes a grados."""
    return radianes * (180 / math.pi)


def main():
    while True:
        print("\nConversor de Ángulos")
        print("1. Convertir grados a radianes")
        print("2. Convertir radianes a grados")
        print("3. Salir")

        opcion = input("Elige una opción (1/2/3): ")

        if opcion == "1":
            grados = float(input("Ingresa el ángulo en grados: "))
            radianes = grados_a_radianes(grados)
            print(f"{grados} grados son {radianes} radianes")

        elif opcion == "2":
            radianes = float(input("Ingresa el ángulo en radianes: "))
            grados = radianes_a_grados(radianes)
            print(f"{radianes} radianes son {grados} grados")

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
