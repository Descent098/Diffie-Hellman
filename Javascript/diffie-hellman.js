
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
        number = Math.floor((Math.random() * maxValue) + minValue);
        prime = isPrime(number)
    }

    return number
}



var sharedPrime = generatePrime(0, 300)
console.log("Prime is: " + sharedPrime);
document.getElementById("sharedPrime").innerText = sharedPrime;

