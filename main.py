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


# 7
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = []
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coeff1 + coeff2)
        return Polynomial(new_coeffs)


poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))


# 8
class Queue:
    def __init__(self, *args):
        self.items = list(args)

    def append(self, *values):
        self.items.extend(values)

    def copy(self):
        return Queue(*self.items)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def extend(self, queue):
        self.items.extend(queue.items)

    def next(self):
        return Queue(*self.items[1:]) if len(self.items) > 1 else Queue()

    def __add__(self, other):
        return Queue(*(self.items + other.items))

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.items == other.items

    def __rshift__(self, n):
        return Queue(*self.items[n:]) if n < len(self.items) else Queue()

    def __str__(self):
        return "[" + " -> ".join(map(str, self.items)) + "]" if self.items else "[]"

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q1, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep="\n")
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)


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


# 14
class MailServer:
    def __init__(self, name):
        self.name = name
        self.mailbox = {}

    def receive_mail(self, user):
        return self.mailbox.pop(user, [])

    def send_mail(self, user, message):
        if user not in self.mailbox:
            self.mailbox[user] = []
        self.mailbox[user].append(message)

    def __str__(self):
        return self.name


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        mails = self.server.receive_mail(self.user)
        if mails:
            print(f"Письма для {self.user} на сервере {self.server}:")
            for mail in mails:
                print(f"- {mail}")
        else:
            print(f"Нет новых писем для {self.user}.")

    def send_mail(self, server, user, message):
        if server not in MailSystem.servers:
            print(f"Ошибка: Невозможно отправить письмо на сервер {server}. Он не зарегистрирован.")
            return
        server.send_mail(user, message)
        print(f"Письмо отправлено пользователю {user} на сервере {server}.")


class MailSystem:
    servers = []

    @classmethod
    def register_server(cls, server):
        cls.servers.append(server)

    @classmethod
    def list_servers(cls):
        return [str(server) for server in cls.servers]


if __name__ == "__main__":
    server1 = MailServer("MailServer1")
    server2 = MailServer("MailServer2")
    MailSystem.register_server(server1)
    MailSystem.register_server(server2)
    client1 = MailClient(server1, "user1@example.com")
    client2 = MailClient(server2, "user2@example.com")
    client1.send_mail(server1, "user2@example.com", "Привет от 1")
    client2.send_mail(server1, "user1@example.com", "Привет от 2")
    client1.receive_mail()
    client2.receive_mail()


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
