"""
Programa: Sistema de acceso (Programación Estructurada con interfaz)
"""

import tkinter as tk
from tkinter import messagebox

# Constante
MAXIMO_USUARIOS = 3

# Datos
usuarios = {
    "admin": "1234",
    "santiago": "abcd",
    "user": "pass"
}


def validar_credenciales(nombre_usuario, contrasena):
    """Valida si las credenciales son correctas"""
    if len(usuarios) > MAXIMO_USUARIOS:
        return None

    if nombre_usuario in usuarios:
        if usuarios[nombre_usuario] == contrasena:
            return True
    return False


def mostrar_resultado(acceso_valido):
    """Muestra el resultado del acceso"""
    if acceso_valido is True:
        messagebox.showinfo("Acceso", "Acceso concedido")
    elif acceso_valido is False:
        messagebox.showerror("Acceso", "Acceso denegado")
    else:
        messagebox.showerror("Error", "Se excedió el número máximo de usuarios")


def iniciar_sesion():
    """Obtiene los datos desde la interfaz"""
    nombre_usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    acceso_valido = validar_credenciales(nombre_usuario, contrasena)
    mostrar_resultado(acceso_valido)


def crear_interfaz():
    """Crea la ventana principal"""
    global entrada_usuario, entrada_contrasena

    ventana = tk.Tk()
    ventana.title("Acceso - Estructurado")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Usuario").pack(pady=5)
    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.pack()

    tk.Label(ventana, text="Contraseña").pack(pady=5)
    entrada_contrasena = tk.Entry(ventana, show="*")
    entrada_contrasena.pack()

    tk.Button(ventana, text="Ingresar", command=iniciar_sesion).pack(pady=15)

    ventana.mainloop()


def main():
    """Función principal"""
    crear_interfaz()


if __name__ == "__main__":
    main()
