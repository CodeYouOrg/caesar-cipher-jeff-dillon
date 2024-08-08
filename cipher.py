def get_encrypted_index(index:int, alpha_length:int, offset:int) -> int:
    offset_index = index + offset
    if offset_index > alpha_length:
        offset_index = offset_index % alpha_length
    
    return offset_index

def encrypt(character:str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encryption_offset = 5
    encrypted_index = get_encrypted_index(alphabet.index(character), 
                                 len(alphabet), 
                                 encryption_offset)
    encrypted_character = alphabet[encrypted_index]
    
    return encrypted_character

def main():
    sentence = input('Please enter a sentence: ').lower()
    encrypted_sentence = ""
    for character in sentence:
        if character.isalpha():
            encrypted_sentence = "".join([encrypted_sentence, 
                                          encrypt(character)])
        else:
             encrypted_sentence = "".join([encrypted_sentence, character])
    
    print("The encrypted sentence is:", encrypted_sentence)


if __name__ == "__main__":
    main()