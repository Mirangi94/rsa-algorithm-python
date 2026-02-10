from math import gcd

p = int(input("Enter 1st Prime Number: "))
q = int(input("Enter 2nd Prime Number: "))

# Computation of modulus and Euler's Totient
n = p * q
phi = (p - 1) * (q - 1)

# Selecting public exponent [e]
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Computation of private exponent [d] (Modular Inverse of [e])
d = pow(e, -1, phi)

print("\nPublic Key  (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Encrypting message
msg = int(input("\nEnter message (number < n): "))
cipher = pow(msg, e, n)
print("Encrypted Message:", cipher)

# Decrypting message
plain = pow(cipher, d, n)
print("Decrypted Message:", plain)
