# class Person:
#     bag = []

#     def put_bag(self, stuff):
#         self.bag.append(stuff)

# james = Person()
# james.put_bag('책')

# maria = Person()
# maria.put_bag('열쇠')

# print(james.bag)
# print(maria.bag)

# __init__로 만든 속성은 사실 인스턴스 속성이었습니다.
# class속성을 만들려면 함수선언 없이 바로 class안에 속성명 = 값으로 정의하면 됩니다.
# 이렇게 만들어진 클래스 속성은 클래스내 모든 인스턴스가 공유합니다.

# class Person:
#     bag = []

#     def put_bag(self, stuff):
#         Person.bag.append(stuff) # self.bag.append(stuff)

# james = Person()
# james.put_bag('책')

# maria = Person()
# maria.put_bag('열쇠')


# print(james.bag)
# print(maria.bag)
# print(Person.bag)
# print(Person.bag)

# 인스턴스 속성을 호출할때와 마찬가지로 self를 사용해서 호출하니 클래스 속성과 모호해 집니다.
# self 대신 클래스명을 넣어서 작성하면 클래스 속성을 호출한다는 뜻이 좀더 명확해 집니다.

# class Person:
#     def __init__(self):
#         self.bag = []
    
#     def put_bag(self, stuff):
#         self.bag.append(stuff)

# james = Person()
# james.put_bag('책')

# maria = Person()
# maria.put_bag('열쇠')

# print(james.bag)
# print(maria.bag)

# __init__메소드를 통해서 속성을 정의하면 인스턴스 속성이 됩니다.
# 인스턴스 별로 bag 속성이 생성되어 서로 영향을 주지 않습니다.

# class Knight:
#     __item_limit = 10

#     def print_item_limit(self):
#         print(Knight.__item_limit)

# x = Knight()
# x.print_item_limit()

# print(Knight.__item_limit)

# __item_limit는 클래스 내부에서는 호출이 가능하지만 외부에서는 호출할 수 없습니다.
# 이렇게 클래스 속성에도 앞에 __를 붙여주면 비공개 속성으로 생성됩니다.
# 클래스와 메소드에도 """독스트링"""을 통해 독스트링을 남겨둘 수 있습니다.
# 클래스 독스트링의 호출은  클래스.__doc__
# 메소드의 독스트링은 클래스.메소드.__doc__ 또는 인스턴스.메소드.__doc__

# class Calc:
#     @staticmethod
#     def add(a, b):
#         print(a + b)
    
#     @staticmethod
#     def mul(a, b):
#         print(a * b)

# Calc.add(10, 20)
# Calc.mul(10, 20)

# 클래스 내부에서 @staticmethod를 사용 후 메소드를 작성하면 정적메소드가 생성됩니다.
# 정적 메소드는 클래스 외부에서 인스턴스에 클래스를 할당하지 않고 클래스.메소드()로 바로 사용이 가능합니다.
# 정적 메소드는 self를 받지 않으므로 인스턴스 속성에 접근할 수 없습니다.
# 보통 메소드 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들때 사용합니다.

# class Person:
#     count = 0

#     def __init__(self):
#         Person.count += 1

    
#     @classmethod
#     def print_count(cls):
#         print('{}명 생성되었습니다.'.format(cls.count))

# james = Person()
# maria = Person()

# Person.print_count()

# 클래스 내부에 @classmethod를 사용 후 def 메소드(cls, 매개변수1,...., 매개변수n)과 같이 작성하면 클래스 메소드가 생성됩니다.
# 클래스 메소드의 첫번째 매개변수는 현재 클래스가 들어옵니다.
