print("-"*60)
print('             Welcome to Calculator application')
print("-"*60)
def add(a,b):
        print(f"The sum of {a} and {b} is",a+b)
def sub(a,b):
        print(f"The difference of {a} and {b} is",a-b)
def multi(a,b):
        print(f"The product of {a} and {b} is",a*b)
def div(a,b):
        print(f"The division of {a} and {b} is",a/b)
def squrt(a,b):
        print(f"The squreroot of {a} and {b} is",a**b)
def modul(a,b):
        print(f"The modulus of {a} and {b} is",a%b)
while True:
     print("What you want to perform")
     print("Addition:1")
     print("Subtraction:2")
     print("Multiplication:3")
     print("Division:4")
     print("Exponent:5")
     print("Modulus:6")
    
    
     

     ch=int(input("Enter your choice: "))
     if ch in (1,2,3,4,5,6):
        a=int(input("Enter a first number: "))
        b=int(input("Enter a Second number: "))
     else: 
        print("Invalid choice")
     if ch==1:
        add(a,b)
    
     elif ch==2:
        sub(a,b)
    
     elif ch==3:
        multi(a,b)
    
     elif ch==4:
        if b>0:
            div(a,b)
        else:
            print("Can't divide by 0")
     elif ch==5:
        squrt(a,b)

     elif ch==6:
        modul(a,b)  
     else:
        print("Choose above options only.")
     p=input("Do you want to continue(y/n): ")
     if p=="n":
        print("-"*60)
        print("            Thank You,Come again")
        print("-"*60)
        break