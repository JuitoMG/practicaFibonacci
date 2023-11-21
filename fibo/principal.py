
import unittest                           #Importamos unittest 
from fibo import fibonacci                #Importamos la funcion Fibonacci del archivo fibo.py


class Test(unittest.TestCase):           #definimos clase Test

   def test_comprobacióm_fibonacci(self):    #Esta función hará la comprobación
    
    #Definimos variables posicion y valor para que nos pida los números a comprobar
    
    posicion = int(input('Introduce la posicion de la sucesion Fibonacci que quieres comprobar \n'))
    valor = int(input('Introduce el valor que debería tener esa posicion \n'))

    #Ejecutamos la comprobacion

    self.assertEqual (fibonacci(posicion), valor)

unittest.main()  #Esto ejecuta las funciones tipo test

