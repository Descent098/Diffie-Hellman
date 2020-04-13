/// This file contains a simple implementation of the one-time pad.
/// It is NOT intended for production usage and has not been extensively verified for it.
/// This file is simply an educational tool for AN implementation that works.

extern crate rand;           // Used to generate random numbers

use std::fs::File;           // Used to open files
use std::io::Write;          // Uses to write text to files
use std::path::Path;         // Used to write files to paths
use rand::{thread_rng, Rng}; // Random number generation system

/// The primary entrypoint into the demo
fn main() {
    // Initialize random number generator
    let mut rng = thread_rng();

    // ==== Shared Variables ====

    // These are publicly sent between Alice and Bob
    let shared_prime:u16 = generate_prime_number(0, 100); // p value
    let shared_base:u16 = rng.gen_range(1, 11);           // g value

    // ==== Private secrets ====

    // These are only known by Alice and Bob respectively, but each doesn't know each others secret
    let alice_secret:u16 = rng.gen_range(1, 11); // a value
    let bob_secret:u16 = rng.gen_range(1, 11);   // b value
    println!("g: {}\na: {} \nb: {}", shared_base, alice_secret, bob_secret);

    // ==== Public key generation & exchange ====

    // Alice Generates A = g^a mod p
    let alice_public = u64::pow(shared_base as u64, alice_secret as u32) % (shared_prime as u64);
    // Bob Generates B = g^b mod p
    let bob_public = u64::pow(shared_base as u64, bob_secret as u32) % (shared_prime as u64);

    // ==== Common Secret Calculation ====

    // Alice computes a shared secret: B^a mod p
    let alice_calculated_secret = u64::pow(bob_public as u64, alice_secret as u32) % (shared_prime as u64);
    // Bob Computes Shared Secret: A^b mod p
    let bob_calculated_secret = u64::pow(alice_public as u64, bob_secret as u32) % (shared_prime as u64);

    // Create a text record of the excange, save it to a text file and print it to stdout
    let path = Path::new("exchange.txt");
    println!("{}", save(shared_prime, shared_base, alice_secret, bob_secret, alice_public, bob_public, alice_calculated_secret, bob_calculated_secret, path));
}


/// Checks if the provided value is a prime number
///
/// Parameters
/// ----------
/// number : u64
///     The value to validate is a prime number
///
/// Returns
/// -------
/// bool
///     true if value is a prime number
fn is_prime(number:u16) -> bool{

    if (number == 2) || (number == 3){ //Both 2 and 3 are primes
        return true;
    }
    else if ((number % 2) == 0) || (number < 2){ // No primes exist that are less than 2 or even (also covers negatives)
        return false;
    }

    let mut current_number:u16 = 3;
    loop{
        if current_number < (((number as f32).sqrt() as u16) + 1){
            break;
        }
        if (number % current_number) == 0{
            return false;
        }
        current_number += 2;
    }

    return true;
}

/// Generates a random prime number within the range min_value to max_value
///
/// Parameters
/// ----------
/// min_value : int, optional
///     The smallest possible prime number you want, by default 0
/// max_value : int, optional
///     The largest possible prime number you want, by default 300
///
/// Returns
/// -------
/// int
///     A randomly selected prime number in the range min_value to max_value
fn generate_prime_number(min_value:u16, max_value:u16)-> u16{
    // Initialize random number generator
    let mut rng = thread_rng();
    let mut number:u16;

    // Grab an initial number between min_value and max_value (max 2 byte number)
    number = rng.gen_range(min_value, max_value);

    loop{
        if is_prime(number){
            return number;
        }
        else{
            number = rng.gen_range(min_value, max_value);
        }
    }
}

/// Takes in all the variables needed to perform Diffie-Hellman and stores a text record of the exchange.
/// 
/// Parameters
/// ----------
/// p : u16
///     The shared prime
/// g : u16
///     The shared base
/// a : u16
///     Alice's private secret
/// b : u16
///     Bob's private secret
/// A : u64
///     Alice's public secret
/// B : u64
///     Bob's public secret
/// a_s : u64
///     Alice's calculated common secret
/// b_s : u64
///     Bob's calculated common secret
/// path : &Path
///     The path to save the output file to, by default "exchange.txt":str
/// 
/// Returns
/// -------
/// String
///     The text record of the Diffie-Hellman exchange
///
/// Notes
/// -----
/// * For better definitions of each of the variables see the readme in the root directory
///
pub fn save(p:u16, g:u16, a:u16, b:u16, A:u64, B:u64, a_s:u64, b_s:u64, path: &Path)-> String{
    let exchange = String::from(format!("First a shared prime (p) & shared base (g) were generated(eve knows these also):\n\tp = {}\n\tg = {}
    
Next Alice and Bob generated their own private secrets (a and b respectively):\n\ta = {}\n\tb = {}
    
Alice and Bob now compute their public secrets and send them to each other. \nThese are represented as A and B respectively (eve knows these also):\n\tA = g^a mod p = {}\n\tB = g^b mod p = {}
    
Alice and Bob can now calculate a common secret that can be used to encrypt later transmissions:\n\tAlice's Calculation: \n\t\ts = B^a mod p = {} \n\tBob's Calculation: \n\t\ts = A^b mod p = {}", p, g, a, b, A, B, a_s, b_s));

    let mut file = File::create(path).expect("Error when creating file");

    file.write_all(exchange.as_bytes()).expect("Failed to write file");

    return exchange;
}
