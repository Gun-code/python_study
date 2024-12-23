# Chapter04-03
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Key에 Value를 저장하는 구조
# 파이썬 dict 해시 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수 -> 해시 주소 -> Key에 대한 Value 참조

# Dict 구조
print(__builtins__.__dict__) # 파이썬에서 기본적으로 사용하는 내장함수들을 볼 수 있다.

# Hash 값 확인 (고유한 값) -> 불변형 데이터만 사용 가능
t1 = (10, 20, (30, 40, 50)) # 튜플은 변경 불가능한 객체이기 때문에 해시값을 가질 수 있다.
t2 = (10, 20, [30, 40, 50]) # 리스트는 변경 가능한 객체이기 때문에 해시값을 가질 수 없다.

print(hash(t1))
# print(hash(t2)) # TypeError: unhashable type: 'list' -> 리스트(가변형 데이터)는 해시값을 가질 수 없다.

# Dict Setdefault 예제 / tuple에서 dict 만들 때 공식문서에서 추천하는 방법
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5')) # 이중 튜플을 받았을 때
new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1) # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2) # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# 주의사항
new_dict3 = {k: v for k, v in source}
print(new_dict3) # {'k1': 'val2', 'k2': 'val5'} -> 키가 중복되면 마지막 값으로 덮어씌워진다. (중복 키 처리 주의) -> 딕셔너리 컴프리헨션을 사용할 때 주의해야 한다.
