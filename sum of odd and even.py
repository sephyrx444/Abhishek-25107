def sum_even_odd(n):
    even_sum = sum(i for i in range(1, n+1) if i % 2 == 0)
    odd_sum = sum(i for i in range(1, n+1) if i % 2 != 0)
    return even_sum, odd_sum
n = 10
even_sum, odd_sum = sum_even_odd(n)
print("Sum of even numbers : {even_sum}")
print("Sum of odd numbers : {odd_sum}")
