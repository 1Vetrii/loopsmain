import sys
infile = "systm/dgjkhe82y/tmp/input3.txt"
sys.stdin = open (infile)
#----------------------------------

option = int(input())

if option == 1:
  num1 = int(input())
  num2 = int(input())
  if num1 < num2:
    print(f"The smallest number was {num1}")
  else:
    print(f"The smallest number was {num2}")

if option == 2:
  num1 = int(input())
  num2 = int(input())
  num3 = int(input())
  if num1 < num2 and num1 < num3:
    print(f"The smallest number was {num1}")
  elif num2 < num1 and num2 < num3:
    print(f"The smallest number was {num2}")
  elif num3 < num2 and num3 < num1:
    print(f"The smallest number was {num3}")

if option==3:
  num1 = int(input())
  num2 = int(input())
  num3 = int(input())
  num4 = int(input())
  if num1 < num2 and num1 < num3 and num1 < num4:
    print(f"The smallest number was {num1}")
  elif num2 < num1 and num2 < num3 and num2 < num4:
    print(f"The smallest number was {num2}")
  elif num3 < num2 and num3 < num1 and num3 < num4:
    print(f"The smallest number was {num3}")
  elif num4 < num1 and num4 < num2 and num4 < num3:
    print(f"The smallest number was {num4}")