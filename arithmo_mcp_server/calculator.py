# extract logic here for reuse
def perform_operation(operation: str, a: float, b: float) -> str:
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero is not allowed."
        result = a / b
    else:
        return "Error: Unsupported operation. Use 'add', 'subtract', 'multiply', or 'divide'."

    return format_result(operation, a, b, result)


def format_result(operation: str, a: float, b: float, result: float) -> str:
    return f"""
Operation: {operation.title()}
Inputs: {a} and {b}
Result: {result}
"""
