import tkinter as tk
from PIL import Image, ImageTk
from formulario_login import FormularioLogin
from formulario_recuperarContrasena import FormularioRecuperarContrasena
from formulario_registro import FormularioRegistro

class VentanaPrincipal(tk.Tk):
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
        frame_logo = tk.Frame(self, bd=0, relief=tk.SOLID, padx=20, pady=20, bg='#3a7ff6')
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
            label = tk.Label(frame_logo, image=self.logo, bg='#3a7ff6')
            label.image = self.logo  # Mantener una referencia a la imagen
            label.pack(expand=True, fill=tk.BOTH)
        else:
            print("No se pudo cargar la imagen del logo.")

        # Crear el frame principal para el contenido, ocupando la mitad derecha de la pantalla
        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#ffffff')
        frame_form.grid(row=0, column=1, sticky="nsew")  # Ocupa la columna 1

        # Crear un frame para centrar el título y los botones
        frame_center = tk.Frame(frame_form, bg='#ffffff')
        frame_center.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el frame en el centro de frame_form

        # Crear el título "Inicio"
        title = tk.Label(frame_center, text="Inicio", font=('Times', 40), fg="#666a88", bg='#ffffff')  # Tamaño de la fuente reducido
        title.pack(pady=20)

        # Añadir los botones "Iniciar Sesión" y "Registrar" al frame_center
        tk.Button(frame_center, text="Iniciar Sesión", font=('Times', 20), bg='#3a7ff6', fg='#fff', width=15, padx=10, pady=5, borderwidth=2, relief='raised', command=self.abrir_login).pack(pady=15)
        tk.Button(frame_center, text="Registrar", font=('Times', 20), bg='#3a7ff6', fg='#fff', width=15, padx=10, pady=5, borderwidth=2, relief='raised', command=self.abrir_registro).pack(pady=15)
        

    def abrir_login(self):
        self.withdraw()
        app = FormularioLogin(self)
        app.mainloop()

    def abrir_registro(self):
        self.withdraw()
        app = FormularioRegistro(self)
        app.mainloop()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()

