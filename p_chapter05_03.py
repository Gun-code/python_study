# Chapter05-03
# 일급 함수
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능함

# 클로저(Closure) 사용
def closure_ex1():
    # Free variable 자유 변수
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()

print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print('---------------------------------------------------------------------------------')

# function inspection
print('function inspection >>>',dir(avg_closure1))
print('code >>>', avg_closure1.__code__)
print('closure >>>', avg_closure1.__closure__)
print('closure freevars >>>', avg_closure1.__code__.co_freevars)
print('closure freevars >>>', avg_closure1.__closure__[0].cell_contents)

# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(15)) # 예외
print('---------------------------------------------------------------------------------')
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

