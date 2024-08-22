import customtkinter as ctk
from tkinter import messagebox
from database import actualizar_contrasena

class FormularioRecuperarContrasena(ctk.CTkToplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.title("Recuperar Contraseña")

        # Establecer tema del sistema
        ctk.set_appearance_mode("system")  # Esto hace que el color se adapte al sistema operativo
        ctk.set_default_color_theme("blue")  # Puede ser cambiado a otro tema (dark-blue, green, etc.)

        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Ajustar la ventana para que ocupe toda la pantalla
        self.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        # Crear el marco principal
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(expand=True, fill='both')

        # Crear un frame para centrar el contenido
        content_frame = ctk.CTkFrame(main_frame)
        content_frame.pack(expand=True, pady=20, fill='both')  # Añadir relleno y expansión

        # Título
        ctk.CTkLabel(content_frame, text="Recuperar contraseña", font=('Times', 40)).pack(pady=15)

        # Correo electrónico
        ctk.CTkLabel(content_frame, text="Correo electrónico", font=('Times', 20)).pack(pady=10)
        self.email_entry = ctk.CTkEntry(content_frame, font=('Times', 20))
        self.email_entry.pack(pady=10)

        # Nueva contraseña
        ctk.CTkLabel(content_frame, text="Nueva contraseña", font=('Times', 20)).pack(pady=10)
        self.contrasena_entry = ctk.CTkEntry(content_frame, font=('Times', 20), show='*')
        self.contrasena_entry.pack(pady=10)

        # Botones
        ctk.CTkButton(content_frame, text="Actualizar contraseña", font=('Times', 20), width=200, command=self.recuperar_contrasena).pack(pady=10)
        ctk.CTkButton(content_frame, text="Volver", font=('Times', 20), width=200, command=self.volver).pack(pady=10)

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
