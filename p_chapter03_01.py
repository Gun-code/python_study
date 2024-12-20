# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n))

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n)) # 0이면 false, 0이 아니면 true
print(n * 100, n.__mul__(100)) # 곱하기

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info: {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직 메소드 출력
print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
