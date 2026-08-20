#Nombre: Jose Francisco Gonzalez Rosales
#Matricula: al05052257
#Fecha: Miercoles 19 de agosto del 2026
#precios
precio_menor_3años = 0
precio_menor = 30
precio_mayor = 45
#descuentos
descuento_adulto_mayor= 0.12
descuento_estudiante_y_profesor = 0.10
personas = int(input("¿Cuantas personas son? : "))
total_general = 0
for p in range (1, personas + 1):
    print(f"Persona {p}")
    edad_persona = int(input(f"dame la edad de la persona {p} : "))
    if edad_persona < 3:
        print("Menor de 3 años, entrada gratis.")
        continue

    elif edad_persona <= 17:
        precio = precio_menor

    else:
        precio = precio_mayor

    tipo= input("¿Que tipo de visitante eres? (adulto mayor , profesor , estudiante , otro)")
    if edad_persona >= 60 and tipo == "adulto mayor":
        descuento = precio * descuento_adulto_mayor
        porcentaje = 12

    elif tipo == "profesor" or tipo == "estudiante":
        descuento = precio * descuento_estudiante_y_profesor
        porcentaje = 10

    else:
        descuento = 0
        porcentaje = 0

    total = precio - descuento
    print(f"Precio : ${precio:.2f}")
    print(f"Descuento: {porcentaje:.2f}%")
    print(f"Monto del descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    total_general = total_general + total

   
   

print(f"Total general: ${total_general:.2f}")
