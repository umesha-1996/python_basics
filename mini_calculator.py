def calculator():
    print("Mini Calculator")

    op = input("Enter operator : ")
    no1 = float(input("Enter first number : "))
    no2 = float(input("Enter second number : "))

    if op == '+':
        result = no1 + no2
    elif op == '-':
        result = no1 - no2
    elif op == '*':
        result = no1 * no2
    elif op == '/':
        if no2 != 0:
            result = no1 / no2
        else:
            return "cannot devide by zero"
    else:
        return "Invalid operator!"
    
    return f"Resul : {result}"

print(calculator())
    
