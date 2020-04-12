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
  - [4. Handshake](#4-handshake)      


## Usage

Each folder contains a language implementation with details on how to setup a runtime environment and run the corresponding file. The most polished implementation is python since that's my preferred language. When you run the file it will generate a file called ```exchange.txt``` this will effectively be a printout of stdout when the program is running so you can have a plaintext version of what happened.



## Glossary

Throughout the files I use a set of standardized terms to refer to variables and functions to make the implementations understandable:



### Variables

*The letter values are what is used in the technical explanation so I have included both the letter representations (as they are in the proofs) and a more colloquial name for what they represent.*

***Shared Prime | p***: ...

***Shared Base | g***: ...

***Alice Secret | a***: ...

***Bob Secret | b***: ...

***Alice Public | A***: ...

***Bob Public | B***: ...

***Common Secret | s***: ...



### Functions

*Note the names change to suit whatever is the preferred language style so I have opted to just use names with uppercase first letters and spaces in between instead of either snake_case or camelCase.*



***Is Prime***: ...

***Generate Prime***: ...

***Encrypt***: ...

***Decrypt***: ...

***Save***: ...



***Save***: Takes in either a string or char array based on which language it is, and a file path then serializes the string/char array to the path provided.


## Theory

*This explanation is meant to be somewhat simplistic and skip over some of the detail about secrecy and **proofs** why the math works. This description is meant to be a laymen's terms, step-by-step walkthrough of how the Diffie-Hellman protocol works.*



### 1. Background

It's useful to mention that the Diffie-Hellman key exchange is **not** an encryption protocol, in and of itself. It is used for generating a **common secret** which can be used with another form of encryption to encrypt and decrypt traffic. In other words it tells both people what the 'key' to the lock should look like, but not how to lock the information itself.



The exchange relies on a somewhat complicated principle of [moduli](https://en.wikipedia.org/wiki/Modulo_operation) (the remainder of a division). If you are interested in proofs of why this works you can take a look at [Fermatt's Little Theorem](https://en.wikipedia.org/wiki/Fermat's_little_theorem) & the Wikipedia page on [Diffie-Hellman]([https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange)) for details. The important things to know that make this protocol work are:

1. Each party (alice and bob) needs to generate their own secret (a number)

2. If the same set of procedures is done on two secrets they can generate a third 'common' secret

   ```
   g^(a) mod p = A
   g^(b) mod p = B
   
   B^a mod p = common secret
   A^b mod p = common secret
   ```




### 2. Initial Variables and Secret Generation

...



### 3. Public Secret Exchange

....



### 4. Handshake

...

