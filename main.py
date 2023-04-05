from arithmetic_arranger import arithmetic_arranger
from test_module import test

# Ejemplo de uso de la función
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems = arithmetic_arranger(problems, True)
print(arranged_problems)

# Ejecutar pruebas unitarias
test(arithmetic_arranger)
