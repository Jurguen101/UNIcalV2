import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraGeometrica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Geométrica")
        self.root.attributes('-fullscreen', True)  # Pantalla completa

        # Crear frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="x")
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(fill="both", expand=True)

        # Crear campos de entrada
        self.shape_label = tk.Label(self.input_frame, text="Figura:")
        self.shape_label.pack(side="left")
        self.shape_var = tk.StringVar()
        self.shape_var.set("Círculo")
        self.shape_menu = tk.OptionMenu(self.input_frame, self.shape_var, "Círculo", "Triángulo", "Rectángulo", "Paralelogramo")
        self.shape_menu.pack(side="left")

        self.param_label = tk.Label(self.input_frame, text="Parámetro:")
        self.param_label.pack(side="left")
        self.param_entry = tk.Entry(self.input_frame)
        self.param_entry.pack(side="left")

        self.calculate_button = tk.Button(self.input_frame, text="Calcular", command=self.calculate)
        self.calculate_button.pack(side="left")

        # Crear área de trazado con barras de desplazamiento
        self.canvas_frame = tk.Frame(self.plot_frame)
        self.canvas_frame.pack(fill="both", expand=True)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="white", scrollregion=(0, 0, 2000, 2000))
        self.canvas.pack(side="left", fill="both", expand=True)

        self.hbar = tk.Scrollbar(self.canvas_frame, orient="horizontal", command=self.canvas.xview)
        self.hbar.pack(side="bottom", fill="x")
        self.vbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.vbar.pack(side="right", fill="y")
        
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # Crear lista de historial
        self.history_listbox = tk.Listbox(self.plot_frame)
        self.history_listbox.pack(side="left", fill="both", expand=True)

        # Crear botón para borrar historial
        self.clear_button = tk.Button(self.plot_frame, text="Borrar Historial", command=self.clear_history)
        self.clear_button.pack(side="left", padx=10, pady=10)

        # Crear botón para salir
        self.exit_button = tk.Button(self.plot_frame, text="Salir", command=self.exit_program)
        self.exit_button.pack(side="left", padx=10, pady=10)

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("grid")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Dibujar líneas verticales
        for i in range(0, 2000, 20):
            self.canvas.create_line(i, 0, i, 2000, fill="lightgrey", tags="grid")

        # Dibujar líneas horizontales
        for i in range(0, 2000, 20):
            self.canvas.create_line(0, i, 2000, i, fill="lightgrey", tags="grid")

    def calculate(self):
        shape = self.shape_var.get()
        param = float(self.param_entry.get())

        self.canvas.delete("shape")
        self.draw_grid()

        if shape == "Círculo":
            area = math.pi * param ** 2
            circunferencia = 2 * math.pi * param
            self.plot_circle(param)
            self.history_listbox.insert("end", f"Círculo: Área={area:.2f}, Circunferencia={circunferencia:.2f}")
        elif shape == "Triángulo":
            base = param
            altura = param
            area = (base * altura) / 2
            perímetro = base + altura + math.sqrt(base ** 2 + altura ** 2)
            self.plot_triangle(base, altura)
            self.history_listbox.insert("end", f"Triángulo: Área={area:.2f}, Perímetro={perímetro:.2f}")
        elif shape == "Rectángulo":
            base = param
            altura = param
            area = base * altura
            perímetro = 2 * (base + altura)
            self.plot_rectangle(base, altura)
            self.history_listbox.insert("end", f"Rectángulo: Área={area:.2f}, Perímetro={perímetro:.2f}")
        elif shape == "Paralelogramo":
            base = param
            altura = param
            area = base * altura
            perímetro = 2 * (base + altura)
            self.plot_parallelogram(base, altura)
            self.history_listbox.insert("end", f"Paralelogramo: Área={area:.2f}, Perímetro={perímetro:.2f}")

    def clear_history(self):
        self.history_listbox.delete(0, "end")

    def exit_program(self):
        self.root.quit()

    def plot_circle(self, radio):
        x0, y0 = 1000 - radio, 1000 - radio
        x1, y1 = 1000 + radio, 1000 + radio
        self.canvas.create_oval(x0, y0, x1, y1, outline="black", fill="lightblue", tags="shape")
        self.canvas.create_text(1000, 1000, text=f"Radio={radio}", fill="black", tags="shape")
        self.canvas.xview_moveto((x0 - 500) / 2000)
        self.canvas.yview_moveto((y0 - 500) / 2000)

    def plot_triangle(self, base, altura):
        x0, y0 = 1000, 1000
        x1, y1 = x0 + base, y0
        x2, y2 = x0, y0 - altura
        self.canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline="black", fill="lightgreen", tags="shape")
        self.canvas.create_text((x0 + x1) / 2, y0 + 10, text=f"Base={base}", fill="black", tags="shape")
        self.canvas.create_text(x0 - 10, (y0 + y2) / 2, text=f"Altura={altura}", fill="black", tags="shape")
        self.canvas.xview_moveto((x0 + x1 / 2 - 500) / 2000)
        self.canvas.yview_moveto((y0 + y2 / 2 - 500) / 2000)

    def plot_rectangle(self, base, altura):
        x0, y0 = 1000, 1000
        x1, y1 = x0 + base, y0 + altura
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="lightcoral", tags="shape")
        self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=f"Base={base}", fill="black", tags="shape")
        self.canvas.create_text(x0 - 10, (y0 + y1) / 2, text=f"Altura={altura}", fill="black", tags="shape")
        self.canvas.xview_moveto((x0 + base / 2 - 500) / 2000)
        self.canvas.yview_moveto((y0 + altura / 2 - 500) / 2000)

    def plot_parallelogram(self, base, altura):
        x0, y0 = 1000, 1000
        x1, y1 = x0 + base, y0
        x2, y2 = x1 + altura, y1 + altura
        x3, y3 = x0 + altura, y0 + altura
        self.canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, outline="black", fill="lightyellow", tags="shape")
        self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=f"Base={base}", fill="black", tags="shape")
        self.canvas.create_text((x1 + x2) / 2, y1 + 10, text=f"Altura={altura}", fill="black", tags="shape")
        self.canvas.xview_moveto((x0 + base + altura / 2 - 500) / 2000)
        self.canvas.yview_moveto((y0 + altura / 2 - 500) / 2000)

root = tk.Tk()
calculadora = CalculadoraGeometrica(root)
root.mainloop()
