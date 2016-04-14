class Izdelek:
    def __init__(self, ime_izd, cena_izd, masa_izd, poreklo_izd):
        self.ime = ime_izd
        self.cena = cena_izd
        self.masa = masa_izd
        self.poreklo = poreklo_izd

    def cena_na_kg(self):
        cena_kg = self.cena / self.masa
        return cena_kg

    ime = "ime izdelka"
    cena = 0.00
    masa = 0.0
    poreklo = "drzava"

sir = Izdelek(ime_izd="Sir", cena_izd=2.11, masa_izd=0.22, poreklo_izd="Francija")

print(sir.ime)
print(sir.cena_na_kg())

