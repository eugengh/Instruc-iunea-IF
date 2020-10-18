#3) Să se verifice dacă o literă introdusă este vocală sau consoană. Exemplu : Date de intrare a Date de ieşire vocala.
l = input("litera:")
if l in('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
    print("Vocala")
elif l in('q','Q','w','W','r','R','t','T','y','Y','p','P','s','S','d','D','f','F','g','G','h','H','j','J','k','K','l','L','z','Z','c','C','v','V','b','B','n','N','m','M'):
    print("consoana")