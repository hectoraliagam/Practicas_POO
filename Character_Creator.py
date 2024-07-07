class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    def __str__(self):
        return f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}"
    def __add__(self,otro):
        nuevo_nombre = self.nombre +'-'+ otro.nombre
        nueva_fuerza = self.fuerza + otro.fuerza
        nueva_velocidad = self.velocidad + otro.velocidad
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)

def try_except(prompt):
    try:
        valor = int(input(prompt))
        return valor
    except ValueError:
        pass


cantidad = []
running = True
while running:
    print("------------------")
    print("CARACTER CREATOR")
    print("------------------")
    print("1. Crear personaje")
    print("2. Fusionar personajes")
    print("3. Mostrar personajes")
    print("4. Cerrar")
    opc = try_except("Seleccione una opción: ")
    running1 = True
    while running1:
        if opc == 1:
            print("------------------")
            nombre = input("Ingrese el nombre del personaje: ")
            fuerza = try_except("Ingrese la fuerza del personaje: ")
            velocidad = try_except("Ingrese la velocidad del personaje: ")
            personaje = Personaje(nombre,fuerza,velocidad)
            print("------------------")
            print("Personaje creado con éxito!")
            print(personaje)
            cantidad.append(personaje)
            running1 = False
        elif opc == 2:
            print("------------------")
            if len(cantidad) >= 2:
                num_personaje_1 = try_except("Ingresa el número de la lista del personaje a fusionar: ")
                num_personaje_2 = try_except("Ingresa el número de la lista del otro personaje: ")
                personaje_1 = cantidad[num_personaje_1-1]
                personaje_2 = cantidad[num_personaje_2-1]
                fusionar = personaje_1 + personaje_2
                print("------------------")
                print("Personajes fusionados con éxito!")
                print(fusionar)
                cantidad.append(fusionar)
            else:
                print("Mínimo 2 personajes para fusionar")
            running1 = False
        elif opc == 3:
            print("------------------")
            print("Personajes creados:")
            if len(cantidad) > 0:
                for x in enumerate(cantidad):
                    print("------------------")
                    print(x[1])
            else:
                print("------------------")
                print(cantidad)
                print("No tiene personajes en su lista")
            running1 = False
        elif opc == 4:
            print("------------------")
            running1 = False
            running = False
        else:
            running1 = False

# reto completado :D