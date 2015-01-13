Autor: Francisco Abel Cedrón Santaeufemia
login: francisco.cedron
email: francisco.cedron@udc.es

EjercicioA. Para este ejercicio se ha hecho que la función MAP devuelva un lista con los pares (x,y) donde x es la palabra e y es el número de veces que aparece. Las palabras se ponen todas en minúsculas para que no se cuenten de manera distinta las palabras que estén al principio de una frase. Además se usan las expresiones regulares para que las palabras solo tengan las letras. Además la salida se da ordenada por las palabras (para dar una simulación de ordenación 'merge'). La función reduce lo que hace es leer la lista de pares (x,y) y tiene en cuenta si hay alguna x repetida para dar el resultado correcto. Para que la salida sea lo más legible posible el resultado aparece ordenado por palabras.

EjercicioB. En este ejercicio se pide que se resuelva teniendo almacenada la matriz en un caso por filas y en otro por columnas. Para hacer las funciones MAP y REDUCE lo más flexibles posibles sólo se crea un script para cada una de ellas. La manera de plantear este problema fue pensar que los datos podían estar puestos de manera aleatoria por los ficheros de tal manera que en cada línea tenia una tupla (i,j,a) donde i es índice la fila de i de la matriz, j es índice de la columna de la j y a es el coeficiente en la posición denotada por los índices. La función MAP realiza la multiplicación del cada coeficiente de la matriz con el correspondiente valor del vector (que en este caso el vector sólo tiene la unidad como valores). Si hay alguna fila repetida se suma su valor, para reducir el tamaño de la salida y ahorrarle trabajo a la función REDUCE. Como las salidas de la función MAP no tiene que devolver el resultado de multiplicar una fila o una columna hay que tener en cuenta que puede tener resultados intermedios mezclados. Por eso en la operación de REDUCE hay que mirar que índices están repetidos para sumar su valor.

EjercicioC. En este caso se pide resolver una integración numérica de una o dos variables.
Para la de una variable la función MAP realiza el área del trapecio dada por las coordenadas que aparecen en los archivos y la función usada es la que a un valor x devuelve su cuadrado.
Para el otro caso, en lo que hay que tener en especial atención es que del triángulo se dan las coordenadas. Por eso la fórmula para calcular el área fue la del determinante de cada coordenada (repitiendo al final la primera coordenada que se puso) y multiplicando su resultado por 1/2. La función usada es a la que para dos valores x e y esta devuelve su suma.
Aunque en los archivos de prueba solo aparece un único valor en cada fichero, se supuso que podía haber varios valores en distintas líneas y por eso almacena las sumas parciales de cada intervalo (dado por cada línea) de tal manera que devuelve la suma de las áreas de esos intervalos.
La operación REDUCE se basa en sumar todos los valores de la suma parcial de las áreas.


Descripción del contenido

createSH.c
	Contiene un programa en C que lee el XML que se puede obtener al tratar de acceder al contenido de S3 que contiene los datos para probar las prácticas y genera el archivo 'download.sh' para descargar el contenido que hay en el.

download.sh
	Script que se descarga el contenido de S3 que contiene datos de prueba para la práctica. El comando que se usa para descargar el contenido es 'curl' que en Mac OS X viene por defecto, para otros sistemas se puede descargar de los repositorios.

simulator.sh
	Probar el funcionamiento de las funciones MAP y REDUCE en Amazon EMR puede ser muy lento. Para solventar este problema se creo este script que hace 'casi lo mismo'. Se especifica un directorio que contiene los datos, el script de MAP, el script de REDUCE, un archivo para guardar la salida de realizar la función map y otro archivo para la salida de la función reduce.

EjercicioA
	Contiene los directorios de datos y los script de MAP y REDUCE para el primer  ejercicio (Recuento de palabras)

EjercicioB
	Contiene los directorios de datos y los script de MAP y REDUCE para el segundo ejercicio (Producto matriz vector)

EjercicioC
	Contiene los directorios de datos y los script de MAP y REDUCE para el tercer  ejercicio (Integración numérica)

