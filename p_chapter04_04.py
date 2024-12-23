# Chapter04-04
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict
from types import MappingProxyType # 불변 dict 생성 / 수정 불가능

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d) # 수정 불가능
print(d, id(d), type(d)) # dict는 가변 데이터형이기 때문에 hash값이 없다.
print(d_frozen, id(d_frozen), type(d_frozen))

# 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'
print(d)
print('------------------------------------------------------------------------------------------------------------------------------------')

# Set 선언
s1 = {'apple', 'orange', 'apple', 'orange', 'kiwi'} # 중복 허용 X
s2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi']) # 리스트로 선언
s3 = {3} # 숫자로 선언
s4 = set() # 빈 집합 선언은 set()으로 해야한다. {}는 dict로 인식한다.
s5 = frozenset({'apple', 'orange', 'apple', 'orange', 'kiwi'}) # 수정 불가능

s1.add('melon')

# 추가 불가
# s5.add('melon') # frozenset은 수정 불가능

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))
print('------------------------------------------------------------------------------------------------------------------------------------')

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print(dis('{10}')) # set / 3단계의 과정을 거쳐서 set으로 변환된다.
print(dis('set([10])')) # set / 5단계의 과정을 거쳐서 set으로 변환된다.
print('------------------------------------------------------------------------------------------------------------------------------------')

# 지능형 집합(Comprehending Set)
from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)}) # chr() : 아스키 코드를 문자로 변환