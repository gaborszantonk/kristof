print("Ez a program megszámolja,\n hányféle karakter van a te általad beírt karakter sorozatban!")
a = input("Add meg a karaktersorozatot!: ")
b = ""
if a == "":
    print("Nem  is adtál meg semmit!")
else:
    for cv in range(len(a)):
        print("Ez a(z) " + str(cv + 1) + ". elem: " + a[cv])
