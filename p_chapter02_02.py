# Chapter02-02
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

class Car():
    """
    Car class
    Author: Gun-code
    Date: 2024.12.18
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self): # 매직 메소드, 클래스를 print()로 출력할 때 사용, 사용자 입장의 출력
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # 매직 메소드, 클래스를 그냥 출력할 때 사용, 객체 자체를 출력, __str__이 없으면 __repr__을 호출
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))



# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # False / company 값이 다르기 때문
print(car1 is car2) # False / 서로 다른 객체이기 때문(주소값이 다름)

# dir & __dict__ 확인
print(dir(car1)) # car1이 가지고 있는 모든 메소드와 변수를 리스트로 출력 / 해당 인스턴스가 갖고 있는 모든 속성(상속 포함)과 메소드 출력
print(dir(car2))

print(car1.__dict__) # 해당 인스턴스가 가지고 있는 속성을 딕셔너리로 출력
print(car2.__dict__)

print('------------------------------------------------------------------------------------------------')

# Doctring
print(Car.__doc__) # 클래스의 주석을 출력

print('------------------------------------------------------------------------------------------------')

# 실행
car1.detail_info()
car2.detail_info() # self를 통해 각 인스턴스의 고유한 값을 출력

print('------------------------------------------------------------------------------------------------')

# 비교
print(car1.__class__, car2.__class__) # 클래스 정보 출력
print(id(car1.__class__), id(car2.__class__)) # 클래스의 주소값이 같음

# 에러
# Car.detail_info() # 클래스 메소드는 인스턴스를 통해서 호출해야함
Car.detail_info(car1) # 클래스에서 직접 호출할 때는 인스턴스를 넣어줘야함
Car.detail_info(car2)

print('------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------')


# 클래스 변수 공유 확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__) # 해당 인스턴스가 가지고 있는 속성을 출력하기 때문에 클래스 변수는 출력되지 않음
print(car2.__dict__)
print(dir(car1)) # 클래스 변수 출력
print(dir(car2))

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))