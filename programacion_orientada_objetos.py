""
Programa: Sistema de Inicio de Sesión
Propósito: Validar acceso usando objetos y una interfaz gráfica.
"""

import tkinter as tk
from tkinter import messagebox


class Usuario:
    """Clase que representa un usuario"""

    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def validar_acceso(self, nombre_usuario, contrasena):
        """Valida las credenciales"""
        return (
            self.nombre_usuario == nombre_usuario and
            self.contrasena == contrasena
        )


class Aplicacion:
    """Clase principal de la aplicación"""

    def __init__(self, root):
        self.root = root

        # CAMBIO DEL TÍTULO DE LA VENTANA
        self.root.title("Sistema de Inicio de Sesión")

        self.root.geometry("350x250")
        self.root.configure(bg="#f4f6f7")

        self.lista_usuarios = [
            Usuario("admin", "1234"),
            Usuario("santiago", "abcd"),
            Usuario("user", "pass")
        ]

        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea los elementos de la interfaz"""

        titulo = tk.Label(
            self.root,
            text="INICIO DE SESIÓN",
            font=("Arial", 16, "bold"),
            bg="#f4f6f7",
            fg="#2c3e50"
        )
        titulo.pack(pady=10)

        tk.Label(
            self.root,
            text="Usuario",
            font=("Arial", 11),
            bg="#f4f6f7"
        ).pack(pady=5)

        self.entrada_usuario = tk.Entry(self.root, font=("Arial", 11))
        self.entrada_usuario.pack(pady=5)

        tk.Label(
            self.root,
            text="Contraseña",
            font=("Arial", 11),
            bg="#f4f6f7"
        ).pack(pady=5)

        self.entrada_contrasena = tk.Entry(
            self.root,
            show="*",
            font=("Arial", 11)
        )
        self.entrada_contrasena.pack(pady=5)

        # CAMBIO DEL TEXTO Y ESTILO DEL BOTÓN
        tk.Button(
            self.root,
            text="INICIAR SESIÓN",
            command=self.iniciar_sesion,
            bg="#3b82f6",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(pady=20)

    def iniciar_sesion(self):
        """Procesa el inicio de sesión"""

        nombre_usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        for usuario in self.lista_usuarios:
            if usuario.validar_acceso(nombre_usuario, contrasena):
                messagebox.showinfo(
                    "Acceso Correcto",
                    f"Bienvenido {nombre_usuario}"
                )
                return

        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )


def main():
    """Función principal"""

    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()
