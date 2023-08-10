from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True


# def encrypt(plain_text, shift_ammount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_ammount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_ammount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_ammount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter

#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_ammount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_ammount=shift)


def caesar(start_text, shift_ammount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_ammount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_ammount
            new_char = alphabet[new_position]
            end_text += new_char
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


print(logo)
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    final_shift = shift % 26
    caesar(start_text=text, shift_ammount=final_shift, cipher_direction=direction)
    keep_running = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if keep_running == "no":
        should_continue = False
        print("Good bye")
