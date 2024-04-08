def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

if __name__ == "__main__":
    choice = int(input("1. Encrypt\n2. Decrypt\nEnter your choice: "))
    text = input("Enter the text: ")
    if choice == 1:
        shift = int(input("Enter the shift value: "))
        encrypted_text = encrypt(text, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 2:
        shift = int(input("Enter the shift value: "))
        decrypted_text = decrypt(text, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice.")
