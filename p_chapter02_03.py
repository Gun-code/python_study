# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

# 클래스 선언

class Car():
    """
    Car class
    Author: Gun-code
    Date: 2024.12.18
    Description: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        self._details = details


    def __str__(self): # 매직 메소드, 클래스를 print()로 출력할 때 사용, 사용자 입장의 출력
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # 매직 메소드, 클래스를 그냥 출력할 때 사용, 객체 자체를 출력, __str__이 없으면 __repr__을 호출
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # 매개변수 Self : 인스턴스화 된 객체 자기 자신을 의미
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> Company: {}, Price: {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> Company: {}, Price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    # 매개변수 cls: 클래스 자체를 의미
    @classmethod # 데코레이터 자바의 annotation과 비슷한 역할
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')

    # Static Method
    # 매개변수를 받지 않음, 그만큼 유연하게 사용할 수 있음.
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'


# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격정보 (인스턴스에 직접적으로 접근하는건 좋지 않다. 캡슐화 위반)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print('------------------------------------------------------------------------------------------------')

# 가격 인상(클래스 메소드 미사용)
# Car.price_per_raise = 1.4 # 클래스 변수를 직접 접근하여 변경하는 것은 좋지 않다.
Car.raise_price(1.6) # 클래스 메소드를 통해 접근하여 변경하는 것이 좋다.

print(car1.get_price_culc())
print(car2.get_price_culc())
print('------------------------------------------------------------------------------------------------')

# Static Method 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print('------------------------------------------------------------------------------------------------')

# Static Method 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))


