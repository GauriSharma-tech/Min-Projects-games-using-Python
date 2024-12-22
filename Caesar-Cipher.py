import string 
alphabets = list(string.ascii_lowercase )
print(alphabets)


def encryption(plain_text,shift): #hello (h=7) (shift=3)
   cipher_text=""
   for char in plain_text:
     if char in alphabets:
       position=alphabets.index(char);
       new_position=(position+shift)%26;
       cipher_text+=alphabets[new_position]
     else:
        cipher_text+=char
    
   print(f"Here's the encrypted text:\n{cipher_text}")

def decryption(cipher_text,shift):
   plain_text=""
   for char in cipher_text:
      if char in alphabets:
       position=alphabets.index(char);
       new_position=(position-shift)%26;
       plain_text+=alphabets[new_position]
      else:
         plain_text+=char
   print(f"Here's the decrypted text:\n{plain_text}")
      
wanna_end=False
while not wanna_end:
    what_to_do=input("Type 'encrypt' for encryption,'decrypt' for decryption:\n");
    text=input("Type your message:\n").lower();
    shift=int(input("enter shift key:\n"))
    if what_to_do=="encrypt":
       encryption(text,shift);
    elif what_to_do=="decrypt":
        decryption(text,shift);
    play_again=input("Type 'yes' to continue and type 'no' to exit:\n")
    if(play_again=='no'):
       wanna_end=True
       print("Have a nice day !!")
    else:
       wanna_end=False