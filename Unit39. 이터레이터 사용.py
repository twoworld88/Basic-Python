# 요소가 여러개 들어 있으면서 한번에 하나씩 꺼낼 수 있는 객체를 이터레이터 또는 반복자라고 한다.
# 이런 에터레이터에는 문자열, 리스트, 딕셔너리, 세트, range 등이 있다.
# for문을 사용할때 range(10)은 0~9까지 숫자를 만들고 하나씩 꺼낸다고 했는데 사실 0~9까지 숫자를 만들고 꺼내는 것이 아니라 0~9를 꺼낼 수 있는 이터레이터 하나를 만들거 하나씩 꺼내온 것이다.

# print(dir('iterable'))
# print(dir([1, 2, 3]))
# print(dir({'a' : 1, 'b' : 2, 'C' : 3}))
# print(dir(range(10)))
# print(dir({1, 2, 3}))

# dir함수를 사용하면 해당 객체에 메소드를 확인할 수 있습니다.
# 문자열, 리스트, 딕셔너리, range, 세트는 모두 __iter__메소드를 보유하고 있습니다
# __iter__메소드를 사용하고 변수에 저장해주면 그 요소갯수만큼 반복되는 이터레이터가 만들어 집니다.

# it = [1, 2, 3].__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# __iter__로 이터레이터를 만들고 __next__메소드를 사용하면 요소를 하나씩 반환합니다.
# 요소보다 많은 __next__메소드를 사용하면 Stopiteration 예외가 발생됩니다.

# for i in range(3):
#     print(i)

# 위 for 구문의 작동을 살펴보면 먼저 반복이 가능한 객체 range(3)이 for문으로 인해 __iter__메소드를 호출하여 이터레이터를 만들어 냅니다.
# 생성된 이터레이터를 이용해서 for문으로 인해 __next__가 호출되어 하나씩 값을 꺼내옵니다.
# 반복될때 마다 반환된 값이 i에 할당되어 출력되고 이 과정은 StopIteration 예외가 발생할때 까지 반복됩니다.
# __iter__메소드를 갖고 있는 반복가능한 객체들을 이터레이터 프로토콜을 지원하는 객체라고 합니다.
# 여기서 말하는 반복가능한 객체란 시퀀스 객체와 같아 보입니다. 하지만 극명한 차이를 갖고 있습니다.
# 시퀀스 객체는 반복이 가능하면서 순서가 정해져 있어야 만합니다.
# 하지만 딕셔너리나 세트는 반복은 가능하지만 순서가 없는 객체이기 때문에 시퀀스 객체에 속하지 않습니다.

# class Counter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop

#     def __iter__(self): # 이미 만들어져 있는 반복가능한 객체가 아니므로 __iter__를 호출해주지 않습니다.
#         return self     # 때문에 __iter__메소드를 만들어주고 객체 자체를 반환해줍니다.
    
#     def __next__(self):                 # 반복해주기 위해 __next__메소드를 만들어 줍니다.
#         if self.current < self.stop:    # self.stop보다 self.current가 작을 때까지만 반복합니다.
#             r = self.current            # r이란 변수에 self.current를 할당해줍니다.
#             self.current += 1           # self.current가 반복때마다 1씩 증가하게 해줍니다.
#             return r                    # r을 반환해줍니다.
#         else:
#             raise StopIteration         # self.current와 self.stop이 같아지면 예외가 발생하며 종료됩니다.
        
# for i in Counter(3):
#     print(i, end=' ')

# 위와 같이 이터레이터를 만들 수 있습니다.
# 이는 클래스사용에 대한 이해도가 높아야 이해가 가능할 듯 하니 다음에 복습 및 다른 책을 이용해서 클래스 사용을 심화한 뒤 이해해 보도록 합시다.

# a, b, c = Counter(3)
# print(a, b, c)
# a, b, c, d, e = Counter(5)
# print(a, b, c, d, e)

# 이터레이터는 언패킹이 가능합니다.
# 변수가 이터레이터에서 반복하는 갯수와 동일해야 언패킹이 됩니다.

# _, b = range(2)
# print(_, b)
# a, _, c, d = range(4)
# print(a, _, c, d)

# 위 _, b는 a, b와 같고 a, _, c, d는 a, b, c, d와 같습니다.
# _가 변수의 역할을 할 수 있기 때문입니다,
# 그럼에도 _를 사용하는 이유는 프로그래밍계의 관례적으로 _로 표현한 순서의 반환값을 사용하지 않고 무시하자는 뜻입니다.

class Counter:
    def __init__(self, stop):
        self.stop = stop
    
    def __getitem__(self, index):
        if index < self.stop:
            return index
        
        else:
            raise IndexError

print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
print(list(Counter(3)))
print(tuple(Counter(3)))
for i in Counter(3):
    print(i, end=' ')

# __getitem__을 사용해서 이터레이터를 만들어 봤습니다. 복습을 하며 다시 익혀봐야할듯 합니다.....

# it = iter(range(3))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# iter(반복 가능한 객체)를 사용하면 반복 가능한 객체의 __iter__메소드를 호출해서 객체의 이터레이터를 반환해줍니다.
# next(이터레이터가 할당된 객체)를 사용하면 객체에 할당된 이터레이터에서 하나씩 요소를 꺼내옵니다.

# import random
# it = iter(lambda : random.randint(0, 5), 2)
# print(next(it))

# iter(호출가능한객체, 반복을 끝낼 값)으로 작성해주면 반복을 끝낼 지점을 지정할 수 있습니다.
# 이때는 반복 가능한 객체가 아니라 호출이 가능한 객체를 넣어줍니다. 차이는 좀 더 공부하며 알아가야할듯 합니다...
# 이때 반복을 끝낼 값을 sentinel이라고 하는데 반복을 지켜보다 특정 값이 나오면 중단시키기 때문에 감시병이라는 명칭이 붙었습니다.

# import random
# for i in iter(lambda : random.randint(0, 5), 2):
#         print(i, end=' ')

# for반복문에 넣어서 반복시킬 수 있습니다.
# 이때 숫자가 무작위로 생성돼서 2가 언제나올지 모르기 때문에 for문이 호출해서 꺼내오는 요소의 개수도 항상 달라집니다.

# import random

# while True:
#     i = random.randint(0, 5)
#     if i == 2:
#         break
#     print(i, end=' ')

# 위 for문을 while문으로 바꾸면 위와 같은 코드가 됩니다.
# for문을 사용해야 매번 숫자가 2인지 검사하는 과정을 거치지 않으므로 더욱 간결하고 가벼워집니다.

# it = iter(range(3))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))

# next(반복 가능한 객체, 기본값)과 같이 작성해주면 반복 가능한 객체의 요소를 하나씩 꺼내오고 요소를 다 꺼내고 나면 기본값을 반환합니다.
# 기본값을 반환하기 때문에 예외가 발생하지 않습니다.
