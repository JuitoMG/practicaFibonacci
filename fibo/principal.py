
import unittest                           #Importamos unittest 
from fibo import fibonacci                #Importamos la funcion Fibonacci del archivo fibo.py


class Test(unittest.TestCase):           #definimos clase Test
      
   def test_comprobacióm_fibonacci(self):    #Esta función hará la comprobación
    self.assertEqual (fibonacci(5),3)

unittest.main()

