# Practica Fibonacci


**10.2. Enunciado**

**Contexto práctico**

Julián cuando necesita comprobar parte de un código en Python usa la librería incluida por defecto en las distribuciones de Python llamada unittest.

Tiene un pequeño programa llamado fibo.py que escribe la serie de Fibonacci hasta un número dado y devuelve el valor de esa misma posición.

Decide hacer un test del software de tipo aceptación. Es decir, quiere verificar que una parte del código se comporta de forma esperada. Para ello crea un script que importará la librería unittest y comprobará si el quinto número de la serie Fibonacci, el número 3, es correcto (la serie Fibonacci es 0,1,1,2,3,5,8,13…).

Para ello importa la librería de test de software unittest y define una clase donde incluiría la función para comprobar esta parte especifica del código. Va a comprobar que el quinto número de la serie sea igual a 3, lo hace mediante la sentencia self.assertEqual(result, 3).

**¿Qué se pide?**

Antes de nada reflejaremos la sucesión de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34… Tienes mas información sobre esta interesante sucesión y su origen [aquí](https://es.wikipedia.org/wiki/Sucesión_de_Fibonacci)

1: Crea un script que genere la secuencia de Fibonacci

Puedes usar cualquier lenguaje con el que estés familiarizado, pero te recomiendo por facilidad y por el gran acceso a librerías de evaluación de software el lenguaje Python. Si aún no has programado en Python, su inmersión te será sencilla y amigable.

Llamaremos a este script fibo.py (en el caso en que estemos programando en python)

Deberías de crear un programa con su estructura completa. Dentro de este programa crearemos una funciona llamada fibonacci.

2: Creación del programa principal

2.1. Crearemos un programa principal donde definiremos una clase llamada Test, donde probaremos nuestro software.

2.2. Importaremos la librería de testeo de software, en este caso unittest.

2.3. Crearemos nuestra clase (del tipo unittest.TestCase)

2.4. Dentro de esta clase definiremos una función (podemos llamarla como consideremos, pero es recomendable un nombre ilustrativo)

Dentro de la función reflejaremos el tipo de testeo que vamos a realizar. En este caso nuestro objetivo es verificar si la posición X de la sucesión de Fibonacci coincide con el resultado esperado, es decir, si coincide con la posición X que devuelve nuestro programa. Para ello, comprobamos que el quinto número de la sucesión, que es 3, coincide con el quinto número que devuelve nuestra secuencia. Para hacer esta comprobación usaremos el tipo de comprobación assertequal que comprueba si dos valores son iguales

Mediante esta función comprobaremos si la posición quinta de nuestra función coincide con el valor esperado (el valor esperado es la quinta posición de la sucesión que es 3)

3: Verificación de software y pregunta final

Ejecutaremos el programa final y verificaremos si realmente nuestro programa que calcula la sucesión de Fibonacci (fibo.py) se comporta como esperamos. Si el programa que comprueba el código detecta un error, nos reflejará que dato está esperando y que ha recibido. ¿Qué tipo de prueba hemos realizado?

**Entrega**

Debéis realizar la entrega a través de un repositorio creado para tal fin, en una cuenta personal de Github. Podéis emplear tanto una cuenta que ya tengáis y a la que estáis acostumbrados a acceder, como una que creéis a través de la cuenta que os proporciona el centro. La entrega y, en este caso el repositorio, debe contener:

- Una carpeta con todo el código. Debidamente comentado, sangrado y tabulado.
- Un documento en formato PDF que explique las partes que creáis convenientes y que se os demandan explícitamente el los distintos apartados. Debe contener portada, un índice con los distintos puntos, el contenido correspondiente a la resolución de la práctica y un apartado de bibliografía, si has empleado alguna.

Así, para todos los apartados que expliquéis, es una buena práctica y necesario entregar las capturas de pantalla de los principales pasos realizados, explicando el proceso seguido en cada uno de ellos, así como los resultados de cada una de las ejecuciones o los códigos que se han ido desarrollando y que queréis explicar. El objetivo es que pueda observar que has resuelto la tarea sin estar en tu propio ordenador y entender la explicación proporcionada. Esto os ayudará en el examen de evaluación a repasar lo que habíais realizado unas semanas atrás.

En las capturas de pantalla realizadas se debe poder ver claramente que la ejecución la habéis hecho desde vuestro usuario o vuestro equipo. Una forma es tener como fondo de pantalla la plataforma con tu usuario mostrando claramente la foto de tu perfil. En caso de encontraros en el terminal de ejecución o similares, es importante que se observe que la ejecución la habéis hecho desde un usuario que os corresponda. Aquellos apartados/subapartados que no cumplan esta condición no serán corregidos.

Para la entrega, debéis realizar un último *commit* de entrega de actividad con el siguiente mensaje : “Entrega_UD1_Nombre_Apellidos”. Es importante que el *commit* esté dentro del plazo marcado; cualquier *commit* posterior (y no autorizado), hará que la práctica no sea corregida.

Como recomendación, sería una buena práctica que uséis el repositorio para ir mostrando los avances que realizáis. Tampoco os pido que realicéis *commits* cada vez que modifiquéis algo menor en el programa, pero si si empleáis varios días para la resolución de la práctica, un *commit* por día o por cada cambio significativo (que quede debidamente documentado y con el mensaje correspondiente), se tendrá en cuenta de forma positiva. Es decir, que pueda ver el histórico del proceso de desarrollo es uno de los objetivos de la UD, además de que os ayudará para las siguientes UDs a tener terreno ganado con el manejo de un sistema de control de versiones.
