
import unittest                           #Importamos unittest 
from fibo import fibonacci                #Importamos la funcion Fibonacci del archivo fibo.py


class Test(unittest.TestCase):           #definimos clase Test
      
    entrada = int(input('Inserta un numero \n'))        #Pedimos un numero por teclado 
    fibonacci(entrada)                                  #utilizamos el numero en la funcion
     
