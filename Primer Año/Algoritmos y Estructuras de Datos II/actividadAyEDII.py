import os 
import json # IMPORTAMOS MODULO JSON, PARA PERMITIRNOS MANIPULAR DATOS EN FORMATO JSON.

# ARCHIVO ".JSON" DONDE SE GUARDARAN LOS CONTACTOS.
ARCHIVO = "agenda.json"

# FUNCION PARA CARGAR LOS CONTACTOS DESDE EL ARCHIVO.
def cargar_contactos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    return []

# FUNCION PARA GUARDAR LOS CONTACTOS EN EL ARCHIVO.
def guardar_contactos(contactos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(contactos, archivo, indent=4)

# MOSTRAR MENU.
def mostrar_menu():
    print("\n--- Agenda ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

# FUNCION QUE SIRVE PARA AGREGAR UN CONTACTO.
def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    print("¡Contacto agregado!")

# FUNCION PARA VER LOS CONTACTOS.
def ver_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
        return
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")

# FUNCION PARA MODIFICAR CONTACTOS.
def modificar_contacto(contactos):
    ver_contactos(contactos)
    try:
        indice = int(input("Seleccione el número del contacto a modificar: ")) - 1
        if 0 <= indice < len(contactos):
            contactos[indice]["nombre"] = input(f"Nuevo nombre ({contactos[indice]['nombre']}): ") or contactos[indice]["nombre"]
            contactos[indice]["telefono"] = input(f"Nuevo teléfono ({contactos[indice]['telefono']}): ") or contactos[indice]["telefono"]
            contactos[indice]["email"] = input(f"Nuevo email ({contactos[indice]['email']}): ") or contactos[indice]["email"]
            print("¡Contacto modificado!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

# FUNCION PARA ELIMINAR UN CONTACTO.
def eliminar_contacto(contactos):
    ver_contactos(contactos)
    try:
        indice = int(input("Seleccione el número del contacto a eliminar: ")) - 1
        if 0 <= indice < len(contactos):
            contactos.pop(indice)
            print("¡Contacto eliminado!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

# PROGRAMA PRINCIPAL.
def main():
    contactos = cargar_contactos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            ver_contactos(contactos)
        elif opcion == "3":
            modificar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            guardar_contactos(contactos)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
