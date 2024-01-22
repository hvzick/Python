import sys
def main():
    try:
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        choice = int(input("Enter 1 to Encrypt\nEnter 2 to Decrypt\n"))
        match choice:
            case 1:
                message = input("Enter Text to Encrypt: ").upper()
                key = int(input("Enter Key: "))

                encryptedMessage = encrypt(message, key, alphabets)
                print(encryptedMessage)
            case 2:
                message = input("Enter Text to Decrypt: ").upper()
                key = int(input("Enter Key: "))

                decryptedMessage = decrypt(message, key, alphabets)
                print(decryptedMessage)
    except ValueError:
        sys.exit('Invalid Input')

def encrypt(eMessage, key, alphabets):
    encryptedMessage = ""
    for char in eMessage:
        position = alphabets.index(char)
        newPostiton = position + key
        newMessage = alphabets[newPostiton]
        encryptedMessage += newMessage
    return f"The encrypted message is: {encryptedMessage}"

def decrypt(eMessage, key, alphabets):
    decryptedMessage = ""
    for char in eMessage:
        position = alphabets.index(char)
        newPostiton = position - key
        newMessage = alphabets[newPostiton]
        decryptedMessage += newMessage
    return f"The decrypted message is: {decryptedMessage}"


if __name__ == "__main__":
    main()