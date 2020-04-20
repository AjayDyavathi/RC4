# GENERATION OF RC4 STREAM

key = 'password'   # choose key with length in range(40, 256) 'bits'.

# S_vector initialization
S = list(range(256))
j = 0
for i in range(256):
    j = (i + S[j] + ord(key[i % len(key)])) % 256
    S[i], S[j] = S[j], S[i]

# Stream generation
i, j = 0, 0
while True:
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    added = (S[i] + S[j]) % 256
    stream = S[added]
    print(stream, '{:08b}'.format(stream))  # choose according to requirement
