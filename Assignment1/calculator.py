num1 = int(input("enter your first number "))
num2 = int(input("enter your second number "))
sign = input("enter symbol ")


if sign == '+':
    answer = num1 + num2
    print(answer)
elif sign == '-':
    answer = num1 - num2
    print(answer)
elif sign == '/':
    answer = num1 / num2
    print(answer)
elif sign == '*':
    answer = num1 * num2
    print(answer)
else : 
    sign = input("Enter the correct sign")
