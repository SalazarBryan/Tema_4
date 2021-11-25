# Tema_4
Proyecto 4 de modelos UCR

Lo primero que se busca es crear una función que convierta la imagen que se va a transmitir en una cadena de bits para su respectivo envío, en este caso un arreglo.

Cuando se transforma a una matriz con datos en bits de los RGB, cada dato nos da la intensidad de los respectivos colores a lo largo de la imagen enviada.
La matriz está compuesta por 3 elementos, 2 de pixeles y 1 de los canales.

Luego se pasa a un arreglo de una sola línea y no como una matriz y seguidamente se pasa a código binario en base 2 códificado en 8 bits(estos se trabajan como string pero
al final se pasan a enteros int.

################################

Luego se crea un modulador para pasar los bits en binario a formas de onda y que pueda viajar, ya que la info en bits sufren muchas distorciones si viajan de esta manera en la
transmisión de información.(ondas sinusoidales que pueden variar en frecuencia para diferentes tipos de transmisión)

Se hace una medición del vector y luego se crean variables importantes como el periodo de la portadora y la frecuencia, lo cual es el tiempo en el que viaja, para cada periodo(T)
de la portadora se añade un símbolo, luego de calcular la portadora como tal.

Se hacen las modificaciones necesarias para el archivo con respecto a la modulación 8 PSK, con los operadores lógicos if respectivos y se calcula la potencia de la señal modulada.

La diferencia entre la portadora y la señal de modulada es que el número de muestras por punto para la de muestreo se multiplica por los bits y así usar todos los N bits.
La modulada es la que se tiene que retornar ya que es la señal que sale.

La señal de salida Tx tiene que estar emparejada por cada tiempo de simulación, entonces tienen que ser de la misma forma.

Recordar que los bits no existen en el tiempo, entonces para tratar de simularlos en el tiempo se crea una forma de onda, que tiene que tener el mismo tamaño del tiempo de simulación.


Por último se crea la función demodulador con sus respectivas variables y el bucle for para los productos y el criterio de energía.

Luego solo se muestran los diferentes resultados de las imágenes como la recibida, la transmitida, el tiempo y entre otras funciones con sus respectivos parámetros.









