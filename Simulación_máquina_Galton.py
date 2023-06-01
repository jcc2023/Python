""""
El siguiente código genera resultados de lanzamientos de canicas,
los almacena en una lista y luego genera un histograma 
de las sumas de los resultados.

"""
"""
La primera parte del código es la importación de las librerías necesarias:
random y matplotlib.pyplot. La librería random se utiliza para generar
números aleatorios y matplotlib.pyplot se utiliza para crear gráficos.

"""

import random
import matplotlib.pyplot as plt

"""
En lo que sigue se define la función generar_resultados(). 
Esta función se encarga de generar una lista con los resultados de lanzamientos de canicas.
Utiliza un ciclo while para controlar que se realicen la cantidad de lanzamientos de canicas
establecidos, en este caso, 3000. Dentro del ciclo, se genera una lista llamada
lista_resultados que contiene 12 números aleatorios entre 0 y 1
(representando los resultados de lanzar una canica, donde 0 sería "izquierda"
y 1 sería "derecha"). Luego, esta lista se agrega a la lista resultados. 
Finalmente, se incrementa el contador en 1 en cada iteración del ciclo.
Al final, la función retorna la lista resultados
con todos los resultados de los lanzamientos.

"""
def generar_resultados():  
    resultados = []
    contador = 0
    while contador < 3000:
        lista_resultados = [random.randint(0, 1) for _ in range(12)]
        resultados.append(lista_resultados)
        contador += 1
    return resultados

"""
A continuación, se define la función graficar_histograma(resultados).
Esta función recibe como argumento la lista de resultados de lanzamientos
de canicas generada anteriormente. La función calcula la suma de cada
lista de resultados utilizando una comprensión de lista. 
Crea una lista llamada sumas que contiene las sumas de cada lista de resultados.
Luego, utiliza la función hist() de matplotlib.pyplot para generar un histograma de las sumas.
Se especifica el rango de bins (de 0 a 12), se alinean a la izquierda, se establece el ancho
de las barras y se agregan etiquetas al eje x, al eje y y al título del gráfico.
Finalmente, se muestra el gráfico utilizando la función show() de matplotlib.pyplot.

"""

def graficar_histograma(resultados):

    # Calcula la suma de cada lista de resultados
    sumas = [sum(lista) for lista in resultados]

    # Grafica el histograma
    plt.hist(sumas, bins=range(13), align='left', rwidth=0.8)
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.title('Simulación de la máquina de Galton')
    plt.xticks(range(13))
    plt.show()

"""
Después de definir las funciones, se llama a la función generar_resultados()
para generar la lista de resultados de lanzamientos de canicas y se guarda
en la variable resultados.

Por último, se llama a la función graficar_histograma(resultados) para generar
y mostrar el histograma de los resultados de lanzamientos de canicas.

"""

# Genera los resultados de las canicas
resultados = generar_resultados()

# Llama a la función para generar y graficar los resultados
graficar_histograma(resultados)
