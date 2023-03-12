import os
from datetime import datetime
from tkinter import filedialog, messagebox, simpledialog, Tk


def domain_extractor(combo, dominios):
    """
    Extrae las líneas del combo que corresponden a los dominios especificados.
    """
    lineas_dominio = []
    for linea in combo:
        for dominio in dominios:
            if dominio in linea:
                lineas_dominio.append(linea)
                break
    return lineas_dominio


def eliminar_duplicados(lineas):
    """
    Elimina las líneas duplicadas de una lista y las devuelve en el mismo orden.
    """
    lineas_sin_duplicados = []
    for linea in lineas:
        if linea not in lineas_sin_duplicados:
            lineas_sin_duplicados.append(linea)
    return lineas_sin_duplicados


def guardar_archivo(lineas):
    """
    Crea una carpeta con la fecha y hora actual y guarda un archivo con un nombre genérico y las líneas especificadas.
    """
    # Crear la carpeta con la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    carpeta = f"{fecha_hora_actual}"
    os.mkdir(carpeta)

    # Crear el archivo con un nombre genérico y las líneas especificadas
    nombre_archivo = "extraccion.txt"
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(lineas)

    return ruta_archivo


def main():
    # Crear la ventana principal de tkinter
    root = Tk()
    root.withdraw()

    # Pedir al usuario que ingrese los dominios separados por coma
    while True:
        dominios = simpledialog.askstring(title="Ingresar dominios", prompt="Ingrese los dominios del correo separados por coma (ej. @gmail.com, @hotmail.com):")
        
        # Verificar si se ingresó algún dominio
        if not dominios:
            print("No se ingresó ningún dominio.")
            return

        # Convertir los dominios a una lista y verificar si todos comienzan con "@"
        dominios = [dominio.strip() for dominio in dominios.split(",")]
        if not all(dominio.startswith("@") for dominio in dominios):
            messagebox.showerror("Error", "Todos los dominios deben comenzar con '@'.")
        else:
            break

    # Abrir el explorador de archivos para seleccionar el archivo combo
    ruta_combo = filedialog.askopenfilename(title="Seleccionar archivo combo")

    # Verificar si se seleccionó un archivo
    if not ruta_combo:
        print("No se seleccionó ningún archivo.")
        return

    # Leer las líneas del archivo combo
    with open(ruta_combo, "r") as archivo:
        combo = archivo.readlines()

    # Extraer las líneas del combo que corresponden a los dominios especificados
    lineas_dominio = domain_extractor(combo, dominios)

    # Verificar si se encontraron líneas para los dominios especificados
    if not lineas_dominio:
        print(f"No se encontraron líneas con los dominios {', '.join(dominios)}.")
        return

    # Eliminar las líneas duplicadas
    lineas_sin_duplicados = eliminar_duplicados(lineas_dominio)

    # Verificar si quedaron dominios para buscar
    if not lineas_sin_duplicados:
        print(f"No se encontraron líneas con los dominios {', '.join(dominios)}.")
        return

    #Guardar las líneas sin duplicados en un archivo con un nombre genérico en una carpeta con la fecha y hora actual
    lineas_sin_duplicados = list(set(lineas_sin_duplicados))
    ruta_archivo = guardar_archivo(lineas_sin_duplicados)

    # Mostrar un mensaje de éxito al usuario
    messagebox.showinfo("Extracción completada", f"Se encontraron {len(lineas_sin_duplicados)} líneas con los dominios {', '.join(dominios)}.\nSe guardó un archivo con el nombre {os.path.basename(ruta_archivo)} en la carpeta {os.path.dirname(ruta_archivo)}.")

if __name__ == '__main__':
    main()
