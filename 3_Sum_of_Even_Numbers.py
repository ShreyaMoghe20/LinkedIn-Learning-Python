def sum_of_even(n):
    total = 0
    for i in range(1, n+1):
        if i%2 == 0:
            total = total + i
    return total

n = int(input('Enter number: '))
result = sum_of_even(n)
print(result) 