playing = True


a = int(input("Choose a number:\n"))
b = int(input("Choose another one:\n"))
operation = input(
    "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n" )


while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n" )

    if operation == "+":
        print(f"Result: {a + b}")
        print("------------")
    elif operation == "-":
        print(f"Result: {a - b}")
        print("------------")
    elif operation == "*":
        print(f"Result: {a*b}")
        print("------------")
    elif operation == "/":
        print(f"Result: {a/b}")
        print("------------")
    elif operation == "exit":
        playing = False
        break
    else:
        print("You wrote wrong operation. Please try again.")



