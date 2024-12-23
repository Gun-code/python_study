# Chapter04-01
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!' # 문자열, 불변 / 문자열은 인덱스 순서대로 접근이 가능하다
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s)) # ord() : 문자의 유니코드 값을 반환하는 함수

print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars] # 위의 for문을 한 줄로 표현
print(code_list2)
print('---------------------------------------------------------------------------------------------------------------------------------------------')


# Comprehending Lists + Map 함수, Filter 함수 : 코드가 간결해지지만 가독성이 떨어질 수 있음 / 일반 리스트보다 지능형 리스트가 미세하게 더 빠르다
code_list3 = [ord(s) for s in chars if ord(s) > 40] # ord(s) > 40 조건을 추가하여 필터링
code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # map과 filter를 사용하여 코드를 간결하게 작성

# 출력
print(code_list3)
print(code_list4)
print('---------------------------------------------------------------------------------------------------------------------------------------------')

print([chr(s) for s in code_list1]) # chr() : 유니코드 값을 문자로 반환하는 함수
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# Generator 생성
import array # flat한 자료형, 같은 자료형만 저장 가능하며, 가변 자료형이다.
# a = [1,2,3,4,5,6,7,........,1000] # 리스트는 메모리를 많이 차지하므로, 제너레이터를 사용하여 메모리를 절약할 수 있다

# Generator: 다음에 반환 할 값을 생성하는 함수 / 한 번에 모든 값을 반환하지 않고, 한 번에 하나의 값만 반환(메모리 유지 X)
tuple_g = (ord(s) for s in chars) # 리스트 대신 ()를 사용하여 제너레이터를 생성
array_g = array.array('I', (ord(s) for s in chars)) # array 모듈을 사용하여 제너레이터를 생성

print(type(tuple_g)) # 제너레이터 객체의 타입 출력
print(next(tuple_g)) # 제너레이터 객체 출력
print(next(tuple_g))
print('---------------------------------------------------------------------------------------------------------------------------------------------')

print(type(array_g)) # array 객체의 타입 출력
print(array_g) # array 객체 출력
print(array_g.tolist()) # array 객체를 리스트로 변환하여 출력
print(array_g[0]) # array 객체의 인덱스 0 출력
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21))) # 제너레이터 객체 출력

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)): # 제너레이터 객체를 사용하여 반복문을 실행
    print(s)
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)] # 리스트 컴프리헨션을 사용하여 5x5 리스트 생성
                                        # 리스트 컴프리헨션을 사용하면 각 행이 별도의 리스트로 생성됨
marks2 = [['~'] * 3 ] * 4 # 리스트 컴프리헨션을 사용하지 않고 4x3 리스트 생성
                            # 리스트 컴프리헨션을 사용하지 않으면 모든 행이 같은 리스트를 참조함

print(marks1) # 5x5 리스트 출력
print(marks2) # 4x3 리스트 출력
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# 수정
marks1[0][1] = 'X' # marks1 리스트의 0행 1열을 'X'로 변경
marks2[0][1] = 'X' # marks2 리스트의 0행 1열을 'X'로 변경

print(marks1) # 변경된 marks1 리스트 출력 / marks1 리스트는 0행 1열만 변경됨
print(marks2) # 변경된 marks2 리스트 출력 / marks2 리스트는 0행 1열만 변경했지만, 모든 행의 1열이 변경됨

# 증명
print([id(i) for i in marks1]) # marks1 리스트의 각 행의 id 출력 / marks1 리스트의 각 행은 별도의 리스트를 참조함
print([id(i) for i in marks2]) # marks2 리스트의 각 행의 id 출력 / marks2 리스트의 각 행은 같은 리스트를 참조함