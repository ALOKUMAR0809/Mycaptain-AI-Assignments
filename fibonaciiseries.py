# Fibonacci sequence up to n terms
n = int(input("Enter the number of terms: "))
# declaring the first two terms
a=0
b=0
# check if the number of terms is valid or not
if n <= 0:
   print("The number of terms is invalid. Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence up to", n, "term:")
   print(a)
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(a)
       c = a + b
       # updating the values
       a = b
       b = c
