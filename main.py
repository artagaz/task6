# 1
class BigBell:
    def __init__(self):
        self.ding = 'ding'

    def sound(self):
        print(self.ding)
        if self.ding == 'ding':
            self.ding = 'dong'
        else:
            self.ding = 'ding'


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()


# 2
class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def result(self):
        if self.left == self.right:
            return '='
        elif self.left > self.right:
            return 'L'
        elif self.right > self.left:
            return 'R'


balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())


# 3
class Selector:
    def __init__(self, lst):
        self.lst = lst

    def get_odds(self):
        return [num for num in self.lst if num % 2 == 1]

    def get_evens(self):
        return [num for num in self.lst if num % 2 == 0]


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))


# 4
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other


p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print('Equal True')
else:
    print('Equal False')

if p1 != p2:
    print('Not equal True')
else:
    print('Not equal False')


# 5
class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[-1 - item]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])


# 6
class SparseArray:
    def __init__(self):
        self.data = {}

    def __getitem__(self, item):
        return self.data.get(item, 0)

    def __setitem__(self, key, value):
        self.data[key] = value


arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))


# 9
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


tr = EquilateralTriangle(5)
print(tr.perimeter())


# 10
class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        summ = 0
        for i in range(N + 1):
            summ += self.transform(i)
        return summ


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


a = CubeSummator()
print(a.sum(5))


# 12
class A:
    def __init__(self):
        pass

    def __str__(self):
        return 'A.__str__method'

    def hello(self):
        print('Hello')


class B:
    def __init__(self):
        pass

    def __str__(self):
        return 'B.__str__method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    def __init__(self):
        super().__init__()


class D(B, A):
    def __init__(self):
        super().__init__()


c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)


# 15
class Digits:
    def __init__(self, lst):
        self.lst = [int(x) for x in lst.split()]

    def defaul(self, func):
        self.lst = list(map(func, self.lst))

    def print(self):
        print(*self.lst)

    def make_negative(self):
        self.defaul(lambda x: -abs(x))

    def square(self):
        self.defaul(lambda x: x ** 2)

    def strange_command(self):
        self.defaul(lambda x: x + 1 if x % 5 == 0 else x)


digits = Digits(input())
rep = int(input())
for i in range(rep):
    command = input()
    if command == 'make_negative':
        digits.make_negative()
    elif command == 'square':
        digits.square()
    elif command == 'strange_command':
        digits.strange_command()
digits.print()
