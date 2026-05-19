"""
Programa: Sistema de acceso (POO con interfaz)
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
        self.root.title("Acceso - POO")

        # MODIFICACIÓN 1: Tamaño y color de ventana
        self.root.geometry("420x320")
        self.root.configure(bg="#0f172a")

        self.lista_usuarios = [
            Usuario("admin", "1234"),
            Usuario("santiago", "abcd"),
            Usuario("user", "pass")
        ]

        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea los elementos de la interfaz"""

        # Frame principal
        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(pady=30)

        # Título
        tk.Label(
            frame,
            text="INICIO DE SESIÓN",
            font=("Arial", 16, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=10)

        # Usuario
        tk.Label(
            frame,
            text="Usuario",
            font=("Arial", 11),
            bg="#0f172a",
            fg="white"
        ).pack(pady=5)

        self.entrada_usuario = tk.Entry(
            frame,
            font=("Arial", 11),
            width=25
        )
        self.entrada_usuario.pack()

        # Contraseña
        tk.Label(
            frame,
            text="Contraseña",
            font=("Arial", 11),
            bg="#0f172a",
            fg="white"
        ).pack(pady=5)

        self.entrada_contrasena = tk.Entry(
            frame,
            show="*",
            font=("Arial", 11),
            width=25
        )
        self.entrada_contrasena.pack()

        # MODIFICACIÓN 2: Botón personalizado
        tk.Button(
            frame,
            text="INGRESAR",
            command=self.iniciar_sesion,
            bg="#38bdf8",
            fg="white",
            font=("Arial", 11, "bold"),
            width=15
        ).pack(pady=20)

    def iniciar_sesion(self):
        """Procesa el inicio de sesión"""

        nombre_usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        for usuario in self.lista_usuarios:
            if usuario.validar_acceso(nombre_usuario, contrasena):
                messagebox.showinfo(
                    "Acceso",
                    f"Bienvenido {nombre_usuario}"
                )
                return

        messagebox.showerror(
            "Acceso",
            "Usuario o contraseña incorrectos"
        )


def main():
    """Función principal"""
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()
