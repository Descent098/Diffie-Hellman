/*This file (very simplistically) implements the diffie-helman key exchange: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

Roughly speaking this means generating a shared base(g) and prime number(p) that Alice and Bob both know,
then individually each decides a secret number.Once each has their own secrets (a and b respectively in this
file) they then send:
    g^(their private secret[a or b]) mod p
to each other (named A or B in this file). Using each others 'public' secret they can generate a shared secret 
by taking:
    (other persons public secret[A or B])^(their private secret[a or b]) mod p

This means that both sides can publicly send this information to one another and still have safe encryption without
Eve being able to read their messages.
*/
fn main() {

    // Shared Variables
    let shared_prime = 97; // p value
    let shared_base = 4;  // g value

    // Secrets
    let alice_secret = 2; // a value
    let bob_secret = 11;  // b value

    println!("==Publicly Shared Variables(Eve can see)== \nAlice and Bob agreed on shared prime of {} & shared base of {}", shared_prime, shared_base);

    // Alice Generates A = g^a mod p
    let A = i64::pow(shared_base, alice_secret) % shared_prime;
    // Bob Generates B = g^b mod p
    let B = i64::pow(shared_base, bob_secret) % shared_prime;

    println!("Alice sends {} over public channel \nBob sends {} over public channel", A, B );

    // Alice computes a shared secret: B^a mod p
    let alice_calculated_secret = i64::pow(B, alice_secret) % shared_prime;

    // Bob Computes Shared Secret: A^b mod p
    let bob_calculated_secret = i64::pow(A, bob_secret) % shared_prime;

    println!("\n==Privately Calculated Secrets==\nAlice computed the secret {}\nBob computed the secret {}\nThey both match: {}", alice_calculated_secret, bob_calculated_secret, alice_calculated_secret == bob_calculated_secret);
    println!("\n==Eve Knows==\nShared prime {} & Shared Base: {} \nA: {} & B: {}\nBut cannot calculate Alice and Bob's shared Secret:{}", shared_prime, shared_base, A, B, alice_calculated_secret);

}
