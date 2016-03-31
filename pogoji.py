x = 5
y = 30
z = 5

# ce je x manjsi od y ...
if x < y:
    print("x is smaller than y")
else:
    print("y is smaller than x")

# ce je z enak x-u ...
if z == x:
    print("z is the same as x")
else:
    print("z is NOT the same as x")

# ce je x vecji od 10 ali pa ce je y vecji od 10 ...
if (x > 10) or (y > 10):
    print("either x or y is bigger than 10")

print "==============="

# ce je x vecji od 10 in obenem tudi y vecji od 10 ...
if x > 10 and y > 10:
    print("both x and y are bigger than 10")
elif (x < 10) and (y > 10):
    print "aaaa"
else:
    print("at least one of x and y is NOT bigger than 10")