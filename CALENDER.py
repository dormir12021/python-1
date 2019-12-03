year = int(input("Year:"))
if year < 0:
  print("Invalid, don't use negative numbers.")
else:
  divfour = (year % 4) == 0:
    if (year % 400) == 0:
      if (year % 100) == 0:
        print("{0} is a leap year")
