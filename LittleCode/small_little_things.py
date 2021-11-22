def fizzbuzz():
    for val in range(1, 101):
        if val % 3 == 0 and val % 5 == 0:
            print(f"FizzBuzz")
        elif val % 3 == 0:
            print("Fizz")
        elif val % 5 == 0:
            print("Buzz")
        else:
            print(val)
    return None

# fizzbuzz()

def even_steven(lst):
    for strng in lst:
        if len(strng) % 2 == 0 and strng[0] == "s":
            print("EvenSteven")
        elif len(strng) % 2 == 0:
            print("Even")
        elif strng[0] == "s":
            print("Steven")
        else:
            print(strng)
    return None


# test_lst = ["some", "hello", "sorry", "remi"]
# even_steven(test_lst)

'''
try:
    print("A")
    x = 1/0
    print("B")
except ZeroDivisionError:
    print("C")
finally:
    print("D")
'''

class Polynomial:
    def __init__(self, coeffs_lst):
        assert len(coeffs_lst) != 0, "Must have len greater than 0"
        for val in coeffs_lst:
            assert isinstance(val, int) or isinstance(val, float), "Must be a numeric type"
        self.coeffs = coeffs_lst

    def evaluate(self, x):
        total = 0
        for power, coeff in enumerate(self.coeffs):
            total += coeff * (x ** power)
        return total

test_obj = Polynomial([1, 2, 3])
print(test_obj.evaluate(5))

try:
    test_obj = Polynomial([1, 2, 3, 2, 'A'])
except AssertionError:
    print("faild assertion")
