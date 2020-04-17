# Diffie-Hellman

**NONE of the implementations are intended for production usage**. They have not been extensively validated for it. These files are simply an **educational tool** for looking at **AN implementation** that works to help people understand it.

There is an accompanying video that walks-through the python implementation that I will post a link to once I complete it. Additionally you can find an in-depth explanation below of the protocol and how to use the implementations (again not in production applications).

## Table of contents

- [Usage](#usage)    
- [Glossary](#glossary)        
  - [Variables](#variables)        
  - [Functions](#functions)    
- [Theory](#theory)        
  - [1. Background](#1-background)        
  - [2. Initial Variables and Secret Generation](#2-initial-variables-and-secret-generation)       
  - [3. Public Secret Exchange](#3-public-secret-exchange)       
  - [4. Common Secret Calculation](#4-common-secret-calculation)      


## Usage

Each folder contains a language implementation with details on how to setup a runtime environment and run the corresponding file. The most polished implementation is python since that's my preferred language. When you run the file it will generate a file called ```exchange.txt``` this will effectively be a printout of stdout when the program is running so you can have a plaintext version of what happened.



## Glossary

Throughout the files I use a set of standardized terms to refer to variables and functions to make the implementations understandable:



### Variables

*The letter values are what is used in the technical explanation so I have included both the letter representations (as they are in the proofs) and a more colloquial name for what they represent.*

***Shared Prime | p***: This is a number decided upon by both Alice and Bob (eve knows this also), that is a **prime number** which is used in the various modulus calculations explained later.

***Shared Base | g***: This is an arbitrary number decided upon by both Alice and Bob (eve knows this also), that has no requirements beyond being positive and each member knowing about it.

***Alice Secret | a***: This is a secret that only Alice knows, and is used to calculate her public key (*A*) and the common secret (***s*** and ***a_s***).

***Bob Secret | b***: This is a secret that only Bob knows, and is used to calculate his public key (*B*) and the common secret (***s*** and ***b_s***).

***Alice Public | A***: Alice's public key that is sent to Bob (and it is assumed that eve also knows it) and it used to calculate ***s*** and ***b_s***

***Bob Public | B***: Bob's public key that is sent to Alice (and it is assumed that eve also knows it) and it used to calculate ***s*** and ***a_s***

***Common Secret | s***:  The secret that is calculated by each after the exchange of the public secrets. Naturally this implies that a_s == s == b_s (otherwise something has gone wrong).

***Alice Calculated Common Secret | a_s***: Alice's calculated common secret, if the exchange is done properly then a_s == s == b_s .

***Bob Calculated Common Secret | b_s***: Bob's calculated common secret, if the exchange is done properly then a_s == s == b_s .



### Functions

*Note the names change to suit whatever is the preferred language style so I have opted to just use names with uppercase first letters and spaces in between instead of either snake_case or camelCase.*



***Is Prime***: Takes in a number and returns true if the value is a prime number, get's called by generate prime in order to validate random number is a prime number.

***Generate Prime***: Generates a random prime number within a specified range (needs to be low range in languages with different types of integers to avoid overflow like rust)

***Save***: Takes in all the variables needed to perform Diffie-Hellman and stores a text record of the exchange (exchange.txt), and also returns it so it can be printed later


## Theory

*This explanation is meant to be somewhat simplistic and skip over some of the detail about secrecy and **proofs** why the math works. This description is meant to be a laymen's terms, step-by-step walkthrough of how the Diffie-Hellman protocol works.*



### 1. Background

It's useful to mention that the Diffie-Hellman key exchange is **not** an encryption protocol, in and of itself. It is used for generating a **common secret** which can be used with another form of encryption to encrypt and decrypt traffic. In other words it tells both people what the 'key' to the lock should look like, but not how to lock the information itself. The idea being each person can exchange a public key (that even Eve knows) and end up with the same 'private key' or shared/common secret.



The exchange relies on a somewhat complicated principle of [moduli](https://en.wikipedia.org/wiki/Modulo_operation) (the remainder of a division). If you are interested in proofs of why this works you can take a look at [Fermatt's Little Theorem](https://en.wikipedia.org/wiki/Fermat's_little_theorem) & the Wikipedia page on [Diffie-Hellman]([https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange)) for details. The important things to know that make this protocol work are:

1. Each party (Alice and Bob) needs to generate their own secret (a number)

2. If the same set of procedures is done on two secrets they can generate a third 'common' secret

   ```
   g^(a) mod p = A
   g^(b) mod p = B
   
   B^a mod p = common secret
   A^b mod p = common secret
   ```




### 2. Initial Variables and Secret Generation

There are a number of pieces of public and private variables needed to do Diffiie Hellman. First both Alice and Bob will need Private keys, these will not be known by anyone except the one who generated it. Next they will need a shared prime number and a shared base, both of which are public and Alice, Bob, and Eve know it.



### 3. Public Secret Exchange

....



### 4. Common Secret Calculation

...

