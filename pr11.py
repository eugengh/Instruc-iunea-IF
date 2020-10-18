#11)Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau
#IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par
a=int(input("primul nr:"))
b=int(input("al doilea nr:"))
c=int(input("al treilea nr:"))
if a%2==0:
    print(a, "par")
else:
    print(a, "impar")
if b%2==0:
    print(b, "par")
else:
    print(b, "impar")
if c%2==0:
    print(c, "par")
else:
    print(c, "impar")