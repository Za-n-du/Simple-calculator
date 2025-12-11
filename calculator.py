# simple calculator Program
prtint("------Simple Calculator --------")
def add (a, b):
         return a + b 
def subtract (a, b):
        return a - b 
def multiply(a, b):
        if b == 0:
          return "Error: Cannot divide by zero."
          return a / b 
print("Select Operation")
Print("1.add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

Choice = Input("Enter your Choice"(1/2/3/4): ")

num = float(input("Enter first number :  )")

num = float(input("Enter second number:"))

if choice == "1":
             print("Result:", add (num1, num2))
elif choice == "2":
             Print ("result:", subtract(num1, num2))
elif choice == "3":
             print ("result:", multiply(num1, num2))
elif choice == "4":
            print("Result:", divide(num1, num2))
else:
            print("Invalid Choice")
