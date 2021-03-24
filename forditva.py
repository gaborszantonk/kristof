a = input("Adj megy egy karakter sorozatot és én kiírom visszafele!")
print(a)
b: str = ""
for cv in range(len(a)-1,  -1, -1):
    b = b + a[cv]
print(b)
if a == b:
    print("Ez plaindrom!")
else:
    print("Ez nem az!")
