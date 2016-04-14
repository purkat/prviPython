'''
class IzdelekKg:
    def __init__(self, ime, cena, masa, poreklo):
        self.ime = ime
        self.cena = cena
        self.masa = masa
        self.poreklo = poreklo

class IzdelekL:
    def __init__(self, ime, cena, prostornina, poreklo):
        self.ime = ime
        self.cena = cena
        self.prostornina = prostornina
        self.poreklo = poreklo
'''
class Izdelek:
    def __init__(self, ime, cena, poreklo, dobavitelj="aaa"):
        self.ime = ime
        self.cena = cena
        self.poreklo = poreklo
        self.dobavitelj = dobavitelj
    def to_string(self):
        return "I:{} C:{} Po:{}".format(self.ime, self.cena, self.poreklo)

    def Print(self):
        print self.to_string()

class IzdelekKg(Izdelek):
    def __init__(self, ime, cena, masa, poreklo):
        Izdelek.__init__(self, ime, cena, poreklo)
        self.masa = masa
    def to_string(self):
        return "Ime:{} M:{}".format(self.ime, self.masa)


class IzdelekL(Izdelek):
    def __init__(self, ime, cena, prostornina, poreklo="Slovenija"):
        Izdelek.__init__(self, ime, cena, poreklo)
        self.prostornina = prostornina
    def to_string(self):
        return "{} P:{}".format(Izdelek.to_string(self), self.prostornina)

sir = IzdelekKg(ime="Sir", cena=2.11, masa=0.22, poreklo="Francija")
mleko = IzdelekL(ime="Mleko", cena=3.7, prostornina=1, poreklo="Slovenija")
voda = IzdelekL(ime="Voda", cena=3.7, prostornina=1)


print(sir.to_string())
sir.Print()
print(mleko.to_string())
mleko.Print()
print(voda.to_string())
print(voda.dobavitelj)