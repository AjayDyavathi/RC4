# ENCRYPTION / DECRYPTION OF FILES USING RC4 STREAM CIPHER
import sys


def get_stream(l):
    for k in range(l):
        i, j = 0, 0
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        added = (S[i] + S[j]) % 256
        stream = S[added]
        yield stream


def encrypt(file):
    with open(file, 'rb') as readfile:
        with open(f'rc4_encrypted_{file}', 'wb') as writefile:
            read_bytes = readfile.read()
            print(len(read_bytes), 'bytes')
            print('Encrypting...')
            for each_byte, each_stream in zip(read_bytes, get_stream(len(read_bytes))):
                write_ = bytes([each_byte ^ each_stream])
                writefile.write(write_)
    print(f'Encryption done, file saved with name rc4_encrypted_{file}')


def decrypt(file):
    with open(file, 'rb') as readfile:
        with open(file[13:], 'wb') as writefile:
            read_bytes = readfile.read()
            print(len(read_bytes), 'bytes')
            print("Decrypting...")
            for each_byte, each_stream in zip(read_bytes, get_stream(len(read_bytes))):
                write_ = bytes([each_byte ^ each_stream])
                writefile.write(write_)
    print(f'Decryption done, file saved with name {file[13:]}')


mode = input('Choose mode (enc: encryption / dec: decryption): ').lower()
if mode not in ['enc', 'dec']:
    print(f'Wrong choice: {mode}')
    sys.exit()

file = input('Enter file name in current directory: ')
key = input('Enter password: ')   # choose key with length in range(40, 256) 'bits'.

# S_vector initialization
S = list(range(256))
j = 0
for i in range(256):
    j = (i + S[j] + ord(key[i % len(key)])) % 256
    S[i], S[j] = S[j], S[i]

if mode == 'enc':
    encrypt(file)
elif mode == 'dec':
    decrypt(file)
else:
    print('Invalidf')
