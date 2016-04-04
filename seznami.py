cars = ["renault", "audi", "bmw", "peugeot", "seat"]
print cars
print cars.index("bmw")
print len(cars)
cars.remove("audi")
print cars
print len(cars)

cars1 = ["renault", "audi", "bmw", "audi", "peugeot", "seat"]
print cars1.count("audi")
cars1.remove("audi")
print cars1.count("audi")

if "audi" in cars1:
    print("Audi is in the cars list")
else:
    print("Audi is NOT in the cars list")