#8) Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de
#ieşire nu exista numar par ; Date de intrare 28 14 Date de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4
a=int(input("primul nr:"))
b=int(input("al doilea nr:"))
if (a%2==0) and (b%2==0):
    if a>b:
        print(a)
    elif a==b:
        print(a or b)
    else:
        print(b)
elif (a%2==0) and (b%2!=0):
    print("a -  par, b - impar")
elif (a%2!=0) and (b%2==0):
    print("a -  impar, b - par")
else:
    print("a, b - impare")