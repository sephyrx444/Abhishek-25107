def increment (num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit+1
        num//=10
    return sum
number=123
result=increment(number)
print(result)
