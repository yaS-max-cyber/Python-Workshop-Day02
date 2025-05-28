sum = 0 
for i in range (1,11):
    sqr = i*i
    if(sqr%4==0):
        sum += sqr
print("sum of odd numbers from 0 to 10:",sum)
