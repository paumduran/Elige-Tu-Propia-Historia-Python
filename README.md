# Elige-Tu-Propia-Historia-Python
Objetivo 
Realizar una aplicación denominada "CuentoPersonalizado" que visualice cuentos interactivos, permitiendo al lector decidir el rumbo que la historia toma en distintos momentos. 

Destinatarios 
Los destinatarios serán niño y niñas entre 6 y 99 años. 

Descripción 
"CuentoPersonalizado" se basa en los libros de texto “Elige tu propia aventura”, donde el lector, en algunos puntos específicos de la historia, toma decisiones que lo conducen a distintos desenlaces. 
"CuentoPersonalizado" presentará los cuentos interactivos disponibles para leer. Luego de elegir uno de ellos, debe procesar y representar los guiones del mismo. Éstos se encuentran en archivos de texto que respetan un formato específico1 en un directorio denominado "cuentos". 
En la historia habrá diferentes escenas, actores y diálogos. La descripción de los mismos se encuentran en los archivos que contienen los guiones para cada historia posible. 

Escenas 
Una escena es un fragmento de la historia en donde suceden eventos.
Los "guiones", estarán divididos por escenas. La forma en que aparecerá la información de la escena en el archivo del guión, es la siguiente: 
...
[playa, playa.png]
...
Ocupará una línea dentro del archivo y aparecerá entre corchetes. El primer elemento es el nombre de la escena y, el segundo, el nombre del archivo que contiene el fondo que se debe mostrar. 
Lo que corresponda a una escena abarca desde la aparición de la línea [nombreEscena, archivoFondoEscena], hasta la definición de otra escena o hasta el final del archivo.
El orden de lo que suceda en la escena estará dado por el orden de aparición en el guión de los elementos correspondientes de la misma.
La primer escena será siempre la inicial. 

Actores y diálogos 
Un actor es un personaje con un nombre y sus diálogos en distintos momentos de la historia. Los actores deberán decir su diálogo según el orden de aparición en el guión. Los diálogos se definirán como una secuencia líneas, donde cada línea respetará el siguiente formato: nombre del actor, "dos puntos" (separador) y diálogo (sin saltos de línea).
Ejemplo: 
...
Ac kbar: Es una trampa!
...
El actor de nombre Ackbar dirá “Es una trampa!” en el momento dado por el orden de aparición en la escena. 
Las imágenes de los actores se encuentran en un directorio con el nombre del cuento y el archivo correspondiente será el nombre del actor. 
La posición inicial del actor será una al azar y será otorgada la primera vez que aparezca el actor en la historia. 

Acciones 
Los actores podrán realizar acciones. La información de la acción del actor aparecerá en una línea del guión de la siguiente forma:(nombre del actor, nombre de la acción, parámetros necesarios para la acción). Por ejemplo, para que el actor Luis camine hasta la posición x=100, y=150:
...
(Luis, caminar, 100, 150)
...
Las acciones que podrán realizar los actores son:
  ● “posicionar”, parámetros: x, y. El actor aparece (se posiciona, sin animación) en la posición x, y. 
  ● “caminar”, parámetros: x, y. El actor se mueve a paso lento hasta la posición x, y. 
  ● “correr”, parámetros: x, y. El actor se mueve a paso rápido hasta la posición x, y. 
  ● “saltar”, parámetros: x, y. El actor se mueve saltando hasta la posición x, y. 
  ● “volverse_loco”, sin parámetros. El actor gira sobre su eje 3 veces. 
  ● “reir”, sin parámetros. El actor emite el sonido de risa y sobre su imagen aparece un emoticón de risa. 
  ● “seguir_a”, parámetros: actor2. El actor se mueve hasta la posición del actor2. 
  ● “llorar”, sin parámetros. El actor emite el sonido de un llanto y sobre su imagen aparece un emoticón de tristeza/llanto. 
  ● “hablar_infinitivo”, sin parámetros. Todos los siguientes diálogos del actor serán reemplazados por sólo los verbos en infinitivo. 
  ● “hablar_normal”, sin parámetros. Si el actor hablaba en infinitivo, sus siguientes diálogos volverán a la normalidad. 
  ● “sonar”, parámetro: nombre de archivo de sonido. Deberá sonar el sonido o música indicado por el nombre de archivo. 
Se deberán proponer 3 nuevas acciones para los actores documentando su propósito y forma de uso. 

Decisiones 
Son preguntas que se le harán al lector al finalizar una escena y que, en base a su respuesta se determinará el curso de la historia. Cada respuesta tendrá una escena asociada a la cual la historia saltará si elige esa opción. Las decisiones se definirán ​entre llaves​: primero estará la pregunta, luego ​dos puntos (separador), y las posibles opciones separadas por ​punto y coma​. Las opciones se escribirán como: texto de la opción, igual (signo separador) y nombre de la escena. 
Por ejemplo, “Carlos se va de viaje. A dónde debería ir?” París o Roma:
...
{Carlos se va de viaje. A dónde debería ir?:París=EscenaInicioRoma;Roma:EscenaInicioParis}
...
Si no existe una decisión al finalizar la escena, la historia finaliza. 

Calificación de la historia 
Al finalizar la historia, se le pedirá al jugador que califique la historia con 0, 1, 2, 3, 4 o 5 estrellas, guardando el puntaje acumulado de la historia.
Al iniciar "CuentoPersonalizado" se mostrarán las historias disponibles con las estrellas otorgadas por quienes leyeron ya la historia. 

Configuración 
Se deberán poder configurar los siguientes valores: 
    ● Sonido: Activar o desactivar 
    ● Tiempo de duración de los diálogos. 
Esta información deberá guardarse en un archivo y cargarse al iniciar la aplicación. \
