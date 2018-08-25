"""
def hi(name):
    print("Hej, ", name)


dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']

for imie in dziewczyny:
    hi(imie)
    print("Kolejna dziewczyna")


for i in range (1, 8):
    print(i)

"""

def check(a, b):
    if a > b:
        print(a, " jest większe od ", b)
    elif a < b:
        print(b, "jest większe od ", a)
    elif a == b:
        print("Obie wartości są równe")

check(1,2)
check(8, 4)
check(8, 8)