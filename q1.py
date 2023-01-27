def perfect_number(n):
    divisors = []
    # Find all divisors of n
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    # Sum all divisors
    sum_divisors = sum(divisors)
    # Check if the sum of all divisors is equal to the number
    if sum_divisors == n:
        return True
    else:
        return False

# Test
print(perfect_number(6))
