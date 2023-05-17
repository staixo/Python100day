def calculate(first, operator, operation_dict, second):
    """create an operation based on the operator chosen and two numbers"""
    result= operation_dict[operator]
    result= result(first,second)
    return "Result: "+str(first)+" "+operator+" "+str(second)+" = "+str(result)

def add(first,second):
    """add two numbers"""
    return first + second

def divide(first,second):
    """divide two numbers"""
    if second != 0:
        return first / second
    else:
        return "Cannot divide by zero"

def subtract(first,second):
    """subtract two numbers"""
    return first - second

def multiply(first,second):
    """multiply two numbers"""
    return first * second

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def choose_operator(operation_dict):
    """choose the operator to use in the calculation
    :return: the operator chosen by the user
    """
    for symbol in operation_dict:
        print(symbol)
    operator="0"
    while not operator in operation_dict:
        operator = str(input("Enter the operator: ")) 
    return operator

print(calculate(float(input("Enter the first number: ")), choose_operator(operation_dict), operation_dict, float(input("Enter the second number: "))))
