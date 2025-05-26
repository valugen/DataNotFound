
#Archivo main.py que contenga: 
# Un encabezado con:
    #El propósito del sistema.
    #Cómo instalar y ejecutar el programa.
    #Datos de los integrantes del grupo (nombre, apellido y DNI).
#El menú de opciones.
#Control de flujo de acciones a realizar según la opción seleccionada (sin modularización).

#grupo: DataNotFound

clientes = [] #lista para almacenar a los clientes
destinos = [] #lista para almacenar destinos
ventas = [] #lista para almacenar ventas


#menu prinicpal
while True: 
    print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes") 
    print ("==== Menu Principal ====")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Historial de Ventas")
    print("5. Boton de Arrepentimiento")
    print("6. Reporte General")
    print("7. Acerca del Sistema")
    print("8. Salir")

    #entrada para el usuario al menu principal
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1": #opcion de gestionar clientes
        while True:
            print("==== Gestionar Clientes ====")
            print("1. Ver Clientes")
            print("2. Agregar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menu Principal")
            
            subopcion = input("Seleccione una opcion: ")
            
            if subopcion == "1": #muestra a todos los clientes registrados (si todo esta bien..)
                print("Clientes registrados: ", clientes) #mostrar los clientes en la memoria
                
            elif subopcion == "2": #solicita los datos del cliente y dsp los guarda
                razon_social = input("Razon social: ")
                cuit = input("CUIT: ")
                correo = input("correo: ")
                cliente = {"razon_social": razon_social, "cuit": cuit, "correo": correo}
                clientes.append(cliente)
                while True: #Muestra y confirma los datos cargados
                        print(cliente)
                        print("Los datos son correctos?")
                        print("1. Si")
                        print("2. No")
                        subopcion = input("Seleccione una opcion: ")

                        if subopcion == "1":
                            print("Cliente agregado con éxito!")
                            break

                        elif subopcion == "2":
                            clientes.remove(cliente)
                            print("El cliente no ha sido agregado")
                            break
                        else:
                            print("Opcion inválida, intenta nuevamente.")
                
            elif subopcion == "3": #buscar al cliente por cuit para dsp modificar
                cuit = input("CUIT del cliente a modificar: ")
                
                for c in clientes:
                    if c["cuit"] == cuit:
                        c["razon_social"] = input("nueva razon social: ")
                        c["correo"] = input("nuevo correo:")
                        print("El cliente fue modificado con éxito")
                        break
                else:
                    print("Cliente no encontrado")

            elif subopcion == "4": #busca a un cliente y lo borra de la lista si es que hay
                cuit = input("Ingrese el cuit del cliente a eliminar: ")
                encontrado= False #Variable para comprobar si el cliente existe

                for c in clientes:
                    if c ["cuit"] == cuit:
                        clientes.remove(c)
                        encontrado = True
                        print("Cliente eliminado con éxito.")
                        break # Termina el bucle una vez que lo encuentra
                if not encontrado:
                    print("Cliente no encontrado.")
            elif subopcion == "5":
                break # Salir del submenu 1
            
            else:
                print("Opcion inválida, intenta nuevamente.")

    elif opcion == "2": # Opcion gestionar Destinos
        while True:
            print("==== Gestionar Destinos ====")
            print("1. Destinos disponibles ")
            print("2. Agregar destino")
            print("3. Eliminar destino")
            print("4. Volver al Menu Principal")

            subopcion = input("Seleccione una opcion: ")

            if subopcion == "1":
                print(destinos)

            elif subopcion == "2":
                print("==== Agregar nuevo destino ====")
                id_destino= input("Ingrese ID: ")
                fecha_destino= input("Ingrese fecha: ")
                hora_destino= input("Ingrese hora: ")
                destino= {id_destino,fecha_destino,hora_destino}
                destinos.append(destino)
                while True:
                    print(destino)
                    print("Los datos son correctos?")
                    print("1. Si")
                    print("2. No")
                    subopcion = input("Seleccione una opcion: ")
                    if subopcion == "1":
                        print("Destino agregado con éxito!")
                        break
                    elif subopcion == "2":
                        destinos.remove(destino)
                        print("Destino no agregado.")
                        break
            
            elif subopcion == "3":
                print("Destino eliminado con éxito!")
            
            elif subopcion == "4":
                break # Salir del submenu 2

            else:
                print("Opcion inválida, intenta nuevamente.")
    
    elif opcion == "3": # Opcion gestionar ventas
        while True:
            print("==== Gestionar Ventas ====")
            print("1. Historial de Ventas ")
            print("2. ")
            print("3. Volver al Menu Principal")

            subopcion = input("Seleccione una opcion: ")

            if subopcion == "1":
                print("Selecciono la opcion 1")

            elif subopcion == "2": 
                print("Selecciono la opcion 2")  

            elif subopcion == "3":
                break # Salir del submenu 3
            else:
                print("Opcion inválida, intente nuevamente.")

    elif opcion == "5": # Opcion boton de arrepentimiento
        while True:
            print("==== Botón de arrepentiemiento ====")
            print("1. Iniciar solicitud")
            print("2. Salir")

            subopcion = input("Seleccione una opcion: ")

            if subopcion == "1":
                print("Solicitud cargada con éxito!")  
            elif subopcion == "2":
                break
            else:
                print("Opcion inválida, intente nuevamente.")


    elif opcion == "8": #Salir del programa
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion inválida, intente nuevamente.")

