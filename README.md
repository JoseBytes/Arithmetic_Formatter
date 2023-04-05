[b]Proyecto: Arithmetic Arranger[/b]

[i]Este proyecto fue creado como parte del curso "Científico de datos" de freeCodeCamp.org.[/i]

[b]Descripción[/b]

El proyecto consiste en crear una función que recibe una lista de operaciones aritméticas y devuelve una cadena de texto que muestra estas operaciones dispuestas en una forma organizada. La función debe poder manejar sumas y restas con números de hasta 4 dígitos y opcionalmente, también puede mostrar los resultados de estas operaciones.

[b]Instrucciones de instalación[/b]

No se requiere instalación para este proyecto, simplemente descargue el archivo "arithmetic_arranger.py" y utilícelo en su proyecto.

[b]Instrucciones de uso[/b]

Para utilizar la función "arithmetic_arranger" en su proyecto, primero importe la función en su archivo:

[code]from arithmetic_arranger import arithmetic_arranger[/code]

Luego, llame a la función y pase una lista de operaciones aritméticas como argumento:

[code]arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])[/code]

La función devolverá una cadena de texto que muestra las operaciones dispuestas en una forma organizada.

[b]Ejemplos[/b]

La función puede manejar sumas y restas con números de hasta 4 dígitos. A continuación se muestran algunos ejemplos de cómo se vería la salida de la función:

[code]
arithmetic_arranger(["32 + 698", "3801 - 2"])
# Salida:
#    32
# + 698
# -----
#   730
#
#   3801
# -    2
# -----
#   3799

arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
# Salida:
#     3         45      123
# + 855    - 43    +  49
# -----    ----    -----
#   858        3801      172
#
[/code]

[b]Licencia[/b]

Este proyecto está bajo la Licencia MIT.
