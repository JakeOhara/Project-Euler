#problem 2 

sum=0
a=0 
b=1 

while b <= 4000000:
   if b % 2 == 0: 
      sum +=b
   a,b = b, a+b

print(sum)

