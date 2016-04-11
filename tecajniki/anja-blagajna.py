cenik_izdelkov = {"banane" : 1.45, "kruh": 1.50 , "mleko": 0.50, "kava": 3.80}

def get_price(izdelek):
    cena = 0
    if izdelek in cenik_izdelkov.keys():
        cena = cenik_izdelkov[izdelek]
    return cena

for izdelek in cenik_izdelkov:
    print izdelek, cenik_izdelkov[izdelek]


if __name__ == "__main__":
    while True:
        izberi_izdelek = str(raw_input("Izberi izdelek: "))

        cena = get_price(izberi_izdelek)
        if (cena != 0):
            print "Cena izdelka je %s" % (cena)
        else:
            print "Tega izdelka ni."
            break