## arithmetic_arranger

La función `arithmetic_arranger()` toma una lista de problemas aritméticos y devuelve una cadena formateada que los muestra uno encima del otro. Cada problema consta de dos operandos y un operador (+ o -). La función también puede mostrar el resultado de cada problema si se establece el parámetro `show_result` en `True`.

### Parámetros

- `problems` (requerido): Una lista de problemas aritméticos.
- `show_result` (opcional): Un valor booleano que indica si mostrar o no el resultado de cada problema. El valor predeterminado es `False`.

### Ejemplo de uso

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems, show_result=True)

print(arranged_problems)
```

###Este ejemplo producirá la siguiente salida:
```
  32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----    
 7301      3799      88      172    
```

###Si el parámetro show_result se establece en False, la salida se verá así:
```
  32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----    
```
