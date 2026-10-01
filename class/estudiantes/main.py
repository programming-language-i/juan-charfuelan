estudiantes = [
    {"nombre": "Andres", "edad": 20, "notas": [4.2, 4.5, 5]},
    {"nombre": "Ana", "edad": 21, "notas": [4.2, 4.5, 5]},
    {"nombre": "Sandra", "edad": 20, "notas": [4.5, 4.5, 5]},
]


def agregar_estudiante(estudiantes, nombre, edad, notas):
    estudiante = {"nombre": nombre, "edad": edad, "notas": notas}
    estudiantes.append(estudiante)


def mostrar_estudiantes(estudiantes):
    print(estudiantes)


def calcular_promedio(notas):
    pass


def buscar_estudiante(estudiantes, nombre):
    pass


def eliminar_estudiante(estudiantes, nombre):
    pass


def main():
    agregar_estudiante(estudiantes, "Carlos", 21, [5, 5, 5])
    mostrar_estudiantes(estudiantes)


if __name__ == "__main__":
    main()
