"""This file contains a simple implementation of the Diffie-Hellman Key exchange.

It is NOT intended for production usage and has not been extensively verified for it.
This file is simply an educational tool for AN implementation that works. """
from math import sqrt          # Takes the square root of a value
from secrets import choice     # Used to make a random number choice from a list
from secrets import token_hex  # Used to produce reliably random hex values

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

    # Steps by 2 from 3 (so all are odd) to the number square rooted + 1 (because possible previous numbers have already been checked)
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

def save(p:int, g:int, a:int, b:int, A:int, B:int, a_s:int, b_s:int, path:str="exchange.txt") -> str:
    """Takes in all the variables needed to perform Diffie-Hellman and stores a text record of the exchange.

    Parameters
    ----------
    p : int
        The shared prime
    g : int
        The shared base
    a : int
        Alice's private secret
    b : int
        Bob's private secret
    A : int
        Alice's public secret
    B : int
        Bob's public secret
    a_s : int
        Alice's calculated common secret
    b_s : int
        Bob's calculated common secret
    path : str, optional
        The path to save the output file to, by default "exchange.txt":str

    Returns
    -------
    str
        The text record of the Diffie-Hellman exchange

    Notes
    -----
    * For better definitions of each of the variables see the readme in the root directory

    """
    exchange = "Begin of exchange\n\n" # The variable that holds the description of the exchange

    # Generate Initial Variables
    exchange += f"First a shared prime (p) & shared base (g) were generated(eve knows these also):\n\tp = {p}\n\tg = {g}\n\n"

    # Secret Generation
    exchange += f"Next Alice and Bob generated their own private secrets (a and b respectively):\n\ta = {a}\n\tb = {b}\n\n"

    # Public secret exchange
    exchange += f"Alice and Bob now compute their public secrets and send them to each other. \nThese are represented as A and B respectively (eve knows these also):\n\tA = g^a mod p = {A}\n\tB = g^b mod p = {B}\n\n"

    # Handshake
    exchange += f"Alice and Bob can now calculate a common secret that can be used to encrypt later transmissions:\n\tAlice's Calculation: \n\t\ts = B^a mod p = {a_s} \n\tBob's Calculation: \n\t\ts = A^b mod p = {b_s}"

    with open(path, "w+") as output_file:
        output_file.write(exchange)

    return exchange

if __name__ == "__main__":
    # ==== Shared Variables ====

    # These are publicly sent between Alice and Bob
    shared_prime = generate_prime_number()  # p value
    shared_base =  int(token_hex(2), 16)    # g value

    # ==== Private secrets ====

    # These are only known by Alice and Bob respectively, but each doesn't know each others secret
    alice_secret = int(token_hex(2), 16)     # a value
    bob_secret = int(token_hex(2), 16)       # b value

    # ==== Public key generation & exchange ====

    # Alice Sends Bob A = g^a mod p (in this case A == alice_public)
    alice_public = (shared_base ** alice_secret) % shared_prime
    # Bob Sends Alice B = g^b mod p (in this case B == bob_public)
    bob_public = (shared_base ** bob_secret) % shared_prime

    # ==== Common Secret Calculation ====

    # Alice Computes Shared Secret: s = B^a mod p
    alice_calculated_secret = (bob_public ** alice_secret) % shared_prime
    # Bob Computes Shared Secret: s = A^b mod p
    bob_calculated_secret = (alice_public ** bob_secret) % shared_prime

    # Create a text record of the excange, save it to a text file and print it to stdout
    exchange = save(shared_prime, shared_base, alice_secret, bob_secret, alice_public, bob_public, alice_calculated_secret, bob_calculated_secret)
    print(exchange)
