#To find factorial of a number
def factorial_res(num):
  if (num == 0 | num == 1):
    return 1
  else:
    return num * factorial_res(num - 1)


number = int(input("Enter the number:"))
result = factorial_res(number)
print("The Factorial value of the number is :", result)
