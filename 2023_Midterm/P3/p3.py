class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
    
    def sum(self):
        a = self.real_1 + self.real_2
        b = self.imaginary_1 + self.imaginary_2
        return a, b
    def sub(self):
        a = self.real_1 - self.real_2
        b = self.imaginary_1 - self.imaginary_2
        return a, b


#두개의 복소수 클래스의 저장
a = MyComplex(2, -3, -5, 4)

#연산 각각의 결과
result_sum_a, result_sum_b = a.sum()
result_sub_a, result_sub_b = a.sub()

#결과 출력
print("{} + {}i".format(result_sum_a, result_sum_b))
print("{} + {}i".format(result_sub_a, result_sub_b))
