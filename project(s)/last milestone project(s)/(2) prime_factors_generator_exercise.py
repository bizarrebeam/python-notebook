# because at the end we'll count how many prime as the factors...
from collections import Counter

def is_prime(x):
    """
    Before generating the prime factors, we ought to check whether the number
    is a prime. What's the point of generating the prime factors if it's prime already...
    """

    if x == 2:
        return True
    
    if x %2 == 0:
        return True
    
    for i in range(3, int((x**0.5) + 1), 2):
        # we already check 2
        # we want to check whether x has divisor
            # the greatest divisor is the square root of its number. e.g 49, 7
                # other than the square root, it's just a repetition of the divisor of it's root and number 
                    # -- less than it's root
        # step 2 because 3 + 2 and so on is odd. all the prime number is odd
        """
        Chat GPT says:
        When i is 3, 49 % 3 is not 0 (remainder is 1), so it's not a divisor
        When i is 5, 49 % 5 is not 0 (remainder is 4), so it's not a divisor.
        When i is 7, 49 % 7 is 0 (remainder is 0), which means 7 is a divisor
          of 49. Thus, x is not prime, and the function returns False
        """

        if x % i == 0:
            return False
    return True

def get_exponent(n):
    """
    We get a list called n contains all the factors.
    This function returns the exponent of multiple elements
    """
    c = Counter(n)
    factors = []

    for i in range(min(n), max(n) + 1):
        if i in n:
            if c[i] != 1:
                factors.append(str(i) + '^' + str(c[i]))
            else:
                factors.append(str(i))



