print("Ez a program addig működik, amíg pozitív számokat adsz meg.\n A pozitív számokat összeadja, ha nullát ütsz; negatív esetén leáll.")
ossz: int = 0
a: int = 1
while a > 0:
    a = int(input("Adj meg pozítív számokat!: "))
    if a < 0:
        ossz += a
    elif a == 0:
        break
else:
    print("Kiléptem, mert negatív számot ütöttél!")
if a == 0:
    print("Kiléptem, mert 0-át ütöttél!")
