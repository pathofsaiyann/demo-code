import math

# Fake secret for testing regex/entropy
MATH_API_KEY = "sk-test-98a7sd987f98as7df987as9d8f7" 

def calculate_compound_interest(principal, rate, time):
    amount = principal * (math.pow((1 + rate / 100), time))
    return amount

def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors