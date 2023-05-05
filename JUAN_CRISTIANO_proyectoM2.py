'''
Se crea una función que cuenta las letras de las palabras ingresadas por el
usuario, además controla que la palabra tenga entre 4 y 8 letras.
La función realiza la impresión en pantalla de la cantidad de letras que tiene
la palabra y en caso de que tenga menos de 4 o más de 8 letras cuantas letras le hacen falta
o sobran para estar dentro del rango establecido.

'''
def contador_de_letras():
    palabra = input("Ingrese una palabra que tenga entre 4 y 8 letras\n")
    cantidad_de_letras = len(palabra)
    if cantidad_de_letras >= 4 and cantidad_de_letras <=8:
        print("\nLa palabra tiene: " + str(cantidad_de_letras) + " letras, por lo tanto es correcta.")
    elif cantidad_de_letras < 4:
        print("\nHacen falta letras solo tiene: " + str(cantidad_de_letras))
    else:
        print("\nSobran letras, tiene: " + str(cantidad_de_letras))


    
'''
Se crea una función que en base a 2 números de entrada, coordenadas,
identifica en cuál de los 4 cuadrantes se encuentra el punto. El programa
verifica que ninguna coordenada sea 0.

'''
  

def encuentra_el_cuadrante():

    valor_de_x = int(input("\nIngrese un número distinto de 0 para el eje x\n"))
    valor_de_y = int(input("\nIngrese un número distinto de 0 para el eje y\n"))

    if valor_de_x > 0 and valor_de_y > 0:
             print("\nEl punto se ubica en el cuadrante I")
    elif valor_de_x < 0 and valor_de_y > 0:
            print("\nEl punto se ubica en el cuadrante II")
    elif valor_de_x < 0 and valor_de_y < 0:
            print("\nEl punto se ubica en el cuadrante III")
    elif valor_de_x > 0 and valor_de_y < 0:
            print("\nEl punto se ubica en el cuadrante IV")
    else:
          print("\nDebe ingresar números distintos de 0")
  
contador_de_letras() 
encuentra_el_cuadrante()


       
        
        

        
        
        
        
        
            
       
        

        

    
           

    

    
    
    


        
    


