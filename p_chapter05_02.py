# Chapter05-02
# 파이썬 심화
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) # b가 정의되지 않았기 때문에 에러가 발생한다.

# Ex2
b = 20
def func_v2(a):
    print(a)
    print(b)

func_v1(10) # b가 정의되어 있기 때문에 정상적으로 출력된다.

# Ex3
c = 30
# def func_v3(a):
#     print(a)
#     print(c)
#     c = 40 # c가 함수 내에서 정의되어 있기 때문에 전역 변수 c가 아닌 지역 변수 c로 인식기 때문에 에러가 발생한다.

def func_v3(a):
    global c # 전역 변수 c를 사용하겠다고 선언
    print(a)
    print(c)
    c = 40

print('>>', c) # 전역 변수 c 출력 -> 30으로 선언되어 있다.
func_v3(10) # c가 정의되어 있기 때문에 정상적으로 출력된다.
print('>>>', c) # 전역 변수 c 출력 -> 40으로 변경되어 있다.
print('------------------------------------------------------------------------------------------------------------------------------------')

# Closure(클로저) 사용 이유
# 클로저는 변수의 상태를 save하고 있다.
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 고급 주제
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine: 단일 프로그램에서도 동일한 효과) 프로그래밍에 강점을 갖는다.

a = 100
print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

averager_cls = Averager()

print(dir(averager_cls))

# 누적 / 클로저 사용하여 누적되는 값을 저장한다.
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))

