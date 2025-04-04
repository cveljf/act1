estudiantes = {
    "Viginia Figuera": {"edad": 15, "materias": ["Matemática", "Geografia"]},
    "Camila López": {"edad": 16, "materias": ["Química", "Biología"]},
    "Emma Jara": {"edad": 18, "materias": ["Ciudadania", "Inglés"]}
}


def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materias = []
    while True:
        materia = input("Ingrese una materia aprobada (o escriba 'fin' para terminar): ")
        if materia.lower() == "fin":
            break
        materias.append(materia)
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print(f"El estudiante {nombre} ha sido agregado.")


def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes en la lista.")
        return
    for nombre, datos in estudiantes.items():
        print(f"Nombre: {nombre}")
        print(f"Edad: {datos['edad']}")
        print(f"Materias: {', '.join(datos['materias'])}")
        print("-" * 20)


def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"El estudiante {nombre} ha sido eliminado.")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.")


def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}")
        print(f"Edad: {datos['edad']}")
        print(f"Materias: {', '.join(datos['materias'])}")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.")


def buscar_palabra_clave():
    palabra_clave = input("Ingrese la palabra clave a buscar: ")
    encontrado = False
    for nombre in estudiantes:
        if palabra_clave.lower() in nombre.lower():
            print(f"La palabra clave '{palabra_clave}' se encuentra en el nombre del estudiante '{nombre}'.")
            encontrado = True
    if not encontrado:
        print(f"No se encontró la palabra clave '{palabra_clave}' en ningún nombre de estudiante.")


while True:
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Buscar estudiante")
    print("5. Buscar palabra clave en nombre")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            agregar_estudiante()
        case "2":
            mostrar_estudiantes()
        case "3":
            eliminar_estudiante()
        case "4":
            buscar_estudiante()
        case "5":
            buscar_palabra_clave()
        case "6":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")