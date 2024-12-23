# Chapter03-03
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value


# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt # math 모듈에서 sqrt 함수를 가져옴 sqrt는 제곱근을 구하는 함수(루트)

line_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) # 두 점 사이의 거리를 구하는 공식 sqrt((x2-x1)^2 + (y2-y1)^2)

print(line_leng1)

# 네임드 튜플 사용
from collections import namedtuple # collections 모듈에서 namedtuple 함수를 가져옴

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y') # Point라는 이름의 네임드 튜플을 선언하고 x, y라는 필드를 가지게 함

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3)
# print(pt3[0]) # 인덱스로 접근 가능
# print(pt3.y) # 필드명으로 접근 가능
# print(pt4)

line_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2) # 네임드 튜플을 사용하여 두 점 사이의 거리를 구함

print(line_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', 'x y') # 띄어쓰기로 구분
Point2 = namedtuple('Point', ['x', 'y']) # 리스트로 선언
Point3 = namedtuple('Point', 'x, y') # 문자열로 선언
Point4 = namedtuple('Point', 'x y x class', rename=True) # Key값으로 예약어나 중복되는 필드명을 사용할 때 rename=True 옵션 설정 / Default=False

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35) # 키워드 인자로 네임드 튜플 생성
p2 = Point2(20, 40) # 위치 인자로 네임드 튜플 생성
p3 = Point3(45, y=20) # 위치 인자와 키워드 인자 혼용
p4 = Point4(10, 20, 30, 40) # rename=True로 선언한 네임드 튜플
p5 = Point3(**temp_dict) # 딕셔너리를 언패킹하여 네임드 튜플 생성 언패킹 시 튜플은 (*), 딕셔너리는 (**)
print('---------------------------------------------------------------------------------------------------------------------------------------------')

print(p1)
print(p2)
print(p3)
# rename 옵션
print(p4) # rename=True로 선언한 네임드 튜플은 필드명이 중복되어도 자동으로 이름을 변경하여 생성됨
print(p5) # 딕셔너리를 언패킹하여 네임드 튜플을 생성할 수 있음
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# 사용
print(p1[0] + p2[1]) # 인덱스로 접근 가능
print(p1.x + p2.y) # 네임드 튜플을 사용하여 각 필드에 접근 가능

#unpacking
a, b = p3 # 언패킹 가능

print(a, b) # 언패킹하여 각 필드에 접근 가능
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 네임드 튜플 객체 생성
p4 = Point1._make(temp) # _make() 메소드는 리스트를 네임드 튜플로 변환해줌

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields) # _fields 메소드를 사용하여 네임드 튜플의 필드명을 확인할 수 있음

# _asdict() : OrderedDict 반환 / 딕셔너리는 정렬 순서가 없지만 OrderedDict는 정렬 순서가 있음
print(p1._asdict()) # _asdict() 메소드를 사용하여 네임드 튜플을 OrderedDict로 반환할 수 있음
print(p4._asdict())
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)] # 1부터 20까지의 숫자를 문자열로 변환하여 리스트에 저장
ranks = 'A B C D'.split() # 'A B C D'를 split() 메소드로 리스트로 변환

print(numbers)
print(ranks)
print('---------------------------------------------------------------------------------------------------------------------------------------------')

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers] # 리스트 컴프리헨션을 사용하여 네임드 튜플을 생성

print(len(students)) # 총 학생 수 출력
print(students) # 학생 리스트 출력

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [int(n)
                            for n in range(1, 21)]]

print(len(students2)) # 총 학생 수 출력
print(students2) # 학생 리스트 출력


for s in students2:
    if s.rank == 'C' and s.number <= 15:
        print(s) # 학생 리스트 출력