#a=rows
#b=cols
a=6
b=11
for rows in range(1,a+1):
  for cols in range(1,b+1):
    if cols<=rows or cols>b-rows:
     print("*",end=" ")
    else:
      print(" ",end=" ")
  print()