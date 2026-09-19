print("------ Asistente de Evaluación Física ------")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso_Kg = float(input("Ingrese su peso en Kg: "))
horas_Ejercicio_Semana = int(input("Ingrese la horas de ejercicio por semana: "))

calorias_Quemadas_x_semana = horas_Ejercicio_Semana * 350

if edad < 18:
    print("Categoria: Juvenil.")
else:
    print("Categoria: Adulto.")


# evaluar sedentarismo

if horas_Ejercicio_Semana >= 3:
    print("Estado: Fisicamente Activo.")
else:
    print("Estado: Requiere mayor actividad fisica")


# resumen
print(f"Usuario: {nombre}")
print(f"Calorias quemadas por semana: {calorias_Quemadas_x_semana} calorias.")
