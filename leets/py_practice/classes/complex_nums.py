import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        x = self.real + no.real
        y = self.imaginary + no.imaginary
        return Complex(x, y)

    def __sub__(self, no):
        x = self.real - no.real
        y = self.imaginary - no.imaginary
        return Complex(x, y)

    def __mul__(self, no):
        x = (self.real * no.real) - (self.imaginary * no.imaginary)
        y = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(x, y)

    def __truediv__(self, no):
        det = Complex(no.real, -1*no.imaginary)
        numerator = self*det
        denominator = (no*det).real
        x = numerator.real/denominator
        y = numerator.imaginary/denominator
        return Complex(x, y)

    def mod(self):
        det = Complex(self.real, -1*self.imaginary)
        mult = (det*self).real
        rounded = round(math.sqrt(mult), 2)
        return Complex(rounded, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
