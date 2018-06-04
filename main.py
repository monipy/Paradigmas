# !/usr/local/bin/python 3.6.4
"""
Módulo Main: Programa principal (controlador).

Trabajo Práctico - Paradigmas de la Programación
Registro de Empleados- Ejecute "ayuda" para más información
"""
from empleado import Empleado
from estante import Estante
from repl import REPL
from repl import strip


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": self.salir
        }
        archivo = "empleado.db"
        introduccion = strip(__doc__)
        self.empleado = Estante(archivo)
        if not self.empleado.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, cedula, nombre, apellido, telefono, salario):
        """
        Agrega un registro de empleado.

        cedula   -- Documento de identidad del empleado. Se usará como clave.
        nombre   -- Nombre del empleado.
        apellido -- Apellido del empleado.
        telefono -- Teléfono del contacto.
        salario  -- Importe de Saalario del empleado
        """
        self.empleado[cedula] = Empleado(cedula, nombre, apellido, telefono, salario)

    def borrar(self, cedula):
        """
        Borra un registro de empleado.

        cedula -- Cedula del empleado que se desea borrar.
        """
        del self.empleado[cedula]

    def mostrar(self, cedula):
        """
        Retorna un registro de un empleado.

        cedula -- Cedula del empleado que se desea mostrar.
        """
        return self.empleado[cedula]

    def listar(self):
        """
        Retorna un generador con todos los registros de empleados.

        Este comando no requiere de parámetros.
        """
        return (self.empleado[cedula]
                for cedula in sorted(self.empleado))

    def buscar(self, cadena):
        """
        Retorna un generador con los registros que contienen una cadena.

        cadena -- Cedula del empleado que se desea buscar.
        """
        return (self.empleado[cedula]
                for cedula in sorted(self.empleado)
                if cadena in cedula)

    def ayuda(self, comando=None):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [parámetro3] [parámetro4][..]\n" + \
                     "Comandos: " + \
                     ", ".join(sorted(self.comandos.keys()))
        return salida

    def salir(self):
        """
        Sale de la aplicación.
        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()
