import math

# Fake secret for testing regex/entropy
MATH_API_KEY = "sk-test-98a7sd987f98as7df987as9d8f7" 

def calculate_compound_interest(principal, rate, time):
    """
    Calculate the future amount using compound interest.
    
    Args:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate as a percentage.
    time (float): The number of time periods (e.g., years) the interest is applied.
    
    Returns:
    float: The total amount after applying compound interest.
    """
    amount = principal * (math.pow((1 + rate / 100), time))
    return amount

def get_prime_factors(n):
    """
    Return the prime factors of a positive integer as a list in non‑decreasing order.
    
    Args:
    n (int): The integer to factor. Must be greater than 1.
    
    Returns:
    list[int]: A list containing the prime factors of *n*, repeated according to their multiplicity. If *n* is prime, the list contains only *n*.
    """
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