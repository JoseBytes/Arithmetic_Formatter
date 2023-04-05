def arithmetic_arranger(problems, show_result=False):
    # Validar número máximo de problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    # Inicializar variables
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # Iterar por cada problema
    for problem in problems:
        # Separar operando y operación
        operand1, operator, operand2 = problem.split()

        # Validar operadores y operandos
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Validar longitud de operandos
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcular resultado
        if operator == "+":
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)

        # Obtener longitud de operandos y resultado
        length = max(len(operand1), len(operand2)) + 2
        result_length = len(str(result))

        # Agregar espacios para alinear operandos y resultado
        line1 += operand1.rjust(length) + "    "
        line2 += operator + operand2.rjust(length - 1) + "    "
        line3 += "-" * length + "    "
        line4 += str(result).rjust(length) + "    " if show_result else ""

    # Unir líneas
    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()

    return arranged_problems
