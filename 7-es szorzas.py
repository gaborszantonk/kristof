print("Kiírom a 7-es szorzó tábla első 20 elemét \n és megmondom melyik osztható 3-mal!")
cv: int = 0
while cv < 20:
    cv += 1
    b = (7*cv)
    if b % 3 == 0:
        print(str(b) + "*")
    else:
        print(str(b))
