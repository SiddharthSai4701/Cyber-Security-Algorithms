# -*- coding: utf-8 -*-
"""
Filename: 

About the program:

Created on Wed Nov  2 17:57:37 2022

@author: Siddharth Vijay Sai
"""

# Accepting for prime numbers, P,Q,R,S along with the plaintext M
P = int(input("Enter the first prime number: "))
Q = int(input("Enter the second prime number: "))
R = int(input("Enter the third prime number: "))
S = int(input("Enter the fourth prime number: "))
M = int(input("Enter the plaintext value: "))

# Calculating the modulus of encryption, n
n = P*Q*R*S

# Calculating phi_n, the Euler's quotient
phi_n = (P-1)*(Q-1)*(R-1)*(S-1)

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


# The public key e should be a value greater than 1 and less than phi_n. Therefore, I've initialised i to 2.
i = 2

# Running a while loop until a value for i is obtained such that the gcd of phi_n and i is 1
while True:
    
    # x is the gcd of phi_n and i
    x = gcd(phi_n,i)
    
    # if x has a value of 1, assign that value of i to the variable e.
    if x == 1:
        e = i
        break
    i+=1

# Printing the value of e
print("\ne is:",e)

# Next, we calculate the private key, d.
# For this, we choose values of j starting from 0 all the way to infinity until a value for j is obtained such that d is a non decimal number.
# The formula used to calculate d is d = ((phi_n * j) + 1)/e

j = 0

# Running the while loop until  an appropriate value of j is obtained

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

# d is of type float. If it isn't typecast to an integer, it will lead to an erroneous result when it is used later for decryption.
d = int(d)

# Print the value of the private key, d
print("\nd is: ",d)

# Calculate the cipher text, c and print it
c = pow(M,e)%n
print("\nThe encrypted text is:",c)

# Decipher the cipher text and print it
p = (c**d)%n
print("\nThe decrypted text is:",int(p))