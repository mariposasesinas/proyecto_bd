import tkinter as tk
from tkinter import messagebox
from database import iniciar_sesion
from formulario_recuperarContrasena import FormularioRecuperarContrasena

class FormularioLogin(tk.Tk):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.title("Iniciar Sesión")
        
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Ajustar la ventana para que ocupe toda la pantalla
        self.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")


        tk.Label(self, text="Correo electrónico", font=('Arial', 14)).pack(pady=10)
        self.email_entry = tk.Entry(self, font=('Arial', 14))
        self.email_entry.pack(pady=10)

        tk.Label(self, text="Contraseña", font=('Arial', 14)).pack(pady=10)
        self.contrasena_entry = tk.Entry(self, font=('Arial', 14), show='*')
        self.contrasena_entry.pack(pady=10)

        tk.Button(self, text="Iniciar Sesión", command=self.login).pack(pady=20)
        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)
        tk.Button(self, text="Olvidé mi contraseña", font=('Arial', 14), command=self.abrir_recuperar_contrasena).pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.contrasena_entry.get()

        # Validar que los campos no estén vacíos
        if not email or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if iniciar_sesion(email, password):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.destroy()
            # Aquí puedes abrir la ventana principal
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def volver(self):
        self.destroy()
        if self.parent:
            self.parent.deiconify()

    def abrir_recuperar_contrasena(self):
        self.withdraw()
        recuperar_contrasena = FormularioRecuperarContrasena(self)
        recuperar_contrasena.mainloop()

