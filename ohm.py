# Programa para calcular la Ley de Ohm
print("Ley de Ohm")
print("Selecciona la opción:")
print("1 = Calcular Voltaje (V)")
print("2 = Calcular Corriente (I)")
print("3 = Calcular Resistencia (R)")

try:
    opcion = int(input("Opción: "))
    if opcion == 1:
        resistencia = float(input("Ingresa la resistencia (ohm): "))
        corriente = float(input("Ingresa la corriente (amperios): "))
        voltaje = resistencia * corriente
        print(f"Voltaje = {voltaje} V")
    elif opcion == 2:
        voltaje = float(input("Ingresa el voltaje (voltios): "))
        resistencia = float(input("Ingresa la resistencia (ohm): "))
        if resistencia == 0:
            print("Error: la resistencia no puede ser cero.")
        else:
            corriente = voltaje / resistencia
            print(f"Corriente = {corriente} A")
    elif opcion == 3:
        voltaje = float(input("Ingresa el voltaje (voltios): "))
        corriente = float(input("Ingresa la corriente (amperios): "))
        if corriente == 0:
            print("Error: la corriente no puede ser cero.")
        else:
            resistencia = voltaje / corriente
            print(f"Resistencia = {resistencia} ohm")
    else:
        print("Opción no válida.")
except ValueError:
    print("Error: ingresa valores numéricos válidos.")