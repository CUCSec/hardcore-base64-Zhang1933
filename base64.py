
# def debug(a):
#     print("###{}###".format(a))


def garph():
    for i in range(0,26):
        arr.append(chr(i+65))
    for i in range(0,26):
        arr.append(chr(i+97))
    for i in range(0,10):
        arr.append(chr(i+48))
    arr.append('+')
    arr.append('/')

arr=[]
garph()
# for i in range(0,64):
#     debug(arr[i])
 


def EnCode():
    origin=input()
    addEq=0
    if len(origin)%3 !=0:
        addEq=3-len(origin)%3
    res=""

    for char in origin:
        tmp=bin(ord(char))[2:]
        tmp=tmp.zfill(8)
        res+=tmp
    
    if len(res)%6 != 0:
        res=res.ljust(6-len(res)%6+len(res),'0')

    for i in range(0,len(res),6):
        print(arr[int(res[i:i+6] , base=2)],end='')

    for i in range(0,addEq):    
        print('=',end='')
    print('')

def DeCode():
    deco=input()
    res=''
    for char in deco:
        if char!='=':
            res+=bin(arr.index(char))[2:].rjust(6,'0')

    for i in range(0,len(res),8):

        print( chr( int( res[i:i+8],2)),end='')
    print('')

while(1):

    judge=input("if you want to encode please input 1,decode input 2,exit the programm input 3:\n")
    if(judge=='3'):
        break

    elif judge=='1':
        print("encode：")
        EnCode()

    elif judge=='2':
        print('decode')
        DeCode()

    else:
        print('大哥！输入其他字符是没用的')

