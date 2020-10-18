#12)“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă
#iubeşte …. Exemplu: Date de intrare: x=10 Date de ieşire: … de loc.
a=int(input("nr de petale: "))
b="Ma iubeste un pic"
f="Ma iubeste mult"
c="Ma iubeste cu pasiune"
d="Ma iubeste la nebunie"
e="Ma iubeste de loc"

if a>0:
    if (a-(a//6)*6)==0:
        print(b)
    elif (a-(a//6)*6)==1:
        print(f)
    elif (a-(a//6)*6)==2:
        print(c)
    elif (a-(a//6)*6)==3:
        print(d)
    elif (a-(a//6)*6)==4:
        print(e)
else:
    print("Error")
