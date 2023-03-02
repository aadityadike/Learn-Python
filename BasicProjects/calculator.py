def main():
    num1= input("enter number 1: ")
    operation = input("enter the operation do you want to perform : ")
    num2= input("enter number 2: ")
        
    if (operation == "+") :
        add(num1,num2)
    elif (operation == "-") :
        sub(num1,num2)
    elif (operation == "*") :
        mul(num1,num2)
    elif (operation == "/") :
        div(num1,num2)
    elif (operation == "%") :
        mod(num1,num2)
    else:
        print("please enter the valid number ") 
    


    