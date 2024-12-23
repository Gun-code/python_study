# Chapter04-02
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급
from Material.p_chapter04_02 import f_list

# Tuple Advanced
# Unpacking

# b, a = a, b / a에는 b를, b에는 a를 넣어라

print(divmod(100, 9)) # divmod는 몫과 나머지를 튜플로 반환한다. (11, 1)
print(divmod(*(100, 9))) # *를 사용하여 튜플을 unpacking하여 divmod함수에 전달. (11, 1) / 동적으로 생성된 iterable을 함수의 인자로 전달할 때 사용한다.
print(*(divmod(100, 9))) # *를 사용하여 divmod 결과값(튜플)을 unpacking. 11 1 / *를 사용하면 튜플을 풀어서 출력한다.

x, y, *rest = range(10) # *를 사용하여 나머지를 rest에 넣는다. / *rest가 없으면 에러가 발생한다.
print(x, y, rest) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]

x, y, *rest = range(2)
print(x, y, rest) # 0 1 [] / *rest가 없으면 에러가 발생한다.

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest) # 1 2 [3, 4, 5]

print('-------------------------------------------------------------------------------------------------------------------------------------')

# Mutable(가변) vs Immutable(불변)

t = (15, 20, 25) # 튜플은 컨테이너 / 불변이다.
l = [15, 20, 25] # 리스트는 컨테이너 / 가변이다.

print(t, id(t)) # (15, 20, 25) 140707366366080
print(l, id(l)) # [15, 20, 25] 140707366366976

t = t * 2
l = l * 2

print(t, id(t)) # (15, 20, 25, 15, 20, 25) 140707366366080 / 새로운 객체가 생성된다.
print(l, id(l)) # [15, 20, 25, 15, 20, 25] 140707366366976 / 새로운 객체가 생성된다.

t *= 2
l *= 2

print(t, id(t)) # (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 140707366366080 / 새로운 객체를 생성한다.
print(l, id(l)) # [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 140707366366976 / 기존 객체를 사용한다.
print('-------------------------------------------------------------------------------------------------------------------------------------')

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 / 원본 데이터 변경 X
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list)) # ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry'] / 정렬
print('sorted - ', sorted(f_list, reverse=True)) # ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple'] / 역순으로 정렬
print('sorted - ', sorted(f_list, key=len)) # ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry'] / 글자 길이를 기준으로 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1])) # ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry'] / 마지막 글자를 기준으로 정렬
print('sortedR - ', sorted(f_list, key=lambda x: x[-1], reverse=True)) # ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya'] / 마지막 글자를 기준으로 역순으로 정렬
print('sorted - ', f_list)
print('-------------------------------------------------------------------------------------------------------------------------------------')

# sort : 정렬 후 객체 직접 변경 / 원본 데이터 변경 O
# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list) # sort -  None ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry'] / 원본 데이터가 변경된다.
print('check  - ', f_list) # check  -  ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry'] / 원본 데이터가 변경된다.
print('sort - ', f_list.sort(reverse=True), f_list) # sort -  None ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple'] / 역순으로 정렬
print('sort - ', f_list.sort(key=len), f_list) # sort -  None ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry'] / 글자 길이를 기준으로 정렬
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list) # sort -  None ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry'] / 마지막 글자를 기준으로 정렬
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list) # sort -  None ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya'] / 마지막 글자를 기준으로 역순으로 정렬
print('check  - ', f_list) # check  -  ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya'] / 원본 데이터가 변경된다.

# List vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)