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

# Shared Variables; These are publicly sent between Alice and Bob
shared_prime = 81    # p value
shared_base = 20     # g value

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