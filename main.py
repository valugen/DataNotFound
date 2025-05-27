"""
¡Bienvenidos al sistema de destión de pasajes SkyRoute S.R.L!
SkyRoute S.R.L es un sistema desarrollado como parte de un proyecto academico,
con el propósito de simular el funcionamiento de una agencia de pasajes aéreos.
Aquí se pueden registrar diferentes tipos de clientes, tanto empresas como
personas físicas, gestionar destinos con sus respectivos costos y asociar cada
venta a un cliente y destino específico.
Además, incorpora la función del “botón de arrepentimiento”, que simula el
derecho del usuario a cancelar una compra dentro de un plazo determinado, en
línea con la normativa de defensa al consumidor.

Requisitos:
- Python version 3.9 en adelante.
Pasos a seguir:
1. Descargar el archivo SkyRoute.py.
2. Hacer doble click y abrir el archivo o correr en la terminal con: "python SkyRoute.py".
3. Seguir las instrucciones indicadas.

Grupo: DataNotFound

Integrantes:
- Cabrera, Gonzalo (41501046)
- Gesto, Valentina (41893604)
- Guevara, Gonzalo (38802553)
- Herrera, Bruno   (46592052)
- Theaux, Jimena   (40928800)

"""
#Variables

clientes = [] #lista para almacenar a los clientes
destinos = [] #lista para almacenar destinos
ventas = [] #lista para almacenar ventas

#menu prinicpal
while True:
    print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("==== Menu Principal ====")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Boton de Arrepentimiento")
    print("5. Consulta de datos")
    print("6. Acerca del Sistema")
    print("7. Salir")

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

            elif subopcion == "2": #solicita los datos del cliente y despues los guarda
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
            print("3. Modificar destino")
            print("4. Eliminar destino")
            print("5. Volver al Menu Principal")

            subopcion = input("Seleccione una opcion: ")

            if subopcion == "1":
                print("==== Destinos disponibles ====")
                print(destinos)

            elif subopcion == "2":
                print("==== Agregar nuevo destino ====")
                id_destino= input("Ingrese ID: ")
                pais_destino= input("Ingrese pais: ")
                ciudad_destino= input("Ingrese ciudad: ")
                costo_destino= input("Ingrese costo base: $ ")
                destino= {"id_destino": id_destino, "pais_destino": pais_destino, "ciudad_destino": ciudad_destino, "costo_destino": costo_destino}
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
            elif subopcion =="3": #Buscar destino para modificar
                id_destino = input("Ingrese ID del destino a modificar: ")

                for d in destinos: #Modificar ciudad
                   if d["id_destino"] == id_destino:
                        ciudad_vieja = ciudad_destino
                        d["ciudad_destino"] = input("Ingrese la nueva ciudad destino: ")
                        print(f"La ciudad {ciudad_vieja} fue actualizada a la ciudad {ciudad_destino} con éxito.")
                        break
                else:
                    print("Destino no encontrado.")

            elif subopcion == "4": #Eliminar un destino
                id_destino = input("Ingrese el ID del destino a eliminar: ")
                encontrado= False #Variable para comprobar si el destino existe

                for d in destinos:
                    if d ["id_destino"] == id_destino:
                        destinos.remove(d)
                        encontrado = True
                        print("Destino eliminado con éxito.")
                        break # Termina el bucle una vez que lo encuentra

                if not encontrado:
                    print("Destino no encontrado.")

            elif subopcion == "5":
                break # Salir del submenu 2

            else:
                print("Opcion inválida, intenta nuevamente.")

    elif opcion == "3": # Opcion gestionar ventas
        while True:
            print("==== Gestionar Ventas ====")
            print("1. Nueva venta")
            print("2. Historial de ventas")
            print("3. Modificar venta")
            print("4. Eliminar venta")
            print("5. Volver al Menu Principal")

            subopcion = input("Seleccione una opcion: ")

            if subopcion == "1": #Registrar una nueva venta

                cuit = input("Ingrese el CUIT del cliente: ")
                id_destino = input("Ingrese ID destino: ")
                fecha_venta = input ("Ingrese fecha de venta: ")

                #Verifica si el cliente y destino existen
                cliente_existe = any(c ["cuit"] == cuit for c in clientes)
                id_destino_existe = any(d["id_destino"] == id_destino for d in destinos)

                if not cliente_existe:
                   print("El cliente no está registrado.")
                elif not id_destino_existe:
                  print("ID destino no registrado.")
                else:
                   print("Venta registrada con éxito.")
                   venta = {"cliente": cuit, "destino": id_destino, "fecha": fecha_venta, "estado": "Activa"}
                   ventas.append(venta)
            elif subopcion == "2":
                print("==== Historial de ventas ====")
                print(ventas)

            elif subopcion == "3":
                print("==== Modificar venta ====")
                cuit = input("Ingrese el CUIT del cliente: ")
                id_destino = input("Ingrese ID destino: ")
                fecha_venta = input ("Ingrese fecha de venta: ")

                for v in ventas:
                    if v["cliente"] == cuit and v["destino"] == id_destino and v["fecha"] == fecha_venta:
                        v["estado"] = input("Ingrese nuevo estado: ")
                        print("Venta modificada con éxito.")
                        break
                    else:
                        print("Venta no encontrada.")

            elif subopcion == "4":
                print("==== Eliminar venta ====")
                cuit = input("Ingrese el CUIT del cliente: ")
                id_destino = input("Ingrese ID destino: ")
                fecha_venta = input ("Ingrese fecha de venta: ")

                for v in ventas:
                    if v["cliente"] == cuit and v["destino"] == id_destino and v["fecha"] == fecha_venta:
                        ventas.remove(v)
                        print("Venta eliminada con éxito.")
                        break
                else:
                    print("Venta no encontrada.")

            elif subopcion == "5":
                break # Salir del submenu 3

            else:
                print("Opcion inválida, intente nuevamente.")

    elif opcion == "4":  # Opción botón de arrepentimiento
      while True:
        print("==== Botón de arrepentimiento ====")
        print("1. Iniciar solicitud")
        print("2. Volver al menú principal")

        subopcion = input("Seleccione una opción: ")

        if subopcion == "1":
            print("Recuerde que solo podrá anular ventas con fecha igual o inferior a 60 días desde la compra.")
            cuit = input("Ingrese CUIT del cliente: ")
            ventas_cliente = []

            # Buscar ventas que coincidan con el CUIT
            for venta in ventas:
                if venta["cliente"] == cuit:
                    ventas_cliente.append(venta)

            # Verificar si se encontraron ventas
            if len(ventas_cliente) == 0:
                print("No se registran ventas con su número de CUIT.")
            else:
                print("Sus ventas registradas son:")
                for i, venta in enumerate(ventas_cliente):
                    print(f"{i+1}. Destino: {venta['destino']}, Fecha: {venta['fecha']}, Estado: {venta['estado']}")

                seleccion = input("Ingrese el número de la venta que desea anular: ")

                # Asegurarse de que la selección sea un número válido
                try:
                    seleccion = int(seleccion) - 1
                    if 0 <= seleccion < len(ventas_cliente):
                        venta_seleccionada = ventas_cliente[seleccion]
                        dias = int(input("Por favor, ingrese en números ¿Cuántos días pasaron desde la compra?: "))

                        if dias <= 60:
                            venta_seleccionada["estado"] = "Anulada"
                            print("La venta ha sido anulada correctamente. Un asesor se comunicará con usted.")
                        else:
                            print("No es posible anular la venta. Ya pasaron más de 60 días.")
                            print("Consulte bases y condiciones en nuestra web.")
                    else:
                        print("Selección inválida. Por favor, seleccione un número válido de la lista.")
                except ValueError:
                    print("Opción inválida, debe ingresar un número.")

        elif subopcion == "2":
            break  # Sale del submenu 4

        else:
            print("Opción inválida, intente nuevamente.")

    elif opcion == "5":
      while True:
        print("==== Consulta de datos ====")
        print("1. Clientes")
        print("2. Destinos")
        print("3. Ventas realizadas")
        print("4. Ventas anuladas")
        print("5. Volver al Menu Principal")

        subopcion = input("Seleccione una opcion: ")

        if subopcion == "1":
            print("==== Clientes ====")
            print(clientes)

        elif subopcion == "2":
            print("==== Destinos ====")
            print(destinos)

        elif subopcion == "3":
            print("=== Ventas realizadas ===")
            print("1. Clientes")
            print("2. Destino")
            print("3. Estado")
            print("4. Volver al menu principal")

            filtro = input("Seleccione la opción por la que desea filtrar: ")

            if filtro == "1":
                cuit = input("Ingrese el CUIT del cliente: ")
                for v in ventas:
                    if v["cliente"] == cuit:
                        print(v)
                    elif v["cliente"] != cuit:
                        print("No hay clientes registrados con ese CUIT.")

            elif filtro == "2":
                id_destino = input("Ingrese el ID del destino: ")
                for v in ventas:
                    if v["destino"] == id_destino:
                        print(v)

            elif filtro == "3":
                estado = input("Ingrese el estado (Activa/Anulada): ")
                for v in ventas:
                    if v["estado"].lower() == estado.lower():
                        print(v)

            elif filtro =="4":
                break

            else:
                print("Opción inválida, intente nuevamente.")

        elif subopcion == "3":
          print("=== Ventas realizadas ===")
          print("Seleccione la opción por la que desea filtra")
          print("")

        elif subopcion == "4":
          ventas_anuladas = [v for v in ventas if v["estado"] == "Anulada"]
          if ventas_anuladas:
            print("\n==== Ventas Anuladas ====")
            for v in ventas_anuladas:
                print(f'Cliente: {v["cliente"]}, Destino: {v["destino"]}, Fecha: {v["fecha"]}')
          else:
              print("No hay ventas anuladas registradas.")

        elif subopcion == "5":
            break  # Sale del submenu 5
        else:
            print("Opcion inválida, intente nuevamente.")

    elif opcion == "6":
        print("==== Acerca del sistema ====")
        print("""
¡Bienvenidos al sistema de destión de pasajes SkyRoute S.R.L!
SkyRoute S.R.L es un sistema desarrollado como parte de un proyecto academico,
con el propósito de simular el funcionamiento de una agencia de pasajes aéreos.
Aquí se pueden registrar diferentes tipos de clientes, tanto empresas como
personas físicas, gestionar destinos con sus respectivos costos y asociar cada
venta a un cliente y destino específico.
Además, incorpora la función del “botón de arrepentimiento”, que simula el
derechodel usuario a cancelar una compra dentro de un plazo determinado, en
línea con la normativa de defensa al consumidor.

""")

    elif opcion == "7": #Salir del programa
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion inválida, intente nuevamente.")
        