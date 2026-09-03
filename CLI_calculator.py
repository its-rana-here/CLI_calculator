def addition(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Can not divide by zero"
    return a / b
def m_division(a,b):
    return a % b
print("------Welcome-------")
print("------CLI Claculater------")

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo Division")
print("6 Exit")

def f_input():
    while True:
        choice = input("Enter your Function: ")

        if choice == "":
            print("⚠️ Please enter a function.")
            continue

        return choice

def f_run(choice):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice in ["1", "+"]:
        print("Output:", addition(a,b))
        check()
    elif choice in ["2", "-"]:
        print("Output:", subtract(a,b))
        check()
    elif choice in ["3", "*"]:
        print("Output:", multiply(a,b))
        check()
    elif choice in ["4", "/"]:
        print("Output:", division(a,b))
        check()
    elif choice in ["5", "%"]:
            print("Output:", m_division(a,b))
            check()
    else:
        print("thanks for using our service")

def check():
        choice = f_input()
        if choice in ["1", "+", "2", "-", "3", "*", "4", "/", "5", "%"]:       
            f_run(choice)
        elif choice in ["5", "Exit", "exit"]:
           print("Thanks for using our service.")
        elif choice == choice.strip():
            print("kuchh bhi type kiya hai. Kuchh to choose karo. ")
            check()

        else:
            print("Wrong Input ⚠️ ")
            check()
            
print("Hey buddy. ")
check()


