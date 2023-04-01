import tkinter as tk
from tkinter import filedialog, messagebox
from functions import remove_duplicates, combo_extractor, compare_files, combo_combiner, domain_extractor, domain_sorter, user_pass_extractor


class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Herramientas para combos")
        self.master.config(bg="#293241")

        # Obtener el tamaño de la pantalla y calcular las coordenadas para centrar la ventana
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_coordinate = int((screen_width/2) - (400/2))
        y_coordinate = int((screen_height/2) - (500/2))

        self.master.geometry(f"400x500+{x_coordinate}+{y_coordinate}")
        self.master.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Seleccione una opción:", font=(
            "Arial", 14), fg="#E0FBFC", bg="#293241")
        option1_button = tk.Button(self.master, text="1. Eliminar duplicados", font=(
            "Arial", 12), width=30, command=remove_duplicates.main, bg="#FFA62B", fg="#293241")
        option2_button = tk.Button(self.master, text="2. Extraer combos", font=(
            "Arial", 12), width=30, command=combo_extractor.main, bg="#FF7F50", fg="#293241")
        option3_button = tk.Button(self.master, text="3. Comparar archivos", font=(
            "Arial", 12), width=30, command=compare_files.main, bg="#FF4C29", fg="#E0FBFC")
        option4_button = tk.Button(self.master, text="4. Combinar combos", font=(
            "Arial", 12), width=30, command=combo_combiner.main, bg="#008891", fg="#E0FBFC")
        option5_button = tk.Button(self.master, text="5. Extraer por dominio", font=(
            "Arial", 12), width=30, command=domain_extractor.main, bg="#66DE93", fg="#293241")
        option6_button = tk.Button(self.master, text="6. Ordenar por dominio", font=(
            "Arial", 12), width=30, command=domain_sorter.main, bg="#EE6C4D", fg="#E0FBFC")
        option7_button = tk.Button(self.master, text="6. Extraer LOGS User:Pass", font=(
            "Arial", 12), width=30, command=user_pass_extractor.main, bg="#EE6C4D", fg="#E0FBFC")
        exit_button = tk.Button(self.master, text="Salir", font=(
            "Arial", 12), width=10, command=self.master.quit, bg="#F2CC8F", fg="#293241")

        title_label.pack(pady=20)
        option1_button.pack(pady=10)
        option2_button.pack(pady=10)
        option3_button.pack(pady=10)
        option4_button.pack(pady=10)
        option5_button.pack(pady=10)
        option6_button.pack(pady=10)
        option7_button.pack(pady=10)
        exit_button.pack(side="bottom", pady=20)


root = tk.Tk()
app = MainApplication(master=root)
app.mainloop()
