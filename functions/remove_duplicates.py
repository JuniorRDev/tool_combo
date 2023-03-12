import os
from tkinter import filedialog, messagebox, Tk


def remove_duplicates():
    
    # Abre una ventana de selección de archivo y permite al usuario seleccionar un archivo .txt
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    # Verifica que se ha seleccionado un archivo
    if not file_path:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
        return

    # Verifica que el archivo seleccionado existe
    if not os.path.isfile(file_path):
        messagebox.showerror("Error", "El archivo seleccionado no existe.")
        return

    # Abre el archivo y elimina las líneas duplicadas y en blanco
    with open(file_path, "r") as file:
        lines = set(line.strip() for line in file if line.strip())

    # Escribe las líneas únicas en el mismo archivo
    with open(file_path, "w") as file:
        file.write("\n".join(lines))

    # Muestra un mensaje de éxito
    messagebox.showinfo("Éxito", "Se han removido las líneas duplicadas y en blanco del archivo seleccionado.")

if __name__ == "__main__":
    remove_duplicates()
