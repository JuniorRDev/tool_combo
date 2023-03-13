import os
import re
from tkinter import filedialog, messagebox, Tk

def combinar_archivos(rutas_archivos):
    """
    Combina los contenidos de varios archivos y elimina las líneas repetidas y vacías.
    """
    # Crear un conjunto (set) vacío para almacenar las líneas únicas
    lineas_unicas = set()

    # Iterar sobre las rutas de los archivos y agregar sus líneas únicas al conjunto
    for ruta_archivo in rutas_archivos:
        with open(ruta_archivo, "r") as archivo:
            lineas_archivo = {linea.strip() for linea in archivo if re.match(r"[^@]+@[^@]+\.[^@]+:.+", linea.strip())}
            lineas_unicas.update(lineas_archivo)

    return lineas_unicas


def main():
    # Crear la ventana principal de tkinter
    root = Tk()
    root.withdraw()

    # Abrir el explorador de archivos para seleccionar varios archivos
    rutas_archivos = filedialog.askopenfilenames(title="Seleccionar multiples archivos por combinar (Asegurate que esten todos los combos en la misma carpeta)")

    # Verificar si se seleccionó al menos un archivo
    if not rutas_archivos:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
        return
    else:
        # Combinar los contenidos de los archivos seleccionados y eliminar las líneas repetidas y vacías
        lineas_unicas = combinar_archivos(rutas_archivos)

        # Permitir que el usuario escriba el nombre del archivo de salida
        ruta_salida = filedialog.asksaveasfilename(title="Guardar archivo combinado", defaultextension=".txt")

        # Verificar si se seleccionó un archivo de salida
        if ruta_salida:
            # Escribir las líneas únicas en el archivo de salida seleccionado
            with open(ruta_salida, "w") as archivo_salida:
                archivo_salida.writelines(linea + "\n" for linea in sorted(lineas_unicas) if linea.strip())

            messagebox.showinfo("Completado", f"Se combinaron {len(rutas_archivos)} archivos y se escribieron {len(lineas_unicas)} líneas únicas en el archivo:\n{ruta_salida}")
        else:
            messagebox.showerror("Error","No se seleccionó o dió nombre para crear un nuevo archivo de salida.")


if __name__ == '__main__':
    main()
