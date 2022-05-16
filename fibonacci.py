# Write a Python program to get the Fibonacci series between 0 to 50

n1, n2 = 0, 1

   
# generate fibonacci sequence

print("Fibonacci sequence:")
while n1 < 50:
  print(n1)
  nth = n1 + n2
       # update values
  n1 = n2
  n2 = nth

