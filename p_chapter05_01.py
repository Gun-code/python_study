# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화 
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능(return)
from symtable import Function


# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
# 함수를 객체 취급한다는 증명
print(type(factorial), type(A))
print(dir(factorial)) # 함수 이지만 __lt__, __repr__ 등의 메소드를 가지고 있어 객체로 취급하는 것을 볼 수 있다.
print(sorted(set(dir(factorial)) - set(dir(A)))) # 함수만 가지고 있는 메소드를 확인할 수 있다.
print(factorial.__name__) # 함수의 이름을 확인할 수 있다.
print(factorial.__code__) # 함수의 바이트 코드를 확인할 수 있다.
print('------------------------------------------------------------------------------------------------------------------------------------')

#변수 할당
var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11)))) # map() : 함수와 반복 가능한 자료형을 입력으로 받아 함수를 적용한 결과를 반환한다.
print('------------------------------------------------------------------------------------------------------------------------------------')

#함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)
# map(), filter(), reduce() 등
# es6의 map(), filter(), reduce()와 비슷하다.

# map() 함수
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6))))) # filter() : 함수와 반복 가능한 자료형을 입력으로 받아 함수의 결과가 참인 것만 반환한다.
print([var_func(i) for i in range(1, 6) if i % 2]) # 리스트 컴프리헨션을 사용하여 홀수만 출력한다.

# reduce() 함수
from functools import reduce
from operator import add

print(sum(range(1, 11))) # sum() : 모든 요소의 합을 반환한다.
print(reduce(add, range(1, 11))) # add() : 두 인자를 더하는 함수

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 익명함수 보다 함수 사용
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1, 11))) # lambda : 함수를 한 줄로 간결하게 만들어 사용할 수 있다.
print('------------------------------------------------------------------------------------------------------------------------------------')

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인 .doc 속성으로 확인 가능하며 __call__ 속성이 있는지 확인하면 된다.

print(var_func.__dir__())
print(callable(str), callable(A), callable(var_func), callable(factorial), callable(3.14), callable(100)) # true true true true false false
# callable() : 호출 가능한지 확인하며 해당 객체에 __call__ 속성이 있어야 호출 가능하다.

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10)) # mul() : 두 인자를 곱하는 함수

# 인수 고정
five = partial(mul, 5) # mul() 함수의 첫 번째 인자를 5로 고정한다.
# 5 * ? 형태를 객체로 만들어준다.
print(five(10)) # 5 * 10
print(five(100)) # 5 * 100

# 고정 추가
six = partial(five, 6)
print(six()) # 5 * 6
# print(six(10)) # 5 * 6 * 10 / 인수가 넘쳐 맞지 않아 오류가 발생한다.
print([five(i) for i in range(1, 11)]) # 5 * 1 ~ 5 * 10 구구단 출력
print(list(map(five, range(1, 11)))) # 5 * 1 ~ 5 * 10 구구단 출력

