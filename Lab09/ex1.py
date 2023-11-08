print("""
+-------------------------------------------+
|    Program Name: Fraction Program         |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab09 (Exercise 1)             |
+-------------------------------------------+
""")

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator

        if denominator == 0:
            raise Exception("Denominator cannot be 0")
        else:
            self.denominator = denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def convert_fraction_to_float(self):
        return self.numerator / self.denominator

    def __truediv__(self, other):
        # print(self.numerator)
        # print(self.denominator)
        # print(other.numerator)
        # print(other.denominator)
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return numerator / denominator

    def invert_fraction(self):
        return Fraction(self.denominator, self.numerator)


def main():
    f1 = Fraction(1, 3)  # self
    f2 = Fraction(3, 5)  # other

    print(f"First object instance: {f1}")
    print(f"Second object instance: {f2} \n")

    print("----------------- Part I ----------------")
    f1_float_result = f1.convert_fraction_to_float()
    f2_float_result = f2.convert_fraction_to_float()
    print(f"Float conversion of first object: {f1_float_result}")
    print(f"Float conversion of second object: {f2_float_result} \n")

    print("---------------- Part II ----------------")
    truediv = f1 / f2
    print(f"True division: {truediv} \n")

    print("--------------- Part III ----------------")
    f1_inverted_fraction = f1.invert_fraction()
    f2_inverted_fraction = f2.invert_fraction()
    print(f"Inverted first object: {f1_inverted_fraction}")
    print(f"Inverted second object: {f2_inverted_fraction}")


if __name__ == '__main__':
    main()
