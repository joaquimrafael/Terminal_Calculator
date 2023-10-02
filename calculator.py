# Terminal calculator project developed by Joaquim Prieto

#sum function
def sum(x,y):
    return x + y

#subtraction function
def subtraction(x,y):
    return x - y

#multiplication function
def multiplication(x,y):
    return x * y

#division function
def division(x,y):
    return x / y

#power function
def power(x,y):
    return x**y

#rest of division function
def rest(x,y):
    return x % y

#root function
def root(x,y):
    return x ** (1/y)


#main menu loop
while(True):
    #Title
    print("---Calculator---")
    
    #options available
    print()
    print("Please choose a valid operation: ")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("^ for power")
    print("% for rest of division")
    print("! for root")
    print("$ to exit")
    print()
    
    #receiving user operator choice by keyboard
    option = input("Choice: ").strip()
    #comparing to the end option, if true, end the program
    if option == "$":
        print("<Process ended.>")
        break
    
    #reading the operands
    number1 = float(input("First number: ").strip())
    number2 = float(input("Second number: ").strip())

    #conditional structure to choose the correct operation to be done
    if option == '+': 
        result = sum(number1, number2)
        
    elif option == '-':
        result = subtraction(number1,number2)
        
    elif option == '*':
        result = multiplication(number1,number2)
        
    elif option == '/':
        result = division(number1, number2)
        
    elif option == '^':
        result = power(number1,number2)
        
    elif option == '%':
        result = rest(number1,number2)
        
    elif option == '!':
        result = root(number1,number2)
    
    #invalid case
    else:
        print('Invalid operator, type again!')
        print()
        continue
    
    #printing the result
    print()
    print('*'*50)
    print('{} {} {} = {:.2f}'.format(number1, option, number2, result))
    print('*'*50)
    print()