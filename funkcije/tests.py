from counting import numbers_sum
from calc import calculator

def testing_numbers_sum():
    assert numbers_sum(2, 3) == 5 # zagotovi da bo to res
    assert numbers_sum(-1, 1) == 0
    assert numbers_sum(0, 0) == 0
    assert numbers_sum(0, 1) == 0
    assert numbers_sum(1, 1.1) == 2
    return "testing_numbers_sum() passed successfully"

def testing_function_calculator():
    assert calculator(3, 4, "*") == 12
    assert calculator(3, 4, "/") == 0
    assert calculator(3.0, 4, "/") == 0.75
    assert calculator("a", "b", "+") == "ab"
    assert calculator("a", 4, "*") == "aaaa"
    return "testing_function_calculator() passed successfully"

print testing_numbers_sum()
print testing_function_calculator()

from ugani_drzavo import izpisi_gl_mesto, izpisi_drzavo, podatki

def test_ugani_drzavo(vhod):
    mesta = vhod.keys()
    for mesto in mesta:
        assert izpisi_gl_mesto(izpisi_drzavo(mesto)) == mesto
    drzave = vhod.values()
    for drzava in drzave:
        assert izpisi_drzavo(izpisi_gl_mesto(drzava)) == drzava

test_ugani_drzavo(podatki)