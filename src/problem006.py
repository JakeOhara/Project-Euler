#problem 6

sum = 0
sumsq = 0
dif = 0
for x in range(1,101):
   sum = sum + x**2
   
print(sum)

for y in range(1,101):
   sumsq = sumsq + y

sumsq = sumsq**2
print(sumsq)

dif = sumsq - sum
print(dif)
