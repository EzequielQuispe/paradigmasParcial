import csv
import os

def menu_usuario():
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    ARCHIVO_LEGAJO = "legajo.csv"
    ARCHIVO_DIAS = "dias.csv"

    while True:
        print("Ingrese una opción: \n1- Guardar datos. \n2- Ver dias de vacaciones. \n3- Salir.")
        opcion = input("")

        if opcion == "1":
            cargar_datos(ARCHIVO_LEGAJO, CAMPOS)
        if opcion == "2":
            vacaciones_usuarios(ARCHIVO_LEGAJO, ARCHIVO_DIAS)
        if opcion == "3":
            exit()
        else:
            menu_usuario()

def cargar_datos(archivo, campos):
    guardar = "si"
    lista_empleados = []
    while guardar == "si":
        empleado = {}

        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del empleado: ")
        lista_empleados.append(empleado)
        guardar = input("Desea agregar otro empleados? Si/No ")
        print(lista_empleados)

    try:
        archivo_existe = os.path.isfile(archivo)
        print(archivo_existe)
        if archivo_existe:
            opcion_doc = input("El archivo ya existe, que quiere hacer? \n1- Sobreescribir \n2- Modificar")
            if opcion_doc == "2":
                with open(archivo, 'a', newline='') as file:
                    file_guarda = csv.DictWriter(file, fieldnames=campos)
                    if not archivo_existe:
                        file_guarda.writeheader()
                    file_guarda.writerows(lista_empleados)
                return
            elif opcion_doc == "1":
                with open(archivo, 'w', newline='') as file:
                    file_guarda = csv.DictWriter(file, fieldnames=campos)
                    file_guarda.writeheader()
                    file_guarda.writerows(lista_empleados)
                return
        else:
            with open(archivo, 'w+', newline='') as file:
                file_guarda = csv.DictWriter(file, fieldnames=campos)
                file_guarda.writeheader()
                file_guarda.writerows(lista_empleados)
            return
    except IOError:
        print("Error al abrir el archivo")

def vacaciones_usuarios(legajos, dias):
    

menu_usuario()