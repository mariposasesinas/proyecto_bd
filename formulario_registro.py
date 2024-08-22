import customtkinter as ctk
from tkinter import messagebox
from database import registrar_usuario

class FormularioRegistro(ctk.CTk):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.title("Registrar Usuario")
        
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
        ctk.CTkLabel(content_frame, text="Registro", font=('Times', 40)).pack(pady=15)

        # Nombre
        ctk.CTkLabel(content_frame, text="Nombre", font=('Times', 20)).pack(pady=10)
        self.nombre_entry = ctk.CTkEntry(content_frame, font=('Times', 20))
        self.nombre_entry.pack(pady=10)

        # Apellido
        ctk.CTkLabel(content_frame, text="Apellido", font=('Times', 20)).pack(pady=10)
        self.apellido_entry = ctk.CTkEntry(content_frame, font=('Times', 20))
        self.apellido_entry.pack(pady=10)

        # Correo
        ctk.CTkLabel(content_frame, text="Correo", font=('Times', 20)).pack(pady=10)
        self.email_entry = ctk.CTkEntry(content_frame, font=('Times', 20))
        self.email_entry.pack(pady=10)

        # Contraseña
        ctk.CTkLabel(content_frame, text="Contraseña", font=('Times', 20)).pack(pady=10)
        self.password_entry = ctk.CTkEntry(content_frame, font=('Times', 20), show='*')
        self.password_entry.pack(pady=10)

        # Botones
        ctk.CTkButton(content_frame, text="Registrar", font=('Times', 15), width=200, command=self.registrar).pack(pady=10)
        ctk.CTkButton(content_frame, text="Volver", font=('Times', 15), width=200, command=self.volver).pack(pady=10)

    def registrar(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        mensaje = registrar_usuario(nombre, apellido, email, password)
        messagebox.showerror("Registro", mensaje) 

    def volver(self):
        self.destroy()
        if self.parent:
            self.parent.deiconify()


if __name__ == "__main__":
    app = FormularioRegistro()
    app.mainloop()
