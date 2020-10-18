#1) Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. Exemplu : Date de
#intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de ieşire punctaj maxim are elevul cu nr crt 7.
a=int(input("Nr. curent elev:"))
a1=int(input("Punctajul la elevul "+str(a)+ " :"))
b=int(input("Nr. curent elev:"))
b1=int(input("Punctajul la elevul "+str(b)+ " :"))
c=int(input("Nr. curent elev:"))
c1=int(input("Punctajul la elevul "+str(c)+ " :"))
if(a1>b1) and(a1>c1):
    print("Nr. curent: "+str(a) + " cu punctajul de "+str(a1)+" puncte")
elif(b1>a1) and(b1>c1):
    print("Nr. curent: "+str(b) + " cu punctajul de "+str(b1)+" puncte")
elif(c1>b1) and(c1>a1):
    print("Nr. curent: "+str(c) + " cu punctajul de "+str(c1)+" puncte")
else:
    print("Toate sunt egale")
