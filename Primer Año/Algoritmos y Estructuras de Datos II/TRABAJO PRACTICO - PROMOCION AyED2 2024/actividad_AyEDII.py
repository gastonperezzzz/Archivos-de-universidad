import os
import json # IMPORTAMOS MODULO JSON PARA MANIPULAR LOS DATOS EN FORMATO JSON.

# CREACION DE UN ARCHIVO ".JSON" DONDE SE VAN A GUARDAR LOS DATOS.
ARCHIVO = "agenda_personal.json"

# FUNCION QUE SIRVE PARA CARGAR LOS DATOS DESDE EL ARCHIVO.
def cargar_agenda():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    return {"tareas": [], "eventos": [], "contactos": [], "notas": []}

# FUNCION PARA GUARDAR DATOS AGREGADOS EN EL ARCHIVO.
def guardar_agenda(agenda):
    with open(ARCHIVO, "w") as archivo:
        json.dump(agenda, archivo, indent=4)

# FUNCION QUE SIRVE PARA MOSTRAR EL MENU PRINCIPAL.
def mostrar_menu():
    print("\n--- Agenda Personal ---")
    print("1. Gestionar tareas pendientes")
    print("2. Gestionar eventos")
    print("3. Gestionar contactos")
    print("4. Gestionar notas")
    print("5. Salir")

# FUNCION PARA SELECCIONAR UNA SECCION DENTRO DE UNA OPCION DEL MENU (TAREAS, CONTACTOS, NOTAS, ETC).
def gestionar_seccion(agenda, seccion):
    print(f"\n--- {seccion.capitalize()} ---")
    print("1. Agregar")
    print("2. Ver")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Volver")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_item(agenda, seccion)
    elif opcion == "2":
        ver_items(agenda[seccion])
    elif opcion == "3":
        modificar_item(agenda, seccion)
    elif opcion == "4":
        eliminar_item(agenda, seccion)

# FUNCIONES GENERALES PARAA CONTROLAR SECCIONES.
def agregar_item(agenda, seccion):
    if seccion == "tareas":
        descripcion = input("Descripción de la tarea: ")
        fecha = input("Fecha límite (YYYY-MM-DD): ")
        prioridad = input("Prioridad (Baja/Media/Alta): ")
        agenda[seccion].append({"descripcion": descripcion, "fecha": fecha, "prioridad": prioridad})
    elif seccion == "eventos":
        titulo = input("Título del evento: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        hora = input("Hora (HH:MM): ")
        lugar = input("Lugar: ")
        agenda[seccion].append({"titulo": titulo, "fecha": fecha, "hora": hora, "lugar": lugar})
    elif seccion == "contactos":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agenda[seccion].append({"nombre": nombre, "telefono": telefono, "email": email})
    elif seccion == "notas":
        titulo = input("Título de la nota: ")
        contenido = input("Contenido: ")
        agenda[seccion].append({"titulo": titulo, "contenido": contenido})
    print(f"¡Nuevo {seccion[:-1]} agregado!")

# FUNCION PARA VER LOS ITEMS O ELEMENTOS QUE SE AGREGARON.
def ver_items(items):
    if not items:
        print("No hay elementos para mostrar.")
        return
    for i, item in enumerate(items, 1):
        print(f"{i}. {json.dumps(item, indent=2)}")

# FUNCION PARA ACTUALIZAR UN ITEM ANTERIORMENTE AGREGADO.
def modificar_item(agenda, seccion):
    ver_items(agenda[seccion])
    try:
        indice = int(input("Seleccione el número del elemento a modificar: ")) - 1
        if 0 <= indice < len(agenda[seccion]):
            for clave in agenda[seccion][indice]:
                nuevo_valor = input(f"{clave.capitalize()} ({agenda[seccion][indice][clave]}): ")
                if nuevo_valor:
                    agenda[seccion][indice][clave] = nuevo_valor
            print(f"{seccion[:-1].capitalize()} modificado!")
        else:
            print("Número inválido.")
    except ValueError:               # EXCEPCION PARA CONTROLAR LA ENTRADA DE DATOS.
        print("Entrada inválida.")

# FUNCION PARA ELIMINAR UN ELEMENTO O ITEM ANTERIORMENTE AGREGADO.
def eliminar_item(agenda, seccion):
    ver_items(agenda[seccion])
    try:
        indice = int(input("Seleccione el número del elemento a eliminar: ")) - 1
        if 0 <= indice < len(agenda[seccion]):
            agenda[seccion].pop(indice)
            print(f"{seccion[:-1].capitalize()} eliminado!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

# CONJUNTO DE FUNCIONES QUE CONFORMAN EL PROGRAMA PRINCIPAL.
def main():
    agenda = cargar_agenda()
    while True: # IMPLEMENTACION DE CICLO "DO-WHILE" PARA EVITAR EL CIERRE INVOLUNTARIO DEL PROGRAMA.
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            gestionar_seccion(agenda, "tareas")
        elif opcion == "2":
            gestionar_seccion(agenda, "eventos")
        elif opcion == "3":
            gestionar_seccion(agenda, "contactos")
        elif opcion == "4":
            gestionar_seccion(agenda, "notas")
        elif opcion == "5":
            guardar_agenda(agenda)
            print("¡Agenda guardada! Hasta luego.")
            break # INSTRUCCION UTILIZADA PARA SALIR DEL BUCLE VOLUNTARIAMENTE (CERRAR EL PROGRAMA), MEDIANTE LA SELECCION DE LA 5TA OPCION.
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
