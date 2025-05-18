import sqlite3

def crear_tabla():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT,
            fecha_lectura TEXT
        )
    ''')
    conn.commit()
    conn.close()

def agregar_libro():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    fecha = input("Ingrese la fecha de lectura (AAAA-MM-DD): ")
    cursor.execute("INSERT INTO libros (titulo, autor, genero, fecha_lectura) VALUES (?, ?, ?, ?)", (titulo, autor, genero, fecha))
    conn.commit()
    conn.close()
    print("Libro agregado correctamente.")

def modificar_libro():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    id_libro = int(input("Ingrese el ID del libro a modificar: "))
    nuevo_titulo = input("Ingrese el nuevo título (o presione Enter para no modificar): ")
    nuevo_autor = input("Ingrese el nuevo autor (o presione Enter para no modificar): ")
    nuevo_genero = input("Ingrese el nuevo género (o presione Enter para no modificar): ")
    nueva_fecha = input("Ingrese la nueva fecha (AAAA-MM-DD, o presione Enter para no modificar): ")

    query = "UPDATE libros SET "
    params = []
    if nuevo_titulo:
        query += "titulo = ?, "
        params.append(nuevo_titulo)
    if nuevo_autor:
        query += "autor = ?, "
        params.append(nuevo_autor)
    if nuevo_genero:
        query += "genero = ?, "
        params.append(nuevo_genero)
    if nueva_fecha:
        query += "fecha_lectura = ?, "
        params.append(nueva_fecha)
    
    query = query.rstrip(', ') + " WHERE id = ?"
    params.append(id_libro)

    cursor.execute(query, tuple(params))
    conn.commit()
    conn.close()
    print("Libro modificado correctamente.")


def mostrar_libros():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conn.close()
    if libros:
        print("-" * 30)
        print("Libros registrados:")
        print("-" * 30)
        for libro in libros:
            print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Fecha: {libro[4]}")
        print("-" * 30)
    else:
        print("No hay libros registrados.")


def eliminar_libro():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conn.commit()
    conn.close()
    print("Libro eliminado correctamente.")

def buscar_libro():
    conn = sqlite3.connect('libros.db')
    cursor = conn.cursor()
    criterio = input("Ingrese el criterio de búsqueda (título o autor): ")
    valor = input("Ingrese el valor a buscar: ")
    cursor.execute(f"SELECT * FROM libros WHERE {criterio} LIKE ?", ('%' + valor + '%',))
    libros = cursor.fetchall()
    conn.close()
    if libros:
        print("-" * 30)
        print("Resultados de la búsqueda:")
        print("-" * 30)
        for libro in libros:
            print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Fecha: {libro[4]}")
        print("-" * 30)
    else:
        print("No se encontraron libros que coincidan con la búsqueda.")


def menu():
    crear_tabla()  # Crea la tabla al iniciar el programa
    while True:
        print("\nMenú de gestión de libros:")
        print("1. Agregar un nuevo libro")
        print("2. Modificar un libro")
        print("3. Mostrar libros existentes")
        print("4. Eliminar un libro")
        print("5. Buscar un libro")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                agregar_libro()
            case "2":
                modificar_libro()
            case "3":
                mostrar_libros()
            case "4":
                eliminar_libro()
            case "5":
                buscar_libro()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()