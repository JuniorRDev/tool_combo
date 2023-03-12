import os
import re
from tkinter import filedialog, messagebox, Tk


def leer_archivo(ruta_archivo):
    """
    Lee un archivo y guarda cada línea que tiene formato email:pass en un conjunto (set).
    """
    with open(ruta_archivo, "r") as archivo:
        conjunto = {linea.strip() for linea in archivo if re.match(r"[^@]+@[^@]+\.[^@]+:.+", linea.strip())}
    return conjunto


def main():
    # Crear la ventana principal de tkinter
    root = Tk()
    root.withdraw()

    # Abrir el explorador de archivos para seleccionar el primer archivo
    ruta_archivo1 = filedialog.askopenfilename(title="Seleccionar el primer archivo")

    # Verificar si se seleccionó un archivo
    if not ruta_archivo1:
        print("No se seleccionó ningún archivo.")
        return

    # Leer el contenido del primer archivo y guardar cada línea que tiene formato email:pass en un conjunto (set).
    set1 = leer_archivo(ruta_archivo1)

    # Abrir el explorador de archivos para seleccionar el segundo archivo
    ruta_archivo2 = filedialog.askopenfilename(title="Seleccionar el segundo archivo")

    # Verificar si se seleccionó un archivo
    if not ruta_archivo2:
        print("No se seleccionó ningún archivo.")
        return

    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo2):
        print("El archivo seleccionado no existe.")
        return

    # Leer el contenido del segundo archivo y guardar cada línea que tiene formato email:pass en un conjunto (set).
    set2 = leer_archivo(ruta_archivo2)

    # Encontrar las líneas que están en uno u otro conjunto, pero no en ambos.
    diferentes = set1.symmetric_difference(set2)

    if len(diferentes) > 0:
        # Abrir un diálogo de selección de archivo para que el usuario elija la ubicación y el nombre del archivo de salida.
        ruta_salida = filedialog.asksaveasfilename(title="Seleccionar el archivo de salida", defaultextension=".txt")

        # Verificar si se seleccionó un archivo de salida
        if ruta_salida:
            # Escribir las líneas que se encontraron diferentes en el archivo de salida seleccionado.
            with open(ruta_salida, "w") as archivo_diferentes:
                archivo_diferentes.writelines(linea + "\n" for linea in diferentes)

            messagebox.showinfo("Completado", f"Se encontraron {len(diferentes)} líneas diferentes y se escribieron en el archivo:\n{ruta_salida}")
        else:
            print("No se seleccionó ningún archivo de salida.")
    else:
        messagebox.showinfo("Completado", "Los archivos son iguales.")


if __name__ == '__main__':
    main()
