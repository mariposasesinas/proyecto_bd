import customtkinter as ctk
from PIL import Image, ImageTk
from formulario_login import FormularioLogin
from formulario_recuperarContrasena import FormularioRecuperarContrasena
from formulario_registro import FormularioRegistro

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        # Ajustar la ventana para que ocupe toda la pantalla
        self.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        # Configurar la grilla principal de la ventana
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)  # Configura la columna izquierda
        self.grid_columnconfigure(1, weight=1)  # Configura la columna derecha

        # Crear el frame para el logo que ocupará la mitad izquierda de la pantalla
        frame_logo = ctk.CTkFrame(self, corner_radius=0, fg_color='#3a7ff6')
        frame_logo.grid(row=0, column=0, sticky="nsew")  # Ocupa la columna 0

        # Cargar y redimensionar la imagen directamente desde la carpeta 'imagenes'
        try:
            imagen = Image.open("polar.png")
            imagen = imagen.resize((300, 300), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error al cargar la imagen del logo: {e}")
            self.logo = None

        # Mostrar la imagen en el frame
        if self.logo:
            label = ctk.CTkLabel(frame_logo, image=self.logo, text="")
            label.image = self.logo  # Mantener una referencia a la imagen
            label.pack(expand=True, fill=ctk.BOTH)
        else:
            print("No se pudo cargar la imagen del logo.")
        ctk.set_appearance_mode("system")
        # Crear el frame principal para el contenido, ocupando la mitad derecha de la pantalla
        frame_form = ctk.CTkFrame(self, corner_radius=0)
        frame_form.grid(row=0, column=1, sticky="nsew")  # Ocupa la columna 1

        # Crear un frame para centrar el título y los botones
        frame_center = ctk.CTkFrame(frame_form)
        frame_center.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el frame en el centro de frame_form

        # Crear el título "Inicio"
        title = ctk.CTkLabel(frame_center, text="Inicio", font=ctk.CTkFont('Times', 40), text_color="#666a88")  # Tamaño de la fuente reducido
        title.pack(pady=20)

        # Añadir los botones "Iniciar Sesión" y "Registrar" al frame_center
        ctk.CTkButton(frame_center, text="Iniciar Sesión", font=ctk.CTkFont('Times', 20), fg_color='#3a7ff6', text_color='#fff', width=200, height=40, command=self.abrir_login).pack(pady=15)
        ctk.CTkButton(frame_center, text="Registrar", font=ctk.CTkFont('Times', 20), fg_color='#3a7ff6', text_color='#fff', width=200, height=40, command=self.abrir_registro).pack(pady=15)

    def abrir_login(self):
        self.withdraw()
        app = FormularioLogin(self)
        app.mainloop()

    def abrir_registro(self):
        self.withdraw()
        app = FormularioRegistro(self)
        app.mainloop()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Opcional: puedes cambiar a "Dark" o "Light"
    ctk.set_default_color_theme("blue")  # Puedes cambiar el tema de color
    app = VentanaPrincipal()
    app.mainloop()
    