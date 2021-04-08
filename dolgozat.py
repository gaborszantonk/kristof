print("Ez a program megszámolja,\n hányféle karakter van a te általad beírt karakter sorozatban!")
a = input("Add meg a karaktersorozatot!: ")
n: str = ""
db: int = 0
if a == "":
    print("Nem  is adtál meg semmit!")
else:
    n = a[0]
    db += 1
    for cv in range(1, len(a), 1):
        for i in range(len(n)):
            if a[cv] not in n:
                db += 1
                n = n + a[cv]
if n == "":
    print("Nincs mit kiírnom!")
else:
    print("Az eltérő karakterek száma " + str(db))
    for b in range(len(n)):
        print("A " +str(b + 1) + ". elem: " + n[b])
