# !/usr/local/bin/python 3.6.4
"""
Módulo Empleado: Clase principal (modelo).

Trabajo Práctico - Paradigmas de la Programación
"""


class Empleado:
    """Registro de empleados."""

    def __init__(self, cedula, nombre, apellido, telefono, salario):
        """Constructor: Inicializa propiedades de instancia."""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.salario = salario

    def __str__(self):
        """Cadena de representación."""
        return "{}: {}".format(self.cedula, self.nombre, self.apellido, self.telefono, self.salario)

def main():
    """Función principal (ejemplo de uso)."""
    empleado = {}

    empleado["3757986"] = Empleado("3757986", "Monica", "Gonzalez", "222-333", "5000000")
    empleado["3202643"] = Empleado("3202643", "Julio", "Gonzalez", "444-555", "6000000")
    empleado["1234567"] = Empleado("1234567", "Santi", "Gonzalez", "666-777", "7000000")

    for clave in empleado:
        print(empleado[clave])


if __name__ == "__main__":
    main()
