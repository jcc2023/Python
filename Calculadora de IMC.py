
# Esta calculadora de IMC funciona para personas de 20 o más años (la variable edad funciona como filtro). 
# Para niños y adolescentes es necesario considerar otras variables además del peso y la estatura en el cálculo del IMC.

edad = int(input("¿Cuál es su edad en años?\n"))

if edad < 20:
    print("\nAl ser menor de 20 años debes consultar la calculadora de IMC para niños y adolescentes")
    exit()

nombre = input("¿Cuál es su nombre?\n")
apellido_paterno = input("¿Cuál es su apellido paterno?\n")
apellido_materno = input("¿Cuál es su apellido materno?\n")
peso = float(input("Escriba su peso en Kg\n"))
estatura_centimetros = float(input("Escriba su estatura en centímetros\n"))

# Es necesario dividir la estatura entre 100 para que la unidad de medida sean metros y no centímetros.

estatura_metros = float(estatura_centimetros / 100)

# Se calcula el índice de masa corporal dividiendo la variable peso entre la estatura (medida en metros) elevada al cuadrado.

imc = float(peso / (estatura_metros)**2)

# Se imprimen en pantalla los datos indentificatorios del usuario y su IMC.

print("\nNombre: " + nombre.capitalize())
print("\nApellido paterno: " + apellido_paterno.capitalize())
print("\nApellido materno: " + apellido_materno.capitalize())
print("\nEdad: " + str(edad))
print("\nPeso: " + str(peso))
print("\nEstatura: " + str(estatura_centimetros) + " centímetros")
print("\nSu índice de masa corporal es: {:.1f} ".format(imc))

# Clasificación del IMC de acuerdo al valor obtenido en la calculadora e impresión en pantalla.

if imc < 18.5:
    print("\nSu índice de masa corporal indica que tiene bajo peso\n")
elif imc >= 18.5 and imc <= 24.9:
    print("\nSu índice de masa corporal indica que tiene peso normal\n")
elif imc >= 25 and imc <= 29.9:
    print("\nSu índice de masa corporal indica que tiene sobrepeso\n")
else:
    print("\nSu índice de masa corporal indica que tiene obesidad\n")
    
    
    





