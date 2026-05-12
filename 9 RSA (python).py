# RSA Algorithm in Python

# Function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Input prime numbers
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

# Calculate n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Find public key e
for e in range(2, phi):
    if gcd(e, phi) == 1:
        break

# Find private key d
for i in range(1, 100):
    if (i * e) % phi == 1:
        d = i
        break

# Message input
msg = int(input("Enter message: "))

# Encryption
c = (msg ** e) % n

# Decryption
m = (c ** d) % n

print("Public Key (e) =", e)
print("Private Key (d) =", d)

print("Encrypted Message =", c)
print("Decrypted Message =", m)
