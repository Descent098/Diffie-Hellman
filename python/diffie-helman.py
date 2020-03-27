"""This file (very simplistically) implements the diffie-helman key exchange: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

Roughly speaking this means generating a shared base(g) and prime number(p) that Alice and Bob both know,
then individually each decides a secret number.Once each has their own secrets (a and b respectively in this
file) they then send:
    g^(their private secret[a or b]) mod p
to each other (named A or B in this file). Using each others 'public' secret they can generate a shared secret 
by taking:
    (other persons public secret[A or B])^(their private secret[a or b]) mod p

This means that both sides can publicly send this information to one another and still have safe encryption without
Eve being able to read their messages.
"""
from math import sqrt      # Takes the square root of a value
from secrets import choice # Used to make a random number choice from a list

def is_prime(number:int) -> bool:
    """Checks if the provided value is a prime number
    
    Parameters
    ----------
    number : int
        The value to validate is a prime number

    Returns
    -------
    bool
        True if value is a prime number
    """
    if number == 2 or number == 3: # Both 2 and 3 are primes
        return True

    elif number % 2 == 0 or number < 2: # No primes exist that are less than 2 or even (also covers negatives)
        return False

    # Steps by 2 from 3 (so all are odd) to the number square rooted + 1 (because possibleprevious numbers have already been checked)
    for current_number in range(3 , int(sqrt(number)) + 1, 2):
        if number % current_number == 0:
            return False
    return True

def generate_prime_number(min_value=0, max_value=300):
    """Generates a random prime number within the range min_value to max_value
    
    Parameters
    ----------
    min_value : int, optional
        The smallest possible prime number you want, by default 0
    max_value : int, optional
        The largest possible prime number you want, by default 300
    
    Returns
    -------
    int
        A randomly selected prime number in the range min_value to max_value
    """
    # Create a list of prime values within the range
    primes = [number for number in range(min_value,max_value) if is_prime(number)]
    return choice(primes)

# Shared Variables; These are publicly sent between Alice and Bob
shared_prime = generate_prime_number()  # p value
shared_base = 20                        # g value

# Private secrets; These are only known by Alice and Bob respectively, but each doesn't know each others secret
alice_secret = 6     # a value
bob_secret = 15      # b value

 
# Alice Sends Bob A = g^a mod p
A = (shared_base ** alice_secret) % shared_prime
# Bob Sends Alice B = g^b mod p
B = (shared_base ** bob_secret) % shared_prime

print( f"""
\n==Public Stuff(Eve can see)==
Alice and Bob agreed on shared prime of {shared_prime} & shared base of {shared_base}
Alice Sends {A} to Bob over public channel (A)
Bob Sends {B} to Alice over public channel (B)""" )
 

# Alice Computes Shared Secret: B^a mod p
alice_calculated_secret = (B ** alice_secret) % shared_prime
# Bob Computes Shared Secret: A^b mod p
bob_calculated_secret = (A**bob_secret) % shared_prime

print( f"""
\n==Individually calculated==
Alice Calculated Secret: {alice_calculated_secret}
Bob Calculated Secret: {bob_calculated_secret}
Both calculated the right value: {alice_calculated_secret == bob_calculated_secret}""")

# What eve knows
print(f"""
\n==Eve knows==
Shared Prime: {shared_prime} & Shared Base: {shared_base}
A:{A} & B:{B}
But cannot calculate Alice and Bob's shared Secret:{alice_calculated_secret}""")
