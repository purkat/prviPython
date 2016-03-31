a_raw = raw_input("A: ")
b_raw = raw_input("B: ")

operacija = raw_input("Operacija: ")

a = int(a_raw)
b = int(b_raw)

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
    print "Rezultat a " + operacija + " b = " + str(rezultat)