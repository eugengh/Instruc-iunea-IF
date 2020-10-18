#5) Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
#exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
#de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani. 
a=int(input("anul curent:"))
l=int(input("luna curenta:"))
z=int(input("ziua curenta:"))
a1=int(input("anul nasterii:"))
l1=int(input("luna nasterii:"))
z1=int(input("ziua nasterii:"))
if ((a<=2020)and(l<=12)and(z<=31))and(l1<=12)and(z1<=31):
    if l>l1:
        print(a-a1,"ani")
    elif l<l1:
        print((a-a1)-1, "ani")
    elif l==l1:
        if z<z1:
            print((a-a1)-1,"ani")
        elif z>z1:
            print(a-a1, "ani")
        elif z==z1:
            print(a-a1, "ani")
else:
    print("error")
        
        
        

