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
        self.root.geometry("300x200")

        self.lista_usuarios = [
            Usuario("admin", "1234"),
            Usuario("santiago", "abcd"),
            Usuario("user", "pass")
        ]

        self.crear_interfaz()

    def crear_interfaz(self):
        """Crea los elementos de la interfaz"""
        tk.Label(self.root, text="Usuario").pack(pady=5)
        self.entrada_usuario = tk.Entry(self.root)
        self.entrada_usuario.pack()

        tk.Label(self.root, text="Contraseña").pack(pady=5)
        self.entrada_contrasena = tk.Entry(self.root, show="*")
        self.entrada_contrasena.pack()

        tk.Button(self.root, text="Ingresar", command=self.iniciar_sesion).pack(pady=15)

    def iniciar_sesion(self):
        """Procesa el inicio de sesión"""
        nombre_usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        for usuario in self.lista_usuarios:
            if usuario.validar_acceso(nombre_usuario, contrasena):
                messagebox.showinfo("Acceso", "Acceso concedido")
                return

        messagebox.showerror("Acceso", "Acceso denegado")


def main():
    """Función principal"""
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()
