#To find the Year is Leap Year or Not
def Leap_Year_check(Year):
  if ((Year % 100 == 0 & Year % 400 == 0) | (Year % 400 == 0)):
    print("The Given Year is Leap Year")
  else:
    print("The Given Year is not a Leap Year")


Get_Year = int(input("Enter the Year:"))
Leap_Year_check(Get_Year)
