# Crea un programa en Python que:
# Pida al usuario su peso y lo guarde en una variable

# Defina una constante con el valor de KG por libra

# Calcule el peso en libras

# Muestre por pantalla el peso en libras

peso = float(input("Dime tu peso en kg: "))
kg_por_libra = 0.45359237
peso_en_libras = peso / kg_por_libra
print (f"Tu peso en libras es : {peso_en_libras}")