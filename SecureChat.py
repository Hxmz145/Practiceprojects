#Its an encryptor and decryptor so you can add any plaintext you want and it will encrypt it in 
#Ceaser Cipher,DES,AES,OTP,RSA,Columnar and Rail fence encryption



import tkinter
from tkinter import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
import numpy as np
import onetimepad
import random
import string
import rsa
import hashlib
from hashlib import blake2b
import cryptography
import math




root = Tk()

root.minsize(1000,600)
root.maxsize(1000,600)
securechat = Label(root,text="Sender")
chat_enter = Entry()
word = 0


#Ceaser cypher shift button
shift = Label(root,text="Ceaser cypher shift value")
shift.place(x=150,y=200)
s = Entry(width=5)
s.place(x=180,y=220)

#Playfair keyword
playfair_keyword = Label(root,text="keyword")
playfair_keyword.place(x=150,y=250)
keyword = Entry()
keyword.place(x=150,y=270)


def Rail_fence():
    Railtext = f"{chat_enter.get()}"
    Railkey = int(s.get())
    rail = [['\n' for i in range(len(Railtext))]
                  for j in range(Railkey)]
    dir_down = False
    Railrow, Railcol = 0, 0
    for i in range(len(Railtext)):
        if (Railrow == 0) or (Railrow == Railkey - 1):
            dir_down = not dir_down
        rail[Railrow][Railcol] = Railtext[i]
        Railcol += 1

        if dir_down:
            Railrow += 1
        else:
            Railrow -= 1
    Railresult = []
    for i in range(Railkey):
        for j in range(len(Railtext)):
            if rail[i][j] != '\n':
                Railresult.append(rail[i][j])
    Railcipher = "".join(Railresult)
    key.config(text=f"Key:{Railkey}")
    ciphertext.config(text=f"Ciphertext:{Railcipher}")
    def Raildecrypt():
        drail = [['\n' for i in range(len(Railcipher))]
                       for j in range(Railkey)]
        ddir_down = None
        drow,dcol = 0,0

        for i in range(len(Railcipher)):
            if drow == 0:
                ddir_down = True
            if drow == Railkey - 1:
                ddir_down = False

            drail[drow][dcol] = "*"
            dcol += 1

            if ddir_down:
                drow += 1
            else:
                drow -= 1
        index = 0
        for i in range(Railkey):
            for j in range(len(Railcipher)):
                if ((drail[i][j] == '*') and
                    (index < len(Railcipher))):
                    drail[i][j] = Railcipher[index]
                    index += 1
        dresult = []
        drow,dcol = 0, 0
        for i in range(len(Railcipher)):
            if drow == 0:
                ddir_down = True
            if drow == Railkey-1:
                ddir_down = False

            if (drail[drow][dcol] != '*'):
                dresult.append(drail[drow][dcol])
                dcol += 1
            if ddir_down:
                drow += 1
            else:
                drow -= 1
        Railplain = "".join(dresult)
        Reciver_plaintext.config(text=f"Plaintext:{Railplain}")
    def Railsend():
        Reciver_key.config(text=f"Key:{Railkey}")
        Reciver_Ciphertext.config(text=f"Ciphertext:{Railcipher}")
    Railsend_button = Button(root,text="Send",command=Railsend)
    Railsend_button.place(x=300,y=50)
    Raildecrypt_button = Button(root,text="Decrypt",command=Raildecrypt)
    Raildecrypt_button.place(x=600,y=310)

def columnar():
    colummnar_key = f"{keyword.get()}"
    msg = f"{chat_enter.get()}"
    Columnar_cipher = ""
    ck_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    ck_lst = sorted(list(colummnar_key))
    col = len(colummnar_key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col)- msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i:i + col]
              for i in range(0,len(msg_lst), col)]
    for _ in range(col):
        curr_idx = colummnar_key.index(ck_lst[ck_indx])
        Columnar_cipher += ''.join([row[curr_idx]
                                    for row in matrix])
        ck_indx += 1
    ciphertext.config(text=f"Ciphertext:{Columnar_cipher}")
    key.config(text=f"Key:{colummnar_key}")
    def Columnar_send():
        Reciver_Ciphertext.config(text=f"Ciphertext:{Columnar_cipher}")
        Reciver_key.config(text=f"Key:{colummnar_key}")
    def Columnar_decryption():
        orig_msg = ""
        dec_cocipher = []
        msg_indx2 = 0
        ck_indx2 = 0
        msg_len2 = float(len(Columnar_cipher))
        msg_lst2 = list(Columnar_cipher)
        for _ in range(row):
            dec_cocipher += [[None] * col]
        for _ in range(col):
            curr2_idx = colummnar_key.index(ck_lst[ck_indx2])
            for j in range(row):
                dec_cocipher[j][curr2_idx] = msg_lst2[msg_indx2]
                msg_indx2 += 1
            ck_indx2 += 1
        try:
            orig_msg = ''.join(sum(dec_cocipher, []))
        except TypeError:
            raise TypeError("This program cannot handle repeating words")
        null_count = msg.count("_")
        if null_count > 0:
            final_msg = orig_msg[: -null]
        Reciver_plaintext.config(text=f"Plaintext:{orig_msg}")
    Columnar_sendbutton = Button(root,text="Send",command=Columnar_send)
    Columnar_sendbutton.place(x=300,y=50)
    Columnar_dbutton = Button(root,text="Decrypt",command=Columnar_decryption)
    Columnar_dbutton.place(x=600,y=310)


def Polyalphabetic():
    poly_input = f"{chat_enter.get()}"
    polys_keyword = f"{keyword.get()}"
    polykey = list(polys_keyword)
    if len(poly_input) != len(polykey):
        for i in range(len(poly_input)-len(polykey)):
            polykey.append(polykey[i % len(polykey)])
            final_polykey = ''.join(polykey)
            key.config(text=f"Key:{final_polykey}")
            poly_encrypttext = []
            for i in range(len(poly_input)):
                x = (ord(poly_input[i]) + ord(final_polykey[i])) % 26
                x += ord("A")
                poly_encrypttext.append(chr(x))
                poly_cipher = ''.join(poly_encrypttext)
                ciphertext.config(text=f"Ciphertext:{poly_cipher}")
                def poly_decryption():
                    polyorig_text = []
                    for i in range(len(poly_cipher)):
                        y = (ord(poly_encrypttext[i]) - ord(final_polykey[i]) + 26) % 26
                        y += ord("A")
                        polyorig_text.append(chr(y))
                        poly_original = "".join(polyorig_text)
                        Reciver_plaintext.config(text=f"Plaintext:{chat_enter.get()}")
                def poly_send():
                    Reciver_Ciphertext.config(text=f"Ciphertext:{poly_cipher}")
                    Reciver_key.config(text=f"Key:{final_polykey}")
                poly_sendbutton = Button(root,text="Send",command=poly_send)
                poly_sendbutton.place(x=300,y=50)
                poly_decryptbutton = Button(root,text="Decrypt",command=poly_decryption)
                poly_decryptbutton.place(x=600,y=310)

def DES_Encryption():
    DES_input = f"{chat_enter.get()}"
    DES_data = DES_input.encode('utf-8')
    DES_key = get_random_bytes(8)
    DES_cipher = DES.new(DES_key, DES.MODE_OFB)
    DES_ciphertext = DES_cipher.iv + DES_cipher.encrypt(DES_data)
    key.config(text=f"Key:{DES_key}")
    ciphertext.config(text=f"Ciphertext:{DES_ciphertext}")
    def DES_Decryption():
        DES_decrypt = DES_ciphertext - DES_cipher.encrypt(DES_data)
        Reciver_plaintext.config(text=f"Plaintext:{DES_decrypt}")
    def DES_send():
        Reciver_Ciphertext.config(text=f"Ciphertext:{DES_ciphertext}")
        Reciver_key.config(text=f"{DES_key}")
    DES_sendbutton = Button(root,text="send",command=DES_send)
    DES_sendbutton.place(x=300,y=50)


def AES_Encryption():
    AES_input = f"{chat_enter.get()}"
    data = AES_input.encode('utf-8')
    AES_key = get_random_bytes(16)
    AES_cipher = AES.new(AES_key, AES.MODE_EAX)
    AES_ciphertext,tag = AES_cipher.encrypt_and_digest(data)
    AES_nonce = AES_cipher.nonce
    key.config(text=f"Key:{AES_key}")
    ciphertext.config(text=f"Ciphertext:{AES_ciphertext}")
    def AES_decryption():
        AES_decrypt = AES.new(AES_key,AES.MODE_EAX,nonce=AES_nonce)
        AES_decrypt.update(AES_input)
        AES_plaintext = AES_cipher.decrypt_and_verify(AES_ciphertext, tag)
        Reciver_plaintext.config(text=f"Plaintext:{AES_input}")
    def AES_send():
        Reciver_Ciphertext.config(text=f"Ciphetext:{AES_ciphertext}")
        Reciver_key.config(text=f"Key:{AES_key}")
    AES_sendbutton = Button(root,text="send",command=AES_send)
    AES_sendbutton.place(x=300,y=50)
    AES_decryptbutton = Button(root,text="decrypt",command=AES_decryption)
    AES_decryptbutton.place(x=600,y=310)

def ceaser_cypher():
    new_list = [*chat_enter.get()]
    encrypt_list = []
    shift_value = int(s.get())
    for i in range(len(new_list)):
        new_list1 = ord(new_list[i])
        crpyt = new_list1+shift_value
        if crpyt > 122:
            crpyt = 95+shift_value
        encrypt = chr(crpyt)
        encrypt_list.append(encrypt)
        cipher = ''.join(encrypt_list)
        key.config(text=f"key:{shift_value}")
        ciphertext.config(text=f"Ciphertext:{cipher}")
        def cdecryption():
            decrypt_list = [*cipher]
            decrypt4 = []
            for i in range(len(decrypt_list)):
                decrypt1 = ord(decrypt_list[i])
                decrypt = decrypt1-shift_value
                if decrypt > 122:
                    decrypt = 95-shift_value
                decrypt2 = chr(decrypt)
                decrypt4.append(decrypt2)
                decipher = ''.join(decrypt4)
                Reciver_plaintext.config(text=f"plaintext:{decipher}")

        def csend():
            Reciver_Ciphertext.config(text=f"Ciphertext:{cipher}")
            Reciver_key.config(text=f"Key:{shift_value}")
        Csend_button = Button(root,text="Send",command=csend)
        Csend_button.place(x=300,y=50)
        cdecrypt = Button(root,text="decrypt",command=cdecryption)
        cdecrypt.place(x=600,y=310)


def OTP():
    OTP_list = []
    OTP_input = f"{chat_enter.get()}"
    OTP_input_list = [*chat_enter.get()]
    for i in range(len(OTP_input_list)):
        OTP_key = random.choice(string.ascii_letters)
        OTP_list.append(OTP_key)
        OTP_finalkey = " ".join(OTP_list)
        OTP_cipher = onetimepad.encrypt(OTP_input,OTP_finalkey)
        ciphertext.config(text=f"Ciphertext:{OTP_cipher}")
        key.config(text=f"Key:{OTP_finalkey}")
        def OTP_decryption():
            OTP_plain = onetimepad.decrypt(OTP_cipher,OTP_finalkey)
            Reciver_plaintext.config(text=f"Plaintext:{OTP_plain}")
        def OTP_send():
            Reciver_Ciphertext.config(text=f"Ciphertext:{OTP_cipher}")
            Reciver_key.config(text=f"Key:{OTP_finalkey}")
    OTPsend_button = Button(root,text="Send",command=OTP_send)
    OTPsend_button.place(x=300,y=50)
    OTPdecrypt_button = Button(root,text="Decrypt",command=OTP_decryption)
    OTPdecrypt_button.place(x=600,y=310)

def RSA():
    publickey, privatekey = rsa.newkeys(512)
    RSA_plaintext = f"{chat_enter.get()}"
    RSA_cipher = rsa.encrypt(RSA_plaintext.encode(),publickey)
    key.config(text=f"{publickey}")
    ciphertext.config(text=f"Ciphertext:{RSA_cipher}")
    def RSA_decryption():
        RSA_plain = rsa.decrypt(RSA_cipher, privatekey)
        Reciver_plaintext.config(text=f"Plaintext:{RSA_plain}")
    def RSA_send():
        Reciver_Ciphertext.config(text=f"Ciphertext:{RSA_cipher}")
        Reciver_key.config(text=f"Private Key:{privatekey}")
    RSAsend_button = Button(root,text="Send",command=RSA_send)
    RSAsend_button.place(x=300,y=50)
    RSAdecrpyt_button = Button(root,text="Decrypt",command=RSA_decryption)
    RSAdecrpyt_button.place(x=600,y=310)



root.title("SecureChat")
#Buttons
cipher_teqniques = Label(root,text="Encyption Teqniques")
Ceaser_Cypher = Button(root,text="Ceaser Cypher",fg="black",command=ceaser_cypher)
Polyalphabetic_button = Button(root,text="Polyalphabetic",command=Polyalphabetic)
DES_button = Button(root,text="DES",fg="black",command=DES_Encryption)
AES_button = Button(root,text="AES",fg="black",command=AES_Encryption)
OTP_button = Button(root,text="OTP",command=OTP)
RSA_button = Button(root,text="RSA",command=RSA)
Columnar_button = Button(root,text="Columnar",command=columnar)
Railfence_button = Button(root,text="Rail Fence",command=Rail_fence)

#Sender
plain_text = Label(root,text=f"Plaintext:",)
key = Label(root,text="key:")
ciphertext = Label(root,text=f"Ciphertext:")


#Reciver
reciever = Label(root,text="Reciver")
reciever.place(x=600,y=200)
Reciver_Ciphertext = Label(root,text="Ciphertext:")
Reciver_Ciphertext.place(x=600,y=220)
Reciver_key = Label(root,text="Key:")
Reciver_key.place(x=600,y=250)
Reciver_plaintext = Label(root,text="plaintext:")
Reciver_plaintext.place(x=600,y=280)


Railfence_button.place(x=10,y=415)
Columnar_button.place(x=10,y=390)
RSA_button.place(x=10,y=365)
OTP_button.place(x=10,y=340)
plain_text.place(x=10,y=60)
key.place(x=10,y=85)
ciphertext.place(x=10,y=120)
AES_button.place(x=10,y=315)
DES_button.place(x=10,y=290)
Polyalphabetic_button.place(x=10,y=265)
cipher_teqniques.place(x=10,y=200)
securechat.place(x=50,y=10)
chat_enter.place(x=80,y=58)
Ceaser_Cypher.place(x=10,y=240)
root.mainloop()
