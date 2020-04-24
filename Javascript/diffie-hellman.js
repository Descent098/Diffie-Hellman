
function isPrime(number){
    if (number == 2 || number == 3){ // Both 2 and 3 are primes
        return true
    }

    else if (number % 2 == 0 || number < 2){ // No primes exist that are less than 2 or even (also covers negatives)
        return false
    }

    // Steps by 2 from 3 (so all are odd) to the number square rooted + 1 (because possible previous numbers have already been checked)
    var count = 3
    while (count <=  Math.sqrt(number) + 1){
        if (number % count == 0){
            return false
        }
        count += 2
    }

    return true
}

function generatePrime(minValue, maxValue){
    var prime = false
    var number = -1
    while (!prime){
        number = Math.floor((Math.random() * maxValue) + minValue)
        prime = isPrime(number)
    }

    return number
}


// These are publicly sent between Alice and Bob
var sharedPrime = generatePrime(1, 50)                // p value
var sharedBase = Math.floor((Math.random() * 50) + 1) // g value

// These are only known by Alice and Bob respectively, but each doesn't know each others secret
var aliceSecret = Math.floor((Math.random() * 50) + 1)    // a value
var bobSecret = Math.floor((Math.random() * 50) + 1)      // b value

// Alice Sends Bob A = g^a mod p (in this case A == alice_public)
// Bob Sends Alice B = g^b mod p (in this case B == bob_public)
var alicePublic = Math.pow(sharedBase, aliceSecret) % sharedPrime // A
var bobPublic = Math.pow(sharedBase, bobSecret) % sharedPrime     //B

// Alice Computes Shared Secret: s = B^a mod p
// Bob Computes Shared Secret: s = A^b mod p
// BUG: These values differ on non-zero values
var aliceCalculatedSecret = Math.pow(bobPublic, aliceSecret) % sharedPrime
var bobCalculatedSecret = Math.pow(alicePublic, bobSecret) % sharedPrime

// Print Variables to stdout
console.log("Shared Base is: " + sharedBase)
console.log("Shared Prime is: " + sharedPrime)
console.log("Alice's Public Key is: " + alicePublic)
console.log("Bob's Public Key is: " + bobPublic)
console.log("Alice's Calculated Secret is: " + aliceCalculatedSecret)
console.log("Bob's Calculated Secret is: " + bobCalculatedSecret)

// Write variables to HTML elements
document.getElementById("sharedPrime").innerText = sharedPrime
document.getElementById("sharedBase").innerText = sharedBase
document.getElementById("alicePublic").innerText = alicePublic
document.getElementById("bobPublic").innerText = bobPublic

document.getElementById("aliceSecret").innerText = "Alice's Private Secret " + aliceSecret + "\nAlice's Calculated Secret " + aliceCalculatedSecret 
document.getElementById("bobSecret").innerText = "Bob's Private Secret " + bobSecret + "\nBob's Calculated Secret " + bobCalculatedSecret 
