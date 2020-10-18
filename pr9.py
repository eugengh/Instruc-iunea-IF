#9) Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
#câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
#numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
#Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
#bilelor: 17 Mari: 11 bile Verzi: 7 bile .
a=int(input("bile albe mari:"))
a1=int(input("bile albe mici:"))
r=int(input("bile rosii mari:"))
r1=int(input("bile rosii mici:"))
v=int(input("bile verzi mari:"))
v1=int(input("bile verzi mici:"))
print("In total pe masa sunt: ",(a+a1+r+r1+v+v1), " bile")
if (a+r+v)>(a1+r1+v1):
    print("Mai multe sunt bile mari: ",(a+r+v))
elif (a+r+v)==(a1+r1+v1):
    print("Nr bilelor mici = nr bilelor mari")
else:  
    print("Mai multe sunt bile mici: ",(a1+r1+v1))
if (a+a1)>(r+r1) and (a+a1)>(v+v1):
    print("cele mai numeroase sunt bilele albe:", (a+a1))
elif (r+r1)>(a+a1) and (r+r1)>(v+v1):
    print("cele mai numeroase sunt bilele rosii:", (r+r1))
elif (v+v1)>(a+a1) and (v+v1)>(r+r1):
    print("cele mai numeroase sunt bilele verzi:", (v+v1))
elif (a+a1)==(v+v1)==(r+r1):
    print("toate sunt egale")