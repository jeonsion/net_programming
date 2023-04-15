# class MyComplex:
#     def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
#         self.real_1 = real_1
#         self.imaginary_1 = imaginary_1
#         self.real_2 = real_2
#         self.imaginary_2 = imaginary_2
    
#     def multiply(self, other):
#         result_real = self.real_1 * other.real_1 - self.imaginary_1 * other.imaginary_1 \
#                       + self.real_2 * other.real_2 - self.imaginary_2 * other.imaginary_2
#         result_imaginary = self.real_1 * other.imaginary_1 + self.imaginary_1 * other.real_1 \
#                            + self.real_2 * other.imaginary_2 + self.imaginary_2 * other.real_2
#         return MyComplex(result_real, result_imaginary, 0, 0)

# a = MyComplex(3, -4, 0, 0)
# b = MyComplex(-5, 2, 0, 0)

# c = a.multiply(b)

# print(c.real_1, "+", c.imaginary_1, "i")


class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
    
    def multiply(self, other):
        result_real = self.real_1 * other.real_1 - self.imaginary_1 * other.imaginary_1                     
        result_imaginary = self.real_1 * other.imaginary_1 + self.imaginary_1 * other.real_1
        return MyComplex(result_real, result_imaginary, 0, 0)

a = MyComplex(3, -4, 0, 0)
b = MyComplex(-5, 2, 0, 0)

c = a.multiply(b)

print(c.real_1, "+", c.imaginary_1, "i")

