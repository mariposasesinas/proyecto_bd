import tkinter as tk
from tkinter import messagebox
from database import actualizar_contrasena

class FormularioRecuperarContrasena(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.title("Recuperar Contraseña")
        
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Ajustar la ventana para que ocupe toda la pantalla
        self.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")


        tk.Label(self, text="Correo electrónico", font=('Arial', 14)).pack(pady=10)
        self.email_entry = tk.Entry(self, font=('Arial', 14))
        self.email_entry.pack(pady=10)

        tk.Label(self, text="Nueva contraseña", font=('Arial', 14)).pack(pady=10)
        self.contrasena_entry = tk.Entry(self, font=('Arial', 14), show='*')
        self.contrasena_entry.pack(pady=10)

        tk.Button(self, text="Actualizar contraseña", font=('Arial', 14), command=self.recuperar_contrasena).pack(pady=20)
        tk.Button(self, text="Volver", command=self.volver).pack(pady=10)

    def recuperar_contrasena(self):
        email = self.email_entry.get()
        nueva_contrasena = self.contrasena_entry.get()

        if actualizar_contrasena(email, nueva_contrasena):
            messagebox.showinfo("Éxito", "Contraseña actualizada con éxito")
            self.volver()  # Regresa a la ventana de inicio de sesión
        else:
            messagebox.showerror("Error", "El correo electrónico no está registrado o hubo un error")
    
    def volver(self):
        self.destroy()  # Cierra la ventana de recuperación
        self.parent.deiconify()  # Muestra la ventana principal nuevamente

if __name__ == "__main__":
    app = FormularioRecuperarContrasena()
    app.mainloop()

