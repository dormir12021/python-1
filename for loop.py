#this is for, "for loop"
math = [int(x) for x in input().split()]
#input().split() is just basically making the number into a list
totalnumber = 0
for e in math:
  totalnumber += e 
print(totalnumber)
