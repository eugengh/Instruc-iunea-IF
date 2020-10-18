#14)Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
#Exemplu : date de intrare : n=69 date de ieşire : casuta 17.
a=int(input("Ionel a sosit al: "))
if a>0:
    if a%4==0:
        print("Ionel s-a cazat in casuta: ",a//4) 
    elif a%4!=0:
        print("Ionel s-a cazat in casuta:",(a//4)+1)