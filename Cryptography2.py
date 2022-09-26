#This is a Ceaser cypher encoder so you can enter any word and enter the shift value you would like to add



Plaintext_input = (input("Enter a word to shift in ceaser cypher:"))
S = (int(input("enter shift pattern you would like:")))
new_list = [*Plaintext_input]
encrypt_list = []
for i in range(len(new_list)):
    new_list1 = ord(new_list[i])
    crpyt = new_list1+S
    if crpyt > 122:
        crpyt = 95+S
    encrypt = chr(crpyt)
    encrypt_list.append(encrypt)
    cipher = ''.join(encrypt_list)
    
               



print("Plain text :" + Plaintext_input)
print("Shift pattern: " + str(S))
print("Cipher:",cipher)

