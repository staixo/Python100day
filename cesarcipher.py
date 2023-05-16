def caesar(typecode, message, shift):
    match typecode:
        case 'encode':
            new_message = ''
            for letter in message:
                new_message += chr(ord(letter) + shift)
            print(f"The encoded message is: {new_message}")
        case 'decode':
            new_message = ''
            for letter in message:
                new_message += chr(ord(letter) - shift)
            print(f"The decoded message is: {new_message}")

typecode=''
while typecode != 'encode' and typecode != 'decode':
    typecode = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: "))

message = str(input("Type your message: "))

shift = int(input("Type the shift number: "))
end = 0
while end == 0:
    caesar(typecode, message, shift)
    end = int(input("Type 0 to continue, or any other number to quit: "))