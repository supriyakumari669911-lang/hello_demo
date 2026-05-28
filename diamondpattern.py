n= int(input("enter the number of rows:"))
for i in range (1, n+1, 2):
	space= (n//2-i//2)
	print("space",end="")
	for j in range (i):
		print("*",end="")
      print()
      for i in range(n-2,0,-2):
	space= (n//2-i//2)
	print("space",end="")
	for j in range(i):
		print("*",end="")
		
