# arithmetic_arranger

Este programa toma una lista de problemas aritméticos y los organiza en un formato legible para ser impreso. También puede mostrar el resultado de los cálculos si se especifica.

## Uso

Para usar esta función, llámela con una lista de problemas y una bandera opcional para mostrar el resultado. Por ejemplo:

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems)

print(arranged_problems)

# Output:
#   32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
```
