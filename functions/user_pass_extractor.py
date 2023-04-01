import re
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime


def extract_credentials(line):
    match = re.search(
        r"https://miclaro\.claro\.com\.do.*?(?: |:)([\w.@]+)(?: |:)(\S+)", line
    )
    if match:
        return match.group(1), match.group(2)
    else:
        return None


def process_file(file_path, output_file, not_extracted_file):
    with open(file_path, "r", encoding="utf-8") as input_file, open(
        output_file, "w", encoding="utf-8"
    ) as out_file, open(not_extracted_file, "w", encoding="utf-8") as not_out_file:
        for line in input_file:
            credentials = extract_credentials(line)
            if credentials:
                out_file.write(f"{credentials[0]}:{credentials[1]}\n")
            else:
                not_out_file.write(line)


def main():
    # Seleccionar archivo
    file_path = filedialog.askopenfilename(
        title="Seleccionar el archivo a extraer", defaultextension=".txt")
    if not file_path:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
        return  # Salir si no se seleccionó ningún archivo

    # crear una carpeta con el nombre de la función si no existe
    function_name = "extraer_user_pass"
    folder_path = f"./{function_name}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # crear una carpeta con la fecha actual y un número secuencial
    current_date = datetime.now().strftime("%Y-%m-%d")
    seq_num = 1
    while True:
        subfolder_name = f"{current_date}_{seq_num}"
        subfolder_path = f"{folder_path}/{subfolder_name}"
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)
            break
        seq_num += 1

    # generar los nombres de los archivos de salida con el número secuencial
    filename = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{subfolder_path}/{filename}_extraido_{seq_num}.txt"
    not_extracted_file = f"{subfolder_path}/{filename}_no_extraido_{seq_num}.txt"

    process_file(file_path, output_file, not_extracted_file)


if __name__ == "__main__":
    main()
