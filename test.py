my_name = "Matej"
print(my_name)
print("My name is " + my_name)
print("My name is %s" % my_name)

name = "Matej"
#name = raw_input("Please enter your name: ")
print("Howdy, %s" % name)

if name == "Matt":
    print("Hello Matt")
    kakoSi = raw_input("Kako si? ")
    print("Vidim da si %s" % kakoSi)
else:
    print("Hello %s" % name)
print("Bye")


num1 = 25
num2 = 38
num3 = 25

print(num1 == num2)
print(num1 == num3)
print(num1 > num3)
print(num1 < num3)
print(num1 >= num3)
print(num1 != num2)



num = 1

while num < 10:
    print(num)
    num = num + 1


my_answer = "yes"

while my_answer == "yes":
    my_answer = raw_input("Do you still want to be in the while loop? (yes/no) ")
    if my_answer != "no":
        break


# komentar

"""
To je vecvrsticni komentar
 aaa
 asdasd
 sadsdsad
 asdasd
 a
"""
