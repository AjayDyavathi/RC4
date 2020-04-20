# ENCRYPTION OF STRINGS USING RC4 STREAM CIPHER

message = 'secret_message'
key = 'password'   # choose key with length in range(40, 256) 'bits'.

# S_vector initialization
S = list(range(256))
j = 0
for i in range(256):
    j = (i + S[j] + ord(key[i % len(key)])) % 256
    S[i], S[j] = S[j], S[i]

# Stream generation
i, j = 0, 0
stream_bytes = []
for q in range(len(message)):
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    added = (S[i] + S[j]) % 256
    stream = S[added]
    stream_bytes.append(stream)

# Encryption
num_message = [ord(char) for char in message]
cipher = ''.join(['{:08b}'.format(i ^ j) for i, j in zip(num_message, stream_bytes)])
print('Ciphertext:', cipher)

# Decryption
num_cipher = [int(cipher[i:i + 8], 2) for i in range(0, len(cipher), 8)]
plain = ''.join(chr(i ^ j) for i, j in zip(num_cipher, stream_bytes))
print('Plaintext:', plain)
