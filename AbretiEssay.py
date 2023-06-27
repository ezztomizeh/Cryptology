alphabets = ['a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']


def encryption(plianText,key1,key2):
    cipherText = ""
    plianText = plianText.lower()
    for i in range(len(plianText)):
        if(plianText[i] == "") : continue
        elif(i%2 == 0 ) : letter = (alphabets.index(plianText[i]) + key1) % 26
        else : letter = (alphabets.index(plianText[i]) + key2) % 26
        cipherText += alphabets[letter]
    return cipherText.upper()

def Decryption(cipherText,key1,key2):
    plianText = ""
    cipherText = cipherText.lower()
    for i in range(len(cipherText)):
        if(cipherText[i] == "") : continue
        elif(i%2 == 0) : letter = (alphabets.index(cipherText[i]) - key1) % 26
        else : letter = (alphabets.index(cipherText[i]) - key2) % 26
        plianText += alphabets[letter]
    plianText = plianText.replace("a"," ")
    return plianText


