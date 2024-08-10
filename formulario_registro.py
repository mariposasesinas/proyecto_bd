import tkinter as tk
from tkinter import messagebox
from database import registrar_usuario

class FormularioRegistro(tk.Tk):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("Registrar Usuario")
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        self.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        tk.Label(self, text="Registro", font=('Times', 20)).pack(pady=20)

        tk.Label(self, text="Nombre").pack(pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        tk.Label(self, text="Apellido").pack(pady=5)
        self.apellido_entry = tk.Entry(self)
        self.apellido_entry.pack(pady=5)

        tk.Label(self, text="Correo").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Contraseña").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Registrar", command=self.registrar).pack(pady=20)
        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)

    def registrar(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        mensaje = registrar_usuario(nombre, apellido, email, password)
        messagebox.showinfo("Registro", mensaje)

    def volver(self):
        self.destroy()
        self.parent.deiconify()
