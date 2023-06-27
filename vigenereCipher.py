alphabets = ['a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']

def encryption(plainText,keyword):
    plainText = plainText.lower()
    cipherText = ""
    ptr = 0
    for i in range(len(plainText)):
        if(plainText[i] == " "):
            cipherText += " "
            continue
        if(ptr == len(keyword)) : ptr = 0
        key = alphabets.index(keyword[ptr])
        letter = (alphabets.index(plainText[i]) + key) % 26
        cipherText += alphabets[letter]
        ptr += 1
    return cipherText.upper()

def decryption(cipherText,keyword):
    cipherText = cipherText.lower()
    plainText = ""
    ptr = 0
    for i in range(len(cipherText)):
        if(cipherText[i] == " "):
            plainText += " "
            continue
        if(ptr == len(keyword)) : ptr = 0
        key = alphabets.index(keyword[ptr])
        letter = (alphabets.index(cipherText[i]) - key) % 26
        plainText += alphabets[letter]
        ptr += 1
    return plainText
