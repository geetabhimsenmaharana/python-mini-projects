# -------------------------------
# CALCULATOR PROGRAM (DAY 1)
# -------------------------------


# 'def' is used to DEFINE (create) a function
# A function is like a small machine that takes input and gives output
# Here we are creating build_calculator function with 2 parameter number 1 and number 2.
def build_calculator(number1, number2):

    # input() is used to take input from the user
    # It always returns a STRING (text)
    operator = input("Enter an operator (+, -, *, /): ")

    # 'if' is used to check a condition
    # '==' means "compare" (not assign)
    if operator == "+":
        # If operator is '+', we ADD the two numbers
        result = number1 + number2

    # 'elif' means "else if" (check another condition)
    elif operator == "-":
        # Subtract second number from first
        result = number1 - number2

    elif operator == "*":
        # Multiply both numbers
        result = number1 * number2

    elif operator == "/":
        # Before dividing, check if second number is 0
        # Because division by 0 will crash the program
        if number2 == 0:
            # 'return' sends value back and stops function
            return "Error: Cannot divide by zero"

        # If safe, perform division
        result = number1 / number2

    else:
        # If user enters wrong operator
        return "Error: Invalid operator"

    # 'return' sends the final result back to where function was called
    return result


# -------------------------------
# MAIN PROGRAM STARTS HERE
# -------------------------------

# 'try' means: try running this code
# If error happens, go to 'except'
try:
    # input() gives STRING → we convert to number using float()
    # float() allows decimal numbers like 10.5
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Call the function and pass num1 and num2 as arguments
    # The function will process and return a result
    final_result = build_calculator(num1, num2)

    # print() displays output to the user
    print("Result:", final_result)

# This block runs if user enters invalid number (like 'abc')
except ValueError:
    print("Error: Please enter valid numbers only")

# This block catches any unexpected error
except Exception as e:
    print("Something went wrong:", e)
