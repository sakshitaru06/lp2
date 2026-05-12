# Diffie-Hellman Key Exchange

# Public values
p = 23
g = 5

# Private keys from user
a = int(input("Enter Alice Private Key: "))
b = int(input("Enter Bob Private Key: "))

# Public keys
A = (g ** a) % p
B = (g ** b) % p

# Shared secret keys
alice_key = (B ** a) % p
bob_key = (A ** b) % p

print("\nAlice Public Key:", A)
print("Bob Public Key:", B)

print("\nAlice Shared Key:", alice_key)
print("Bob Shared Key:", bob_key)
