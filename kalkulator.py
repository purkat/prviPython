a_raw = raw_input("A: ")
b_raw = raw_input("B: ")

operacija = raw_input("Operacija: ")

if (a_raw.find(".") == -1):
    a = int(a_raw)
else:
    a = float(a_raw)

if (b_raw.find(".") == -1):
    b = int(b_raw)
else:
    b = float(b_raw)

if (operacija == "+"):
    rezultat = a + b
elif (operacija == "-"):
    rezultat = a - b
elif (operacija == "*"):
    rezultat = a * b
elif (operacija == "/"):
    rezultat = a / b
else:
    print "Te operacije ne poznam"

if 'rezultat' in locals(): # ali spremenljivka rezultat obstaja
    print "Rezultat a ("\
          + str(a) + ") " + operacija\
          + " b (" + str(b) + ") = " + str(rezultat)