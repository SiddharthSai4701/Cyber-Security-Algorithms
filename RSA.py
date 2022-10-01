# -*- coding: utf-8 -*-
"""
RSA.py

Created on Mon Sep 26 22:20:27 2022

This program implements the Rivest Samir Adleman (RSA) Algorithm.

@author: Siddharth Vijay Sai
"""
# Accepting the two prime numbers, P and Q along with the plaintext M
P = int(input("Enter the first prime number: "))
Q = int(input("Enter the second prime number: "))
M = int(input("Enter the plaintext value: "))

# Calculating the modulus of encryption, n
n = P*Q

# Calculating phi_n, the Euler's quotient
phi_n = (P-1)*(Q-1)

# Function to calculate gcd
def gcd(a,b):
 	
 	if (a == 0):
         
 		 return b
 	if (b == 0):
 		 return a

 	if (a == b):
 		 return a

 	if (a > b):
 		 return gcd(a-b, b)
 	return gcd(a, b-a)


# e should be a value greater than 1 and less than phi_n. Therefore, I've initialised i to 2.
i = 2

# Running a while loop repeatedly until we get a value for i such that the gcd of phi_n and i is 1
while True:
    
    # x is the gcd of phi_n and i
    x = gcd(phi_n,i)
    
    # if x has a value of 1, assign that value of i to the variable e. e is the public key.
    if x == 1:
        e = i
        break
    i+=1
    
# Printing the value of e
print("\ne is:",e)

# Next, we calculate the private key, d.
# For this, we choose values of j starting from 0 all the way to infinity until we find a value for j that causes d to be a non decimal number.
# The formula used to calculate d is 

j = 0

# Running the while loop until we get an appropriate value of j

while True:
    
    # num is the numerator 
    num = ((phi_n*j)+1)
    d = num/e
    
    # To check whether the value of j is appropriate, if the modulus of num and e is 0, it means d is a whole number, hence we break out of the loop
    if num%e==0:
        break
    
    # If the value of j isn't appropriate, incrememnt j and continue
    else:
        j+=1
        continue

# Print the value of the private key, d
print("\nd is: ",int(d))

# Calculate the cipher text, c and print it
c = pow(M,e)%n
print("\nThe encrypted text is:",c)

# Decipher the cipher text and print it
p = (c**int(d))%n
print("\nThe decrypted text is:",int(p))
