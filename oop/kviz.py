states = {
    "Slovenija":"Ljubljana",
    "Avstrija":"Dunaj",
    "Italija":"Rim",
    "Francija":"Pariz"
}

class Kviz:
    def povej_mesto(self, mesto):
        return states[mesto]

    def Vnos(self, drzava):
        return raw_input("Vnesi glavno mesto drzave " + drzava + ":")

    def main(self):
        stevec = 0

        for x in states.keys():
            mesto = self.Vnos(x)
            if states[x] == mesto:
                stevec += 1
                print "Bingo!"
            else:
                print "Slabo"
                print "Pravilen odgovor je " + self.povej_mesto(x)


        print "Stevilo pravilnih odgovorov je: {}".format(stevec)



class KvizTest(Kviz):
    def Vnos(self, drzava):
        return "Pariz"

def test():
    kviz_test = KvizTest()
    kviz_test.main()

if __name__ == '__main__':
    print("Start test")
    test()
    print("Start kviz")
    kviz = Kviz()
    kviz.main()

