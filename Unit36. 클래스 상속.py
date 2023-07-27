# class Person:
#     def greeting(self):
#         print('안녕하세요.')
        
# class Student(Person):
#     def study(self):
#         print('공부하기')

# james = Student() 
# james.greeting()
# james.study()

# 새로운 클래스를 만들때 class 클래스명(상속해준 클래스명): 으로 만들면 해당 클래스를 상속받은 클래스를 만들게 됩니다.
# 상속이란 동물 -> 척추동물 -> 포유류 처럼 척추동물은 동물의 특성을 갖고 있지만 척추동물만의 특성을 갖고 있고 포유류는 동물과 척추동물의 특성을 모두 갖고 있지만 또한 포유류만의 특성을 갖고 있는 것과 같습니다.
# 상속받은 클래스(파생클래스, 자식클래스, 서브클래스라고 함.)는 상속해준 클래스(기반클래스, 부모클래스, 슈퍼클래스라고 함.)의 속성과 메소드를 갖고 있으면서 본인만의 속성과 메소드를 갖습니다.
# 상속은 클래스끼리 같은 종류이며 유관할 때 사용합니다. 영어적 표현으로 is-a관계라고 합니다.

# class Person:
#     def greeting(slef):
#         print('안녕하세요.')

# class PersonList:
#     def __init__(self):
#         self.person_list = []
        
#     def append_person(self, person):
#         self.person_list.append(person)

# Person은 사람을 입력하면 인사를 하는 클래스고 PersonList는 사람을 입력하면 저장해서 보관하는 클래스입니다.
# 이렇듯 유관하지만 종류가 다른 클래스를 포함관계의 클래스라고 합니다.
# 라는 설명인데 다른 책에서 찾아서 다시 공부해보자....

# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     def __init__(self):
#         print('Student __init__')
#         self.school = '파이썬 코드 도장'
        
# james = Student()
# print(james.school)
# print(james.hello)

# james를 Student의 인스턴스로 만들어주고 Student의 속성과 Person의 속성을 차례대로 호출하면 Student의 속성만 출력하고 그냥 사용되던 메소드와 다르게 Person의 속성 호출에서 에러가 납니다.
# james.hello를 출력하는 과정에서 먼저 속성이 인스턴트가 속한 클래스 내부에 hello메소드가 있는지 확인하고 있으면 출력합니다.
# 없으면 기반클래스의 __init__를 호출했는지 확인합니다. 호출했으면 내부에 유무를 확인해서 있으면 출력 없으면 에러, 호출인 안됐어도 에러가 발생합니다.

# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     def __init__(self):
#         print('Student __init__')
#         super().__init__() # 이를 기반클래스를 초기화 해준다고 합니다.
#         self.school = '파이썬 코드 도장'
        
# james = Student()
# print(james.school)
# print(james.hello)

# james.school 속성의 출력을 위해 __init__이 메소드를 호출합니다. 'Student __init__'출력하고 super().__init__()를 통해 기반클래스의 __init__메소드를 호출합니다.
# 'Person __init__'출력하고 속성들이 호출되어 와서 순서대로 school의 속성, hello의 속성 순으로 출력됩니다.

# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         print('Student __init__')
#         self.school = '파이썬 코드 도장'
        
# james = Student()
# print(james.school)
# print(james.hello)

# 순서를 한 줄 바꿔주면 __init__의 호출을 알리는 'Person __init__'이 먼저 출력되고 다음으로 'Student __init__'출력된 후 똑같은 순서로 속성들이 출력됩니다.
# super(파생클래스명, self).__init__()로 작성하면 현재클래스가 어떤 클래스인지 표기해줄 수 있다. 물론 기능은 변동이 없다.

# class Person:
#     def __init__(self):
#         print('person __init__')
#         self.hello = '안녕하세요.'

# class Student(Person):
#     pass

# james = Student()
# print(james.hello)

# 이처럼 파생클래스에서 __init__를 별도로 정의하지 않으면 기반클래스를 초기화 해줄 필요가 없습니다.

# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):
#         print('안녕하세여. 저는 파이썬 코딩 도장 학생입니다.')
        
# james = Student()
# james.greeting()

# greeting 메소드가 기반클래스에 존재하지만 파생클래스에서 다시 greeting을 정의하고 호출하니 파생클래스에서 정의한 메소드가 호출되었습니다.
# 이렇게 기반클래스에 있는 메소드를 파생클래스에서 재정의 하는 스킬을 메소드 오버라이딩이라고 합니다.
# 파생의 greeting이 필요해서 재정의 했지만 기반에 있는 greeting도 같이 사용해야 할 경우 어찌할까? 다시 다른 이름으로 또 정의하면 필요할 때 마다 정의해야함으로 불필요한 일과 코드가 늘어난다.

# class Person:
#     def greeting(self):
#         print('안녕하세요.')

# class Student(Person):
#     def greeting(self):
#         super().greeting()
#         print('안녕하세여. 저는 파이썬 코딩 도장 학생입니다.')
        
# james = Student()
# james.greeting()

# 이렇게 super().호출할 기반 클래스 메소드()를 해주면 해당 메소드를 호출해온다.
# super()의 활용으로 불필요한 재정의작업과 코드사용을 줄일 수 있다.

# class Person:
#     def greeting(self):
#         print('안녕하세요.')
    
# class University:
#     def manage_credit(self):
#         print('학점 관리')

# class Undergraduate(Person, University):
#     def study(self):
#         print('공부하기')

# james = Undergraduate()
# james.greeting()
# james.manage_credit()
# james.study()

# 상속을 하나에서만 받는게 아니라 2개의 기반클래스로부터 상속을 받을 수도 있다.
# class 파생클래스명(기반클래스명1, ..., 기반클래스명n):과 같이 만들면 된다.

# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')
        
# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')

# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')
        
# class D(B, C):
#     pass

# x = D()
# x.greeting()

# D는 B, C에게 상속받았지만 그 B, C가 A에게 상속받았습니다. 즉, D는 A, B, C 모두에게 상속받았습니다.
# 문제는 D가 상속받은 A, B, C 모두 greeting 메소드가 있다는 겁니다. 이럴 경우 호출하는 순서가 때마다 다르면 문제가 생길 수 있습니다.
# 이런 상속을 다이아몬드 상속이라 부릅니다.

# print(D.mro())

# 클래스명.mro() 메소드를 사용하면 해당 클래스의 상속관계 중 탐색을 하는 순서를 반환해줍니다.
# 클래스 D는 B -> C -> A순으로 탐색하므로 B 클래스에 있는 greeting()메소드가 반환됨을 알 수있습니다.
# mro결과 마지막에 나오는 object클래스는 모든 클래스의 조상인 기반클래스라고 보시면 됩니다.
# 모든 클래스선언엔 사실 (object)가 생략된 것입니다.

# from abc import * # abc모듈의 모든 클래스와 메소드를 가져옵니다. 이렇게 하지 않을 경우 가져온 클래스나 메소드 사용시 코드를 더 길게 써야합니다. 이는 추후 다시 배웁니다.

# class StudentBase(metaclass = ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
    
#     @abstractmethod
#     def go_to_school(self):
#         pass

# class Student(StudentBase):
#     def study(self):
#         print('공부하기')

# james = Student()
# james.study()

# 추상클래스는 abc(abstract base class)모듈을 불러와야만 사용이 가능합니다.
# class 추상클래스명(metaclass = ABCMeta): 로 생성합니다.
# 위와 같이 추상클래스에 @abstractmethod가 위에 붙어 있는 메소드가 2개지만 파생클래스에서 그 중 1개만 재정의했습니다.
# 이럴 경우 에러가 납니다.

from abc import *

class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()