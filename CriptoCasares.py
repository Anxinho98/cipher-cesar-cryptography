# Open the text file and read its content
doc = open('06_Casares.txt', encoding='utf-8')
casares = doc.readlines()       # Read lines into a list
loxica = ''.join(casares)       # Join lines into a single string
doc.close()

# Caesar encryption mod 256
def C_enc(clave, texto):
    k = ord(clave)                       # Convert key character to ASCII value
    m_256 = [ord(c) for c in texto]     # Convert each character in text to ASCII
    c_256 = [(a + k) % 256 for a in m_256]  # Shift using Caesar cipher mod 256
    cars = [chr(n) for n in c_256]      # Convert shifted values back to characters
    return ''.join(cars)

# Caesar decryption mod 256
def C_dec(clave, texto):
    k = ord(clave)
    k_inv = 256 - k                     # Inverse key in modular arithmetic
    inv_char = chr(k_inv)
    return C_enc(inv_char, texto)      # Use encryption function with inverse key

# Parameters
clave = 'w'
texto_original = loxica

# Encrypt and decrypt
texto_cifrado = C_enc(clave, texto_original)
texto_descifrado = C_dec(clave, texto_cifrado)

# Save results to a new text file
with open('cifrado_descifrado.txt', 'w', encoding='utf-8') as f:
    f.write("Type of cipher: Caesar cipher mod 256\n")
    f.write(f"Key used for encryption: '{clave}' (ASCII {ord(clave)})\n\n")
    f.write("Encrypted text:\n")
    f.write(texto_cifrado + "\n\n")
    f.write("Decrypted text:\n")
    f.write(texto_descifrado)

import string  # Mover esta importación al inicio del archivo

# Function to calculate absolute frequency of a character
def fa(c, text):
    return text.count(c)

# Function to calculate relative frequency of a character
def fr(c, text):
    return round(fa(c, text) / len(text), 4)

# Returns the 10 most frequent characters in the text
def top10(text):
    freq_list = [[fr(chr(i), text), chr(i)] for i in range(256)]
    freq_list.sort(reverse=True)
    return freq_list[:10]

# Caesar decryption using a single character key
def C_Dec(key_char, text):
    k = ord(key_char)
    k_inv = 256 - k  # inverse key for decryption in modular arithmetic
    decryption_key = chr(k_inv)
    return C_enc(decryption_key, text)  # usar C_enc, no C_Enc

# Frequency analysis attack (tries to guess Caesar key)
def C_X(ciphertext, reference_text):
    most_freq_ref_char = top10(reference_text)[0][1]
    most_freq_cipher_char = top10(ciphertext)[0][1]
    k = (ord(most_freq_cipher_char) - ord(most_freq_ref_char)) % 256
    key = chr(k)
    return C_Dec(key, ciphertext)

# Save results in a single file
def full_analysis(ciphertext, reference_text, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("Letter frequency analysis (relative frequencies)\n")
        f.write("Only lowercase a–z are considered.\n\n")

        for letter in string.ascii_lowercase:
            freq = fr(letter, reference_text.lower())
            f.write(f"{letter}: {freq}\n")

        f.write("\nTop 10 most frequent characters in reference text:\n")
        for freq, char in top10(reference_text):
            f.write(f"{repr(char)}: {freq}\n")

        f.write("\nTop 10 most frequent characters in ciphertext:\n")
        for freq, char in top10(ciphertext):
            f.write(f"{repr(char)}: {freq}\n")

        decrypted_text = C_X(ciphertext, reference_text)
        f.write("\n--- Decrypted text using frequency analysis ---\n")
        f.write(decrypted_text)

# Example usage (assuming loxica is the original text and texto_cifrado is the encrypted version)
full_analysis(texto_cifrado, loxica, "analysis_output.txt")
