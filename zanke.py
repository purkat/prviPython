reprezentanca = ["Dragic", "Lorbek", "Zupan", "Blazic", "Prepelic", "Klobucar", "Slokar"]
print reprezentanca

for igralec in reprezentanca:
    #print "element: " + igralec
    if igralec == "Slokar" or igralec == "Zupan":
        print igralec + ", center"
    else:
        print igralec + ", branilec"

print ("==============")

repka = {"Dragic": "branilec", "Slokar": "center", "Zupan": "center", "Blazic": "branilec"}

for igralec in repka:
    print igralec + ", " + repka[igralec]
    if igralec == "Zupan":
        break

i = int(raw_input("Stevilo: "))
while i > 3:
    print i
    if i == 7:
        break
    i -= 1 # i = (i - 1)
