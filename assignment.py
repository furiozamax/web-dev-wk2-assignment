number1=int(input("Enter the first number:"))
print(number1)
number2=int(input("Enter the second number:"))
print("choose an operation:+,-,*./")
operation=(input("Enter your choice:"))
if operation =="+":
  print("Result:",number1+number2)
elif operation =="-":
  print("Result:",number1-number2)
elif operation =="*":
  print("Result:",number1*number2)
elif operation =="/":
    if number2 !=0:
     print("Result:",number1/number2)
    else:
      print("Error:,Number can not be divided by zero")
else:
  print("Invalid operation")