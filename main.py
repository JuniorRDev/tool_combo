import sys
from tkinter import filedialog, messagebox, Tk
from functions import remove_duplicates, combo_extractor, compare_files, combo_combiner, domain_extractor, domain_sorter


def main():
    # Crear la ventana principal de tkinter
    root = Tk()
    root.withdraw()

    # Mostrar el menú de opciones
    print("Seleccione una opción:")
    print("1. Eliminar duplicados")
    print("2. Extraer combos")
    print("3. Comparar archivos")
    print("4. Combinar combos")
    print("5. Extraer por dominio")
    print("6. Ordenar por dominio")

    # Leer la opción seleccionada por el usuario
    opcion = input("Opción seleccionada: ")

    # Ejecutar el módulo correspondiente según la opción seleccionada
    if opcion == "1":
        remove_duplicates.main()
    elif opcion == "2":
        combo_extractor.extract_combos()
    elif opcion == "3":
        compare_files.main()
    elif opcion == "4":
        combo_combiner.main()
    elif opcion == "5":
        domain_extractor.main()
    elif opcion == "6":
        domain_sorter.main()
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
