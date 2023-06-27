import random

alphabets = ['a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']

plainText = 'ezztomizihere'
cipher = ''
cipherWord = ''
decipherWord = ''


for i in range(len(plainText)):
    cipher = cipher + alphabets[random.randint(0,25)%26]


for i in range(len(plainText)):
    letter = alphabets.index(plainText[i]) + alphabets.index(cipher[i])
    letter %= 26
    cipherWord = cipherWord+alphabets[letter]

print(cipherWord)

for i in range(len(cipherWord)):
    letter = alphabets.index(cipherWord[i]) - alphabets.index(cipher[i])
    letter %= 26
    decipherWord = decipherWord + alphabets[abs(letter)]

print(decipherWord)