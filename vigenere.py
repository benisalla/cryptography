def crypty(message, key):
    arr = list(message)
    alph = "abcdefghijklmnopqrstuvwxyz"
    arrkey = list(key)
    for i in range(0,len(arr)):
        index = alph.index(message[i])
        arr[i] = arrkey[index]
    return ''.join(arr)

def decrypt(message, key):
    arr = list(message)
    alph = "abcdefghijklmnopqrstuvwxyz"
    arrkey = list(key)
    for i in range(0,len(arr)):
        index = arrkey.index(message[i])
        arr[i] = alph[index]
    return ''.join(arr)


key = "abcdefghijklmnopqrstuvwxyz"
key = list(key)
key.reverse()
key=''.join(key)
print(key)

message = "abcdzx"
cipher = crypty(message,key)
clearText = decrypt(cipher,key)
print("real message is : "+message)
print("cipher text is : "+cipher)
print("clear text is : "+clearText)

