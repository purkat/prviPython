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