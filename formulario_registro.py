import tkinter as tk
from tkinter import messagebox
from database import registrar_usuario

class FormularioRegistro(tk.Tk):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.title("Registrar Usuario")
        
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Ajustar la ventana para que ocupe toda la pantalla
        self.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        # Establecer fondo
        self.configure(bg='#ffffff')
        
        tk.Label(self, text="Registro", font=('Times', 40), fg="#666a88", bg='#ffffff').pack(pady=15)

        tk.Label(self, text="Nombre", font=('Times', 20), fg="#666a88", bg='#ffffff').pack(pady=10)
        self.nombre_entry = tk.Entry(self, font=('Times', 20))
        self.nombre_entry.pack(pady=10)

        tk.Label(self, text="Apellido", font=('Times', 20), fg="#666a88", bg='#ffffff').pack(pady=10)
        self.apellido_entry = tk.Entry(self, font=('Times', 20))
        self.apellido_entry.pack(pady=10)

        tk.Label(self, text="Correo", font=('Times', 20), fg="#666a88", bg='#ffffff').pack(pady=10)
        self.email_entry = tk.Entry(self, font=('Times', 20))
        self.email_entry.pack(pady=10)

        tk.Label(self, text="Contraseña", font=('Times', 20), fg="#666a88", bg='#ffffff').pack(pady=10)
        self.password_entry = tk.Entry(self, font=('Times', 20), show='*')
        self.password_entry.pack(pady=10)

        tk.Button(self, text="Registrar", font=('Times', 15), bg='#3a7ff6', fg='#fff', width=15, padx=10, pady=5, borderwidth=2, relief='raised', command=self.registrar).pack(pady=10)
        tk.Button(self, text="Volver", font=('Times', 15), bg='#3a7ff6', fg='#fff', width=15, padx=10, pady=5, borderwidth=2, relief='raised', command=self.volver).pack(pady=10)

    def registrar(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        mensaje = registrar_usuario(nombre, apellido, email, password)
        messagebox.showinfo("Registro", mensaje)

    def volver(self):
        self.destroy()
        if self.parent:
            self.parent.deiconify()

