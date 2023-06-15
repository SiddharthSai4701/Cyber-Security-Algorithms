# -*- coding: utf-8 -*-
"""
Filename: CircularRSA

About the program:

Created on Wed Nov  2 17:29:29 2022

@author: Siddharth Vijay Sai
"""

# import math as m

n1 = input("Enter a prime number: ") #'31'
M = int(input("Enter the plaintext value: "))

l = []
for i in range(len(n1)):
    l.append(n1[i])


nums = [n1]

for i in range(len(n1)-1):
    l.append(l[0])
    l.pop(0)
    
    new_num = ""
    for i in l:
        new_num +=i
    print(new_num)
    nums.append(new_num)
    
n = 1
phi_n = 1
for i in nums:
    
    n*=int(i)
    phi_n *= int(i)-1 
    
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
    # x = m.gcd(phi_n, i)
    
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
