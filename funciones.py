def greet(name):
    print("Hello", name)
    
#greet("maria")

def add(a,b):
    return a+b 

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Options:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        option = int(input("Select an option: "))
        
        if option == 5:
            print("Goodbye")
            break
        
        if option in [1,2,3,4]:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            
            if option == 1:
                print("Result: ", add(num1, num2))
            elif option == 2:
                print("Result: ", substract(num1, num2))
            elif option == 3:
                print("Result: ", multiply(num1, num2))
            elif option == 4:
                print("Result: ", divide(num1, num2))
        else:
            print("Invalid option")
        