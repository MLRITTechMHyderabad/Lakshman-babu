def Calculator(x, y, operator):  #Function 
    try:
        if type(a) not in [int, float] or type(b) not in [int, float]:
            raise TypeError("Error: Invalid Inputs.")

        # Validate the operator
        if operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        elif operator == '*':
            return a*b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Error: Divided by Zero")
            return a/b 
        elif operator == '%':
            if b == 0:
                raise ZeroDivisionError("Error: Divided by zero")
            return a%b
        elif operator == "**":
            return a**b
        else: 
            raise ValueError("Error: Invalid Operator")
    #Handling specific errors
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as v:
        return str(v)
    except TypeError as t:
        return str(t)
    except Exception as E:
        return f"Error: {str(E)}"

try:
    #User input
    a = float(input("Enter the First Number: "))
    b = float(input("Enter the Second Number: "))
    operator = input("Enter the one of this Operators (+, -, *, /, %, **): ")
    result = Calculator(a,b,operator) #Function calling 
    print(f"Result : {result}")
except Exception as E:
    print("Invalid input: ", E)    
        