#7) Se consideră trei numere întregi. Dacă toate sunt pozitive, să se afişeze numărul mai mare dintre al doilea şi al treilea număr, în
#caz contrar să se calculeze suma primelor două numere. Exemple: Date de intrare 45 23 100 date de ieşire 100 ; Date de
#intrare 34 -25 10 Date de ieşire 9.
a=int(input("primul nr:"))
b=int(input("al doilea nr:"))
c=int(input("al treilea nr:"))
if ((a and b and c)>0):
    if(b>c):
        print(b)
    elif(b==c):
        print(b or c)
    else:
        print(c)
else:
    print(a+b)
