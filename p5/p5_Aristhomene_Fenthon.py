def caesar_cipher(text, shift):
    encrypted = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char

    return encrypted


def caesar_decipher(cyphertext, shift):
    decrypted = ""

    for i in range(len(cyphertext)):
        char = cyphertext[i]

        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char

    return decrypted


def letter_frequency(text):
    frequency = {}

    for i in range(len(text)):
        char = text[i].lower()

        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency


def main():
    message = input("Enter a message: ")
    shift = int(input("Enter the shift value: "))

    while True:
        print("\n--- Caesar Cipher Menu ---")
        print("1. View ciphered text")
        print("2. View letter frequency")
        print("3. View deciphered text")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Ciphered text:", caesar_cipher(message, shift))

        elif choice == "2":
            print("Letter frequency:")

            frequency = letter_frequency(message)

            for letter in frequency:
                print(letter, ":", frequency[letter])

        elif choice == "3":
            ciphered = caesar_cipher(message, shift)
            print("Deciphered text:", caesar_decipher(ciphered, shift))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()