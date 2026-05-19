"""
Programa: Sistema de Inicio de Sesión
Propósito: Validar usuario y contraseña mediante una interfaz gráfica.
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
        messagebox.showinfo(
            "Acceso Correcto",
            "Bienvenido al sistema"
        )

    elif acceso_valido is False:
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )

    else:
        messagebox.showerror(
            "Error",
            "Se excedió el número máximo de usuarios"
        )


def iniciar_sesion():
    """Obtiene los datos desde la interfaz"""

    nombre_usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()

    acceso_valido = validar_credenciales(
        nombre_usuario,
        contrasena
    )

    mostrar_resultado(acceso_valido)


def crear_interfaz():
    """Crea la ventana principal"""

    global entrada_usuario, entrada_contrasena

    ventana = tk.Tk()

    # CAMBIO DE TÍTULO
    ventana.title("Sistema de Inicio de Sesión")

    # CAMBIO DE TAMAÑO Y COLOR
    ventana.geometry("420x320")
    ventana.configure(bg="#f0f7fa")

    # TÍTULO PRINCIPAL
    tk.Label(
        ventana,
        text="INICIO DE SESIÓN",
        font=("Arial", 16, "bold"),
        bg="#f0f7fa",
        fg="#1f3c88"
    ).pack(pady=15)

    # USUARIO
    tk.Label(
        ventana,
        text="Usuario",
        font=("Arial", 11),
        bg="#f0f7fa"
    ).pack(pady=5)

    entrada_usuario = tk.Entry(
        ventana,
        font=("Arial", 11)
    )
    entrada_usuario.pack(pady=5)

    # CONTRASEÑA
    tk.Label(
        ventana,
        text="Contraseña",
        font=("Arial", 11),
        bg="#f0f7fa"
    ).pack(pady=5)

    entrada_contrasena = tk.Entry(
        ventana,
        show="*",
        font=("Arial", 11)
    )
    entrada_contrasena.pack(pady=5)

    # CAMBIO DE BOTÓN
    tk.Button(
        ventana,
        text="INGRESAR",
        command=iniciar_sesion,
        bg="#3b82f6",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=20)

    ventana.mainloop()


def main():
    """Función principal"""
    crear_interfaz()


if __name__ == "__main__":
    main()
