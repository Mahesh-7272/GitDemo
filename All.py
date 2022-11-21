
"""
#code for prime no
print("Prime numbers between", 10, "and", 20, "are:")

for num in range(10, 20 + 1):
   # all prime numbers are greater than 1
   #if num > 1:
       for i in range(2, num):
           if num % i == 0:
               break
       else:
        print(num)

a=[1,8,6,3,2,6,8,9]
a.sort()
print(a)


a=[1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)



#palindrome
s="Mahesh"
reverse=s[::-1]
print(reverse)
if  s == reverse:
    print("the value is palindrome")
else:
    print("not palindrome")
    """







