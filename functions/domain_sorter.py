import os
from datetime import datetime
from tkinter import filedialog, messagebox


def domain_sorter():
    # Seleccionar archivo
    file_path = filedialog.askopenfilename(title="Seleccionar el archivo a clasificar", defaultextension=".txt")
    if not file_path:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
        return  # Salir si no se seleccionó ningún archivo

    # Crear carpeta para guardar archivos clasificados
    now = datetime.now()
    folder_name = f"sorter_{now.strftime('%Y-%m-%d_%H-%M-%S')}"
    os.mkdir(folder_name)

    # Contar líneas del archivo
    total_lines = sum(1 for line in open(file_path, "r", encoding="utf8", errors="ignore"))

    # Leer archivo y clasificar combos por dominio
    domain_dict = {}
    with open(file_path, "r", encoding="utf8", errors="ignore") as f:
        processed_lines = 0
        for line in f:
            email, password = line.strip().split(":")
            domain = email.split("@")[-1]
            combo = f"{email}:{password}"
            if domain not in domain_dict:
                domain_dict[domain] = []
            domain_dict[domain].append(combo)
            processed_lines += 1

            # Mostrar progreso
            progress = processed_lines / total_lines * 100
            print(f"Procesando combos... {progress:.2f}%", end="\r")

    # Escribir combos clasificados en archivos separados por dominio
    for domain, combos in domain_dict.items():
        file_path = os.path.join(folder_name, f"{domain}.txt")
        with open(file_path, "w", encoding="utf8") as file:
            file.write("\n".join(combos))

    # Mostrar mensaje de éxito
    message = f"Se clasificaron los combos por dominio y se guardaron en la carpeta {folder_name}."
    messagebox.showinfo("Clasificación de combos", message)


if __name__ == "__main__":
    domain_sorter()
