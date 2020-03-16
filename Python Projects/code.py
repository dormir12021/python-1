Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #this is for, "for loop"
math = [int(x) for x in input().split()]
#input().split() is just basically making the number into a list
totalnumber = 0
for e in math:
  totalnumber += e 
print(totalnumber)
