alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(direction, text, shift):
    if direction not in ["encode", "decode"]:
        print("Sorry, you entered the wrong direction.")
        return

    cipher_text = ''
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == "encode":
                new_index = (index + shift) % len(alphabet)
            else: # for decode
                new_index = (index - shift) % len(alphabet)
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    
    print(f"The {direction}d text is: {cipher_text}")
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    result = input("type 'yes' if you want to go again, otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("goodBye")