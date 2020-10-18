#6) Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate
#notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele
#luate şi afişaţi notele pe care le va comunica părinţilor. Exemple : Date de intrare 6 9 9 Date de ieşire 6 9 9 ; Date de
#intrare 8 5 7 Date de ieşire 8.
a=int(input("prima nota:"))
b=int(input("a doua nota:"))
c=int(input("a treia nota:"))
if ((a and b and c )<=10) and ((a and b and c)>0):
    if c>=8:
        print(a,b,c)
    elif c<8:
        if a>b:
            print(a)
        elif a==b:
            print(a or b)
        else:
            print(b)
else:
    print("error")
            