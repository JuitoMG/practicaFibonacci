def fibonacci(num): #defino funcion
    num1 = 0   #asigno valores iniciales
    num2 = 1
    
    for x in range (num):   #creo bucle for para calcular el numero
        num3= num1 + num2
        num1= num2
        num2= num3         #este baile de variables calcula la suces�on
    
    print(num1)             #imprimimos la variable que da el resultado
    return num1


