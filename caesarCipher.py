alphabets = ['a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']


def Encryption(plainText,key):
    plainText = plainText.lower()
    cipherText = ''
    for i in range(len(plainText)):
        if plainText[i] != " ":
            letter = (alphabets.index(plainText[i]) + key) % 26
            cipherText += alphabets[letter]
        else:
            cipherText += " "
    return cipherText.upper()

def Decryption(cipherText,key):
    cipherText = cipherText.lower()
    plainText = ''
    for i in range(len(cipherText)):
        if cipherText[i] != " ":
            letter = (alphabets.index(cipherText[i]) - key) % 26
            plainText += alphabets[letter]
        else:
            plainText += " "
    return plainText


