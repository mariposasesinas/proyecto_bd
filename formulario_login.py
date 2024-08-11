import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
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

        main_frame = tk.Frame(self, bg='#ffffff')  # Usar blanco claro
        main_frame.pack(expand=True, fill='both')

        # Título
        title = tk.Label(main_frame, text="Iniciar Sesión", font=('Times', 40), fg="#666a88", bg='#ffffff')  # Usar blanco claro
        title.pack(pady=15)
        '''
        # Frame para la imagen del logo
        logo_frame = tk.Frame(main_frame, bg='#ffffff')  # Usar blanco claro
        logo_frame.pack(pady=10)
        
        # Cargar y mostrar la imagen del logo
        try:
            img = Image.open("polar.png")  # Cambiado para usar la imagen en la misma carpeta
            img = img.resize((100, 100), Image.LANCZOS)
            logo = ImageTk.PhotoImage(img)

            logo_label = tk.Label(logo_frame, image=logo, bg='#ffffff')  # Usar blanco claro
            logo_label.image = logo  # Evita que la imagen sea recolectada por el GC
            logo_label.pack()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
            '''
        # Frame para el formulario de inicio de sesión
        form_frame = tk.Frame(main_frame, bg='#ffffff')  # Usar blanco claro
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Correo electrónico", font=('Times', 20), fg="#666a88", bg='#ffffff').pack(pady=15)
        self.email_entry = tk.Entry(form_frame, font=('Times', 20))
        self.email_entry.pack(pady=15)

        tk.Label(form_frame, text="Contraseña", font=('Times', 20), fg="#666a88", bg='#ffffff').pack(pady=15)
        self.contrasena_entry = tk.Entry(form_frame, font=('Times', 20), show='*')
        self.contrasena_entry.pack(pady=15)

        tk.Button(form_frame, text="Iniciar Sesión", command=self.login, font=('Times', 20), bg='#3a7ff6', fg='#fff', width=15).pack(pady=15)
        tk.Button(form_frame, text="Volver", command=self.volver, font=('Times', 20), bg='#3a7ff6', fg='#fff', width=15).pack(pady=15)
        tk.Button(form_frame, text="Olvidé mi contraseña", font=('Times', 20), bg='#3a7ff6', fg='#fff', width=15, command=self.abrir_recuperar_contrasena).pack(pady=15)

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


