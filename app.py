import ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import os

# Caminho absoluto para a biblioteca .so
so_path = os.path.abspath('./libmathlib.so')
mathlib = ctypes.CDLL(so_path)

# Define os tipos de argumentos e retorno das funções
mathlib.quadratic_values.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int)]
mathlib.quadratic_values.restype = None

class QuadraticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Função Quadrática")
        self.create_widgets()

    def create_widgets(self):
        # Labels e entradas para os parâmetros da função quadrática
        ttk.Label(self.root, text="a:").grid(column=0, row=0)
        self.a_entry = ttk.Entry(self.root)
        self.a_entry.grid(column=1, row=0)

        ttk.Label(self.root, text="b:").grid(column=0, row=1)
        self.b_entry = ttk.Entry(self.root)
        self.b_entry.grid(column=1, row=1)

        ttk.Label(self.root, text="c:").grid(column=0, row=2)
        self.c_entry = ttk.Entry(self.root)
        self.c_entry.grid(column=1, row=2)

        ttk.Label(self.root, text="Início (x):").grid(column=0, row=3)
        self.start_entry = ttk.Entry(self.root)
        self.start_entry.grid(column=1, row=3)

        ttk.Label(self.root, text="Fim (x):").grid(column=0, row=4)
        self.end_entry = ttk.Entry(self.root)
        self.end_entry.grid(column=1, row=4)

        ttk.Label(self.root, text="Passo (x):").grid(column=0, row=5)
        self.step_entry = ttk.Entry(self.root)
        self.step_entry.grid(column=1, row=5)

        # Botão para gerar o gráfico
        self.plot_button = ttk.Button(self.root, text="Plotar Gráfico", command=self.plot_graph)
        self.plot_button.grid(column=0, row=6, columnspan=2)

        # Área para o gráfico
        self.figure = plt.Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(column=0, row=7, columnspan=2)

    def plot_graph(self):
        try:
            # Obtém os parâmetros da função quadrática
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            start = float(self.start_entry.get())
            end = float(self.end_entry.get())
            step = float(self.step_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
            return

        # Aloca memória para os valores
        num_points = int((end - start) / step) + 1
        values = (ctypes.c_double * num_points)()
        count = ctypes.c_int()

        # Chama a função C
        mathlib.quadratic_values(a, b, c, start, end, step, values, ctypes.byref(count))

        # Converte os dados retornados para numpy arrays
        x_values = np.arange(start, end + step, step)
        y_values = np.array(values[:count.value])

        # Limpa o gráfico anterior
        self.ax.clear()
        self.ax.plot(x_values, y_values, label=f'y = {a}x^2 + {b}x + {c}')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Gráfico da Função Quadrática')
        self.ax.legend()
        self.ax.grid(True)

        # Atualiza o gráfico
        self.canvas.draw()

# Configura e executa a aplicação
root = tk.Tk()
app = QuadraticApp(root)
root.mainloop()
