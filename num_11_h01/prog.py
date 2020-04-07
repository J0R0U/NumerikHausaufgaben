# -*- coding: utf-8 -*-

import math

class exercise(object):
    @staticmethod
    def number():
        raise NotImplementedError()
        
    @staticmethod
    def execute():
        raise NotImplementedError()

class exercise_one(exercise):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def method_one(self):
        return -self.p + math.sqrt(self.p ** 2 + self.q)
    
    def method_two(self):
        x1 = -self.p - math.sqrt(self.p ** 2 + self.q)
        return - self.q / x1
    
    @staticmethod
    def number():
        return 1
    
    @staticmethod
    def execute():
        ps = [10 ** 2, 10 ** 4, 10 ** 6, 10 **7, 10 ** 8]
        qs = [1]
        
        for p in ps:
            for q in qs:
                print('p: ', p, ', q: ', q)
                tmp = exercise_one(p, q)
                print('Method one: ', tmp.method_one())
                print('Method two: ', tmp.method_two())
                
class exercise_two(exercise):
    def __init__(self, n, x):
        self.n = n
        self.x = x
    
    def method_one(self):
        ret = 0
        for k in range(self.n + 1):
            ret += self.x ** k / math.factorial(k)
        return ret
        
    def method_two(self):
        ret = 0
        for k in range(self.n + 1):
            ret += self.x ** (self.n - k) / math.factorial(self.n - k)
        return ret
    
    @staticmethod
    def number():
        return 2
    
    @staticmethod
    def execute():
        xs = [1, 2, 5]
        ns = [1, 5, 10, 100]
        
        for x in xs:
            for n in ns:
                print('n: ', n, ', x: ', x)
                tmp = exercise_two(n, x)
                print('Method one: ', tmp.method_one())
                print('Method two: ', tmp.method_two())
                
class exercise_three(exercise):
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
    
    def method_rectangle_one(self):
        h = (self.b - self.a) / self.n
        sum = 0
        for i in range(0, self.n):
            sum += self.f(self.a + i * h)
        return h * sum
    
    def method_rectangle_two(self):
        h = (self.b - self.a) / self.n
        sum = 0
        for i in range(1, self.n + 1):
            sum += self.f(self.a + i * h)
        return h * sum
            
        
    def method_trapezoid(self):
        h = (self.b - self.a) / self.n
        sum = 0
        for i in range(1, self.n):
            sum += self.f(self.a + i * h)
        return h / 2 * (self.f(self.a) + 2 * sum + self.f(self.b))
    
    @staticmethod
    def function_one(x):
        return 1 / x ** 2
    
    @staticmethod
    def function_two(x):
        return math.log(x)
    
    @staticmethod
    def number():
        return 3
    
    @staticmethod
    def execute():
        ns = [128,256,512,1024]
        for n in ns:
            print('f: 1/x**2, a: 1/10, b: 10, n: ', n)
            tmp = exercise_three(exercise_three.function_one, 1/10, 10, n);
            print('Rectangle (one): ', tmp.method_rectangle_one())
            print('Rectangle (two): ', tmp.method_rectangle_two())
            print('Trapezoid: ', tmp.method_trapezoid())
            
        for n in ns:
            print('f: ln(x), a: 1, b: 2, n: ', n)
            tmp = exercise_three(exercise_three.function_two, 1, 2, n);
            print('Rectangle (one): ', tmp.method_rectangle_one())
            print('Rectangle (two): ', tmp.method_rectangle_two())
            print('Trapezoid: ', tmp.method_trapezoid())
    
class exercise_four(exercise):
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        
    def method_trapezoid(self):
        h = (self.b - self.a) / self.n
 
        vec = map(lambda i : self.a + i * h, range(self.n + 1))
        vec = list(map(lambda x: self.f(x), vec))
       
        return h / 2 * (sum(vec) * 2 - vec[0] - vec[-1])
        
    @staticmethod
    def function(x):
        return math.log(x)
    
    @staticmethod
    def number():
        return 4
    
    @staticmethod
    def execute():
        ns = [128,256,512,1024]
        for n in ns:
            print('f: 1/x**2, a: 1, b: 2, n: ', n)
            tmp = exercise_four(exercise_four.function, 1, 2, n);
            print('Trapezoid: ', tmp.method_trapezoid())
            
class exercise_five(exercise):
    def __init__(self, x0, x, n):
        self.x0 = x0
        self.y0 = math.sqrt(x0);
        self.x = x
        self.n = n

    def calculate_sqrt_one(self):
        return self.__calculate_sqrt_one_rek(self.n)
    
    def __calculate_sqrt_one_a(self, k):
        if (k == 0):
            return self.y0
        else:
            return (3/(2 * k) - 1) * (self.x / self.x0 - 1) * self.__calculate_sqrt_one_a(k-1)
        
    
    def __calculate_sqrt_one_rek(self, k):
        if (k == 0):
            return self.y0
        else:
            return self.__calculate_sqrt_one_rek(k - 1) + self.__calculate_sqrt_one_a(k);
        
    def calculate_sqrt_heron(self):
        return self.__calculate_sqrt_heron_rek(self.n)
        
    def __calculate_sqrt_heron_rek(self, k):
        if (k == 0):
            return self.y0
        else:
            y_1 = self.__calculate_sqrt_heron_rek(k - 1)
            return 1 / 2 * (y_1 + self.x / y_1);
        
    @staticmethod
    def number():
        return 5
    
    @staticmethod
    def execute():
        x0s = [1, 4]
        
        # It needs 9 steps for the error of calculate_sqrt_one to be smaller than 0,005
        ns = [9, 18]
        
        for x0 in x0s:
            for n in ns:
                print('x: 2, x0: ', x0, ', n: ', n)
                tmp = exercise_five(x0, 2, n);
                print('error abs(sqrt(2) - sqrt_one(2)): ', abs(math.sqrt(2) - tmp.calculate_sqrt_one()))
                print('error abs(sqrt(2) - sqrt_heron(2)): ', abs(math.sqrt(2) - tmp.calculate_sqrt_heron()))
        
    
        
                
def main():
    exercises = [exercise_one, exercise_two, exercise_three, exercise_four, exercise_five]
    
    for exercise in exercises:
        print()
        print('--- Exercise ', exercise.number(), ' ---')
        exercise.execute();        
        print('--- Exercise ', exercise.number(), ' ---')
        print()

main()