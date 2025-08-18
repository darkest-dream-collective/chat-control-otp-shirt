import secrets
from string import ascii_letters

str_num_conv_table = {v:k for k,v in enumerate(ascii_letters + ".,?! ")}
num_str_conv_table = {v:k for k,v in str_num_conv_table.items()}
MAX_KEY_ID = max(num_str_conv_table.keys()) + 1

nums_to_str = lambda nums: [num_str_conv_table[num] for num in nums]

generate_key = lambda plaintext: \
    "".join(nums_to_str([secrets.randbelow(MAX_KEY_ID) for _ in plaintext]))
encrypt = lambda plaintext, key: \
    "".join(nums_to_str([(str_num_conv_table[plaintext[i]] + \
    str_num_conv_table[key[i]]) % MAX_KEY_ID for i in 
    range(len(plaintext))]))
decrypt = lambda cyphertext, key:  \
    "".join(nums_to_str([(str_num_conv_table[cyphertext[i]] - \
    str_num_conv_table[key[i]]) % MAX_KEY_ID for i in 
    range(len(cyphertext))]))

if __name__=="__main__":
    # Option 1: Randomly generated key
    message = "YOUR PRIVATE MESSAGE GOES HERE..."
    key = generate_key(message)
    cyphertext = encrypt(message, key)
    recovered_message = decrypt(cyphertext, key)
    print(f"PLAINTEXT: {message}\nKEY: {key}\nCYPHERTEXT: {cyphertext}\
        \nRECOVERED_TEXT: {recovered_message}\n")
    
    # Option 2: User provided key
    user_encr_key = "ARE YOU GOING TO BAN CALCULATORS?"
    cyphertext = encrypt(message, user_encr_key)
    recovered_message = decrypt(cyphertext, user_encr_key)
    print(f"PLAINTEXT: {message}\nKEY: {user_encr_key}\nCYPHERTEXT: {cyphertext}\
        \nRECOVERED_TEXT: {recovered_message}")