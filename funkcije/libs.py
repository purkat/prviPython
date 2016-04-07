from random import randint

print randint(0, 10)
print randint(0, 10)
print randint(0, 10)
print randint(0, 10)

from datetime import datetime

print datetime.now()

print "=" * 15

from datetime import datetime
import time

current_time = datetime.now()  # shrani trenutni cas v spremenljivko

print current_time

time.sleep(1)  # pavza za 1 sekund

print current_time
current_time = datetime.now()  # shrani trenutni cas v spremenljivko
print current_time

print "=" * 15

def izpisi_cas_vsako_sekundo(i):
    while i > 0:
        print "{} trenutni cas {}".format(i, datetime.now())
        time.sleep(1)
        i -= 1

izpisi_cas_vsako_sekundo(5)