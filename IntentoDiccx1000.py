def añadir_personas():
    personas = []  # Lista para almacenar los datos de varias personas
    salir = 'sí'  # Inicialización para entrar al bucle
    
    while salir == 'sí':  # Bucle que permite agregar múltiples personas
        nombre = input('Introduzca su Nombre: ')
        edad = int(input('Introduzca su Edad: '))
        
        # Validación de edad
        if edad < 18:
            print('¡Error! Eres menor de edad.')
            continue  # Si es menor de edad, no sigue pidiendo datos y vuelve al inicio del bucle
        
        cargo = input('Introduzca su Cargo: ')
        persona = {
            'Nombre': nombre,
            'Edad': edad,
            'Cargo': cargo
        }
        
        # Validación de cargo
        if cargo.lower() == 'jefe':  # Ignora mayúsculas y minúsculas en la entrada
            empleados = int(input('¿Cuántas personas tiene a cargo?: '))
            persona['Personas a cargo'] = empleados  # Añadimos el campo solo si es 'Jefe'
        
        personas.append(persona)  # Agregamos el diccionario 'persona' a la lista
        
        salir = input('¿Deseas agregar otra persona? (sí/no): ').lower()
        # Si el usuario ingresa 'no', el bucle se termina

    return personas

def mostrar_diccionario(personas):
    print("\nDirectorio de Personas:")
    for persona in personas:
        print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Cargo: {persona['Cargo']}")
        if 'Personas a cargo' in persona:
            print(f"Personas a cargo: {persona['Personas a cargo']}")
    if not personas:  # Mensaje si la lista está vacía
        print("No se ha registrado ninguna persona.")
    else:
        print("¡Gracias por colaborar con el programa!")

# Llamadas a las funciones
personas = añadir_personas()
mostrar_diccionario(personas)
