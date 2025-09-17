# Crea un programa en Python que:
# Pida al usuario el radio de una esfera y lo guarde en una variable

# Calcule su área

# Muestre por pantalla el área de la esfera
import math

radio = float(input("Dime el radio de una esfera : "))
area = 4*math.pi*(radio**2)
print (f"El area de la esfera es = {round(area,2)}cm^2")