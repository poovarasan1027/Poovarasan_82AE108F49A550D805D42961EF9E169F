#write a program that determines whether a year entered by the user is a leap year or not using if-elif-else statements.
def CheckLeap(Year):
  if((Year % 400==0) or
   (Year % 100 !=0) and
   (Year % 4 ==0)):
    print("Given year is a leap year");
  else:
   print("Given year i#s not a leap year");
Year = int(input("Enter the number:"))
CheckLeap(Year)