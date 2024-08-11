import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            user='root', password='', host='localhost', database='mydatabase', port='3306'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectarse a MySQL: {e}")
        return None

def registrar_usuario(nombre, apellido, email, password):
    # Verifica que todos los campos están completos
    if not nombre or not apellido or not email or not password:
        return "Todos los campos son obligatorios"

    conexion = conectar_base_datos()
    if conexion and conexion.is_connected():
        try:
            cursor = conexion.cursor()

            # Verifica si el correo electrónico ya existe
            cursor.execute("SELECT * FROM Usuario WHERE email = %s", (email,))
            if cursor.fetchone() is not None:
                return "El correo electrónico ya está registrado"

            # Inserta el nuevo usuario
            sql = "INSERT INTO Usuario (nombre, apellido, email, passwordd) VALUES (%s, %s, %s, %s)"
            valores = (nombre, apellido, email, password)
            cursor.execute(sql, valores)
            conexion.commit()
            return "Usuario registrado correctamente"

        except Error as e:
            return f'Error al guardar los datos: {e}'

        finally:
            if conexion.is_connected():
                conexion.close()
    else:
        return 'No se pudo establecer la conexión a la base de datos'

def iniciar_sesion(email, password):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Verificar credenciales del usuario
            query = "SELECT * FROM Usuario WHERE email = %s AND passwordd = %s"
            cursor.execute(query, (email, password))
            if cursor.fetchone():
                return True
            else:
                return False
        except Error as e:
            print(f"Error al iniciar sesión: {e}")
            return False
        finally:
            conexion.close()

def actualizar_contrasena(email, nueva_contrasena):
    # Verificar que los campos no sean nulos o vacíos
    if not email or not nueva_contrasena:
        print("Error: El correo electrónico y la nueva contraseña no pueden estar vacíos.")
        return False

    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Verificar si el correo electrónico existe en la base de datos
            cursor.execute("SELECT * FROM Usuario WHERE email = %s", (email,))
            if cursor.fetchone():
                # Actualizar la contraseña
                cursor.execute("UPDATE Usuario SET passwordd = %s WHERE email = %s", (nueva_contrasena, email))
                conexion.commit()
                return True
            else:
                print("Error: El correo electrónico no existe.")
                return False
        except Error as e:
            print(f"Error al actualizar la contraseña: {e}")
            return False
        finally:
            conexion.close()
    return False


