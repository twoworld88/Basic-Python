# 클래스(class)란 객체(object)를 표현하기 위한 문법입니다.
# 예를 들어 게임을 만든다고 가장 했을 때, 게임에 존재하는 직업(객체)를 만들기 위해 클래스를 사용합니다.
# 이런 직업마다 갖고 있는 기본체력, 마나, 공격력, 마력 등의 기본 속성값이 있고 베기, 찌르기, 말타기 등의 스킬, 행동이 있습니다.
# 직업(객체)의 표현을 위한 클래스에서 기본속성값을 속성(attribute)라 하며, 스킬을 메소드(method)라 부릅니다.

# class person:
#     def greeting(self):
#         print('Hello')
# james = person()
# james.greeting()

# class 클래스이름: 으로 클래스를 선언합니다.
# 내부에 클랙스의 메소드 greeting을 정의합니다.
# james라는 변수에 클래스를 할당합니다. 이 때, 클래스가 할당된 변수를 인스턴스(instance)라고 합니다.
# class는 코드의 개념을 표현할 뿐 직접 사용할 수 없고, 사용하려면 인스턴스를 생성해줘야만 합니다.
# 메소드를 호출하기 위해서는 인스턴스.메소드()의 모양으로 써야하며, 이렇게 인스턴스를 통해 호출되는 메소드를 인스턴스 메소드라 부릅니다.

# a = int(10)
# b = list(range(10))
# c = dict([('a' , 1), ('b' , 2), ('c' , 3)])
# d = 10
# e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# f = {'a' : 1, 'b' : 2, 'c' : 3}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# 지금까지 사용했던 int, list, dict도 사실 클래스입니다.
# 할당된 변수에 type()을 통해서 결과를 출력해보면 class라는 사실을 알 수 있습니다.
# 이는 직접 정수를 할당해도, 직접 리스트를 만들어 할당해도, 직접 딕셔너리를 만들어 할당해도 마찬가지 입니다.
# a, b, c, d, e, f는 모두 객체이며, 인스턴스입니다.
# 그냥 객체만을 이야기할 땐 객체라 표현하지만 클래스와 연관지어 말할 땐 인스턴스라 표현할 뿐입니다.

# class person:
#     def greeting(self):
#         print('hello')
        
#     def hello(self):
#         self.greeting()
        
# james = person()
# james.hello()

# 동일 클래스 내에 존재하는 다른 메소드를 메소드 안에서 호출할때는 self.메소드명()으로 표현해줘여 합니다.
# self.를 넣지 않으면 클래스 밖에 있는 함수를 호출한다는 뜻이 되니 꼭 눈도장을 찍어둡시다.

# def fectorial(n):
#     if not isinstance(n, int) or n < 0:
#         return None
#     if n == 1:
#         return 1
#     return n * fectorial(n - 1)
# print(fectorial(10))

# isinstance(객체, 클래스) 함수는 객체가 클래스에 포함되면 True를 반환하고 포함되지 않으면 False를 반환합니다.

# class person:
#     def __init__(self):
#         self.hello = '안녕하세요'
        
#     def greeting(self):
#         print(self.hello)
# james = person()
# james.greeting()

# __init__(self) 메소드를 사용해주고 그 내부에 self.속성명 = '값'과 같이 작성하여 속성값을 만들어 줄 수 있습니다.
# 속성값은 __init__ 메소드를 사용해야만 만들 수 있습니다.
# __init__ 메소드처럼 __로 둘러쌓여 있는 메소드를  스페셜 메소드 또는 매직 메소드라고 부릅니다.
# 여기서 self란 인스턴스 자신을 뜻한다고 설명하는데 정확히 설명해주는 다른 자료를 참조하는 것이 좋아보인다.

# class person:
#     def __init__(self, name, age, adrress):
#         self.hello = '안녕하세요'
#         self.name = name
#         self.age = age
#         self.adrress = adrress
    
#     def greeting(self):
#         print('{} 저는 {}입니다.'.format(maria.hello, maria.name))
# maria = person('마리아', 20, '서울측별시 서초구 반포동')
# maria.greeting()
# print('이름 : ', maria.name)
# print('나이 : ', maria.age)
# print('주소 : ', maria.adrress)

# __init__(self, a, b, c)와 같이 매개변수를 self뒤에 지정하고, 아래 self.a = 'a'처럼 속성을 정의해줍니다.
# 클래스 안에서 호출할 때는 self.속성명을 사용하지만 클래스 밖에서 호출할때는 인스턴스명.속성명으로 호출하면 됩니다.

# class person_args:
#     def __init__(self, *args):
#         self.name = args[0]
#         self.age = args[1]
#         self.adrress = args[2]
        
# maria = person_args(*['마리아', 20, '서울특별시 서초구 반포동'])
# j = ['제임스', 23, '서울특별시 용산구 이촌동']
# james = person_args(*j)
# print(maria.name)
# print(maria.age)
# print(maria.adrress)
# print(james.name)
# print(james.age)
# print(james.adrress)

# 위치 인수를 사용해서 *를 이용한 언패킹 스킬을 사용할 수 있습니다.

# class person_kwargs:
#     def __init__(self, **kwargs):
#         self.name = kwargs['name']
#         self.age = kwargs['age']
#         self.adrress = kwargs['adrress']

# maria = person_kwargs(**{'name' : '마리아', 'age' : 20, 'adrress' : '서울특별시 서초구 반포동'})
# j = {'name' : '제임스', 'age' : 23, 'adrress' : '서울특별시 용산구 이촌동'}
# james = person_kwargs(**j)
# print(maria.name)
# print(maria.age)
# print(maria.adrress)
# print(james.name)
# print(james.age)
# print(james.adrress)

# 마찬가지로 키워드 인수를 사용해서 **를 이용한 언패킹 스킬을 사용할 수 있습니다.

# class person:
#     pass

# maria = person()
# maria.name = '마리아'
# print(maria.name)
# james = person()
# print(james.name)

# 속성을 추가하지 않은 빈 클래스에서 maria 인스턴스를 정의하고 maria의 name속성을 '마리아'로 속성을 추가하는게 가능합니다.
# 이렇게 추가한 속성은 클래스의 속성이 아니라 해당 인스턴스의 속성임으로 다른 인스턴스에서는 호출되지 않습니다.

# class person:
#     def greeting(self):
#         self.hello = '안녕하세요'
# maria = person()
# # print(maria.hello)

# maria.greeting()
# print(maria.hello)

# __init__메소드가 아닌 다른 메소드에도 속성을 추가할 수 있지만, 이렇게 추가한 속성은 해당 메소드를 호출해야만 생성됩니다.

# class person:
#     __slots__ = ['name', 'age']

# maria = person()
# maria.name = '마리아'
# maria.age = 20
# maria.adrress = '서울특별시 서초구 반포동'

# __slots__ = ['속성명1', .... '속성명n']으로 속성명을 지정해 두면 해당 속성명만 추가할 수 있습니다.

# class person:
#     def __init__(self, name, age, address, wallet):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet
# maria = person('마리아', 20, '서울특별시 서초구 반포동', 10000)
# maria.__wallet -= 10000

# wallet처럼 속성명 앞에 __를 붙이면 비공개 속성이 됩니다.
# 비공개 속성은 클래스 내부에서만 접근이 가능하고 외부에서는 접근할 수 없습니다.
# 비공개 속성에 돈이 들어 있어서 사용하지 못합니다.

# class person:
#     def __init__(self, name, age, address, wallet):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet
        
#     def pay(self, amount):
#         self.__wallet -= amount
#         print('이제 {}원 남았네요'.format(self.__wallet))
        
# maria = person('마리아', 20, '서울특별시 서초구 반포동', 10000)
# maria.pay(3000)

# 지갑에 들어있는 돈을 이제 사용할 수 있게 되었습니다.

# class person:
#     def __init__(self, name, age, address, wallet):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet
        
#     def pay(self, amount):
#         if amount > self.__wallet:
#             print('돈이 모자라네...')
#             return
#         self.__wallet -= amount
        
# maria = person('마리아', 20, '서울특별시 서초구 반포동', 10000)
# maria.pay(3000)

# 남은 돈을 반환하는 모양보다는 돈이 있으면 사용돼고 없으면 부족해서 불가하다고 표현하는 식을 많이 사용합니다.



# 메소드 앞에도 __를 붙여주면 비공개 메소드가 돼서 클래스 밖에서 호출할 수 없게된다.