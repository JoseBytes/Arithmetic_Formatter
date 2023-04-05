## Proyecto Arithmetic Arranger

Este proyecto consiste en una función llamada `arithmetic_arranger` que recibe una lista de problemas aritméticos en formato de cadena y devuelve las cadenas formateadas para que los problemas estén correctamente alineados.

La función puede recibir una lista de hasta 5 problemas. Cada problema debe estar en formato de cadena y solo puede contener números enteros de un máximo de 4 dígitos y los operadores `+` y `-`. Cada problema debe estar separado por coma en la lista.

La función devolverá una cadena con los problemas formateados de la siguiente manera:
- El primer operando estará alineado a la derecha.
- El segundo operando estará alineado a la derecha debajo del primero.
- El operador estará alineado a la derecha debajo del segundo operando.
- El guión (-) estará alineado a la derecha debajo del operador.
- Si el argumento `show_result` es `True`, se mostrará el resultado de cada problema alineado a la derecha debajo del guión.

Si la función recibe operandos o operadores no válidos o si se supera el número máximo de problemas, devolverá un mensaje de error.

### Ejemplo de uso

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems, show_result=True)

print(arranged_problems)
```

### Este ejemplo producirá la siguiente salida:
```
  32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----    
 7301      3799      88      172    
```

### Si el parámetro show_result se establece en False, la salida se verá así:
```
  32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----    
```
