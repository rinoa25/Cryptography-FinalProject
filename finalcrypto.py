# Rinoa Malapaya 100743955
# Noshin Rahman 100745332
# Aranya Sutharsan 100748986

# Reference: https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py
# Reference: https://careerkarma.com/blog/python-zip/
# Reference: https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/symmetric-encryption-techniques

alphabet = "bBaAdDcCfFeEhHgGjJiIlLkKnNmMpPoOrRqQtTsSvVuUxXwWzZyY1234567890~!@#$%^&*()_+{}|:<>?-=[]\;,./. "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1
    return decrypted


def main():
    # Opens plaintext file and makes sure there's no whitespaces (\n)
    with open('plaintext.txt', 'r') as file:
        # Message variable contains content of plaintext file
        message = file.read().replace('\n', '')

    # print("Original message: " + message)

    # sonnirara is the key
    key = "sonnirara"
    translated = ''
    i = len(message) - 1

    # First encryption: Making plaintext file content backwards (example: airplane = enalpria)
    while i >= 0:
        # Translated variable contains plaintext as backwards
        translated = translated + message[i]
        i = i - 1

    # Second encryption: Encrypt the backwards plaintext with a variation of the Vigenere Cipher using the secret key
    encrypted_message = encrypt(translated, key)

    # print("Encrypted message: " + encrypted_message)

    # Decrypt the encrypted message using the secret key
    decrypted_message = decrypt(encrypted_message, key)

    # Writes the ciphertext into a text file
    with open('ciphertext.txt', 'w') as f:
        f.writelines(encrypted_message)

    not_backwards = ''
    i = len(decrypted_message) - 1

    # Reverses the backwards on the decrypted message
    while i >= 0:
        # not_backwards variable contains original plaintext (fully decrypted message)
        not_backwards = not_backwards + decrypted_message[i]
        i = i - 1

    # print("Decrypted message: " + not_backwards)


main()
