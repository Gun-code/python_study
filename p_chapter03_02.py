# Chapter03-02
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 예제2 일반적인 계산기
# 벡터 (Vector) 좌표
# (5,2) + (4,3) = (9,5) 더하기
# (10,3) * 5 = (50,15) 곱하기
# Max((5,10)) = 10 최대값

class Vector(object):
    def __init__(self, *args): # *args: 가변인자 -> 튜플로 받음
        '''Create a vector, example: v = Vector(5,10)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        '''Return the vector multiplication of self and y'''
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        '''Return the vector boolean'''
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()


# 매직메소드 출력
print(Vector.__init__.__doc__) # 독스트링 출력
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)
print(Vector.__bool__.__doc__)

print(v1, v2, v3)

print(v1.__add__(v2))
print(v1 + v2)

print(v1.__mul__(10))
print(v1 * 10)

print(bool(v1), bool(v2))
print(bool(v3))

print(v1.__repr__() + v2.__repr__())
