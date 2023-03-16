def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"