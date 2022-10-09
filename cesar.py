def crypty(message, key):
    arr = list(message)
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(arr)):
        step = (alph.index(message[i])+key)%26
        if step < 0:
            step = 26 + step
        arr[i] = alph[step]
    return ''.join(arr)

def cracker(cipher,message):
    for i in range(0,26):
        test = crypty(cipher,i)
        isTrue = "0"
        if(test == message):
            isTrue = "1"
        print("try numbeer ["+str(i+1)+"] ==> "+test+"     "+isTrue)

key = 2
message = "abcdzx"
cipher = crypty(message,key)
clearText = crypty(cipher,-key)
print("real message is : "+message)
print("cipher text is : "+cipher)
print("clear text is : "+clearText)


cracker(cipher,message)
