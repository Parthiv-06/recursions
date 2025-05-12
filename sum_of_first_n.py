def sum_of_first(n):
    if n==0:
        return 0
    return n+sum_of_first(n-1)
print(sum_of_first(10))