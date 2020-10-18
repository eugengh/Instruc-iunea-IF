#10)La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
#fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
#afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
#numărul de boabe de porumb. Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe.
a=int(input("Nr de gaini:"))
b=int(input("Numarul de boabe de porumb:"))
if (b%(a+1)==0):
    print("egalitate")
elif(b%(a+1)!=0):
    print("curcanul a primit cu ", (b%(a+1)), "boabe mai mult")