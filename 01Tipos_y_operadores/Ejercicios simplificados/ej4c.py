# Crea un programa en Python que:
# Pida al usuario su altura (en cm) y lo guarde en una variable

# Defina una constante con el valor de cm a pies

# Calcule la altura en pies

# Muestre por pantalla la altura en pies

altura = int(input("Dime tu altura en cm: "))

de_cm_a_pies = 0.03281
altura_en_pies = altura * de_cm_a_pies
print(f"Si tu altura en centimetros es {altura}, entonces tu altura en pies será: {altura_en_pies}")