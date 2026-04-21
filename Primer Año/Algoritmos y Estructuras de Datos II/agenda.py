import json  # Importamos el módulo json para manejar los datos en formato JSON

# Archivo donde se guardará la agenda
ARCHIVO_AGENDA = "agenda.json"

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("\n--- Menú de la Agenda ---")
    print("1. Agregar registro")
    print("2. Mostrar registros")
    print("3. Modificar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    return input("Elige una opción: ")

# Función para cargar los registros desde el archivo JSON
# Si el archivo no existe, devuelve una lista vacía
def cargar_agenda():
    try:
        with open(ARCHIVO_AGENDA, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  # Si el archivo no existe, devuelve una lista vacía

# Función para guardar los registros en el archivo JSON
def guardar_agenda(registros):
    with open(ARCHIVO_AGENDA, "w") as archivo:
        json.dump(registros, archivo, indent=4)  # Guardamos los registros en formato JSON con indentación

# Función para agregar un nuevo registro (nombre y teléfono) a la agenda
def agregar_registro():
    print("\n--- Agregar nuevo registro ---")
    nombre = input("Ingrese el nombre: ")  # Solicitamos el nombre
    telefono = input("Ingrese el número de teléfono: ")  # Solicitamos el número de teléfono
    
    # Cargamos los registros existentes del archivo
    registros = cargar_agenda()

    # Creamos un nuevo registro con el nombre y teléfono
    nuevo_registro = {"nombre": nombre, "telefono": telefono}

    # Agregamos el nuevo registro a la lista de registros
    registros.append(nuevo_registro)

    # Guardamos la lista de registros actualizada en el archivo
    guardar_agenda(registros)

    print("¡Registro agregado exitosamente!")

# Función para mostrar todos los registros almacenados en la agenda
def mostrar_registros():
    registros = cargar_agenda()  # Cargamos los registros del archivo
    if registros:
        print("\n--- Registros de la agenda ---")
        for i, registro in enumerate(registros, 1):  # Enumeramos los registros
            print(f"{i}. {registro['nombre']} - {registro['telefono']}")  # Imprimimos cada registro
    else:
        print("No hay registros en la agenda.")

# Función para modificar un registro existente en la agenda
def modificar_registro():
    registros = cargar_agenda()  # Cargamos los registros del archivo
    if not registros:
        print("No hay registros para modificar.")  # Si no hay registros, informamos al usuario
        return
    
    mostrar_registros()  # Mostramos los registros actuales
    try:
        # Solicitamos al usuario el índice del registro que quiere modificar
        indice = int(input("\nIngrese el número del registro a modificar: ")) - 1
        if 0 <= indice < len(registros):  # Verificamos que el índice sea válido
            # Solicitamos los nuevos valores para el registro
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            registros[indice] = {"nombre": nuevo_nombre, "telefono": nuevo_telefono}  # Modificamos el registro
            guardar_agenda(registros)  # Guardamos la lista de registros actualizada
            print("¡Registro modificado exitosamente!")
        else:
            print("Índice no válido.")  # Si el índice es incorrecto, informamos al usuario
    except ValueError:
        print("Por favor ingrese un número válido.")  # Si la entrada no es un número, mostramos un mensaje de error

# Función para eliminar un registro de la agenda
def eliminar_registro():
    registros = cargar_agenda()  # Cargamos los registros del archivo
    if not registros:
        print("No hay registros para eliminar.")  # Si no hay registros, informamos al usuario
        return
    
    mostrar_registros()  # Mostramos los registros actuales
    try:
        # Solicitamos al usuario el índice del registro que quiere eliminar
        indice = int(input("\nIngrese el número del registro a eliminar: ")) - 1
        if 0 <= indice < len(registros):  # Verificamos que el índice sea válido
            registros.pop(indice)  # Eliminamos el registro de la lista
            guardar_agenda(registros)  # Guardamos la lista de registros actualizada
            print("¡Registro eliminado exitosamente!")
        else:
            print("Índice no válido.")  # Si el índice es incorrecto, informamos al usuario
    except ValueError:
        print("Por favor ingrese un número válido.")  # Si la entrada no es un número, mostramos un mensaje de error

# Función principal que controla el flujo del programa
def main():
    while True:
        opcion = mostrar_menu()  # Mostramos el menú de opciones
        if opcion == "1":
            agregar_registro()  # Agregar un nuevo registro
        elif opcion == "2":
            mostrar_registros()  # Mostrar todos los registros
        elif opcion == "3":
            modificar_registro()  # Modificar un registro existente
        elif opcion == "4":
            eliminar_registro()  # Eliminar un registro
        elif opcion == "5":
            print("¡Hasta luego!")  # Salir del programa
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")  # Si la opción no es válida, mostramos un mensaje

# Ejecución del programa
if __name__ == "__main__":
    main()  # Ejecutamos la función principal cuando el script se ejecuta directamente
