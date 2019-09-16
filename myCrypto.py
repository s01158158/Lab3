def Crypto(text):      #Used Scramble Encryption
  evens = ""
  odds = ""
  Amount = 0
  for i in text:
    if Amount % 2 == 0:
      evens = evens + i
    else:
      odds = odds + i
    Amount = Amount + 1
  cipher = odds + evens
  return cipher
  
Crypto("Hello World")

#Output is 'el olHloWrd'



def CryptoDecrypt(cipher):    # CryptoDecrypt code is used without Crypto code or will get errors.
    halfL = len(cipher) // 2
    odds = cipher[:halfL]
    evens = cipher[halfL:]
    text = ""
    for n in range(halfL):
        text = text + evens[n]
        text = text + odds[n]
    if len(odds) < len(evens):
        text = text + evens[-1]
    return text
    
CryptoDecrypt("el olHloWrd")

# Output is 'Hello World'
