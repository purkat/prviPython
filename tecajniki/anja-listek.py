seznam = []

dodam_izdelek = "Da"
while dodam_izdelek == "Da":
   izdelek = raw_input("Napisite izdelek, ki ga zelite dodati: ")
   seznam.append(izdelek)
   dodam_izdelek = raw_input("Ali zelite dodati se kak izdelek v seznam?: ")
"""
   odg2 = raw_input("Ali zelite dodati se kak izdelek v seznam?: ")
   if odg2 == "Da":
          odg1 = raw_input ("Napisite izdelek, ki ga zelite dodati: ")
          seznam.append(odg1)
          odg2 = raw_input ("Ali zelite dodati se kak izdelek v seznam?: ")
   else:
       print ("Vas nakup vsebuje: "), seznam
       print ("Hvala za vas nakup!")
"""
print ("Vas nakup vsebuje: "), seznam
print ("Hvala za vas nakup!")