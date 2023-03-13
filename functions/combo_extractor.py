import tkinter as tk
from tkinter import filedialog, messagebox
import re

def is_email(text):
    """Verifica si el texto es un correo electrónico válido"""
    return re.match(r"[^@]+@[^@]+\.[^@]+", text)

def main():
    # Seleccionar archivo
    file_path = filedialog.askopenfilename(title="Seleccionar el archivo a extraer", defaultextension=".txt")
    if not file_path:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
        return # Salir si no se seleccionó ningún archivo
    # Pedir nombre para archivo de salida
    output_file = filedialog.asksaveasfilename(title="Seleccionar el archivo de salida", defaultextension='.txt')

    combos = []
    duplicates = set()
    line_count = 0
    duplicate_count = 0
    with open(file_path, "r", encoding="utf8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            email, *rest = line.split(":")
            if not is_email(email) or not rest:
                continue
            password = line.split(":")[-1].strip()
            combo = f"{email}:{password}"
            line_count += 1
            if combo in duplicates:
                duplicate_count += 1
                continue
            duplicates.add(combo)
            combos.append(combo)

    with open(output_file, "w", encoding="utf8") as file:
        file.write("\n".join(combos))

    # Mostrar mensaje con estadísticas
    total_count = len(combos)
    message = f"Se encontraron {line_count} líneas en el archivo.\n"
    if total_count == 0:
        message += "No se encontraron combos válidos."
    else:
        message += f"Se encontraron {total_count} combos válidos.\n"
        if duplicate_count > 0:
            message += f"Se eliminaron {duplicate_count} lineas duplicados."
    tk.messagebox.showinfo("Extracción de combos", message)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    main()