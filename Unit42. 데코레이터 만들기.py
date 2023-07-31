# class calc:
#     @staticmethod # @가 앞에 붙어서 함구를 장식해주며 기능을 부가해주는 것을 데코레이터라고 함
#     de add(a, b):
#         print(a + b)

# 데코레이터는 위에 @staticmethod처럼 함수 앞에 붙어서 함수를 장식해주면서 기능을 부가해주는 것을 말합니다.

# def hello():
#     print('hello 함수 시작')
#     print('hello')
#     print('hello 함수 끝')
 
# def world():
#     print('world 함수 시작')
#     print('world')
#     print('world 함수 끝')
 
# hello()
# world()

# 위와 같이 함수가 시작과 끝을 표시하기 위해서 print함수를 사용해서 시작과 끝을 출력해 줄 수 있습니다.
# 허나, 그럴 필요가 있는 함수의 개수가 무수히 많아지면 매우 번거로워지게 됩니다.

# def trace(func):                             # 호출할 함수를 매개변수로 받음
#     def wrapper():                           # 호출할 함수를 감싸는 함수
#         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         func()                               # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝')
#     return wrapper                           # wrapper 함수 반환
 
# def hello():
#     print('hello')
 
# def world():
#     print('world')
 
# trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
# trace_hello()                 # 반환된 함수를 호출
# trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
# trace_world()                 # 반환된 함수를 호출

# 함수를 사용해서도 데코레이터를 만들 수 있습니다. 위 코드는 함수로 함수의 시작과 끝을 알리는 메세지를 출력하는 데코레이터를 작성한 것입니다.
# 먼저 출력하는 함수를 변수로 받는 tacce함수(데코레이터)를 만들어 줍니다. 프로그래밍에서는 함수의 실행 상황을 추적할 때 trace라는 용어를 사용합니다.
# 그 다음 trace함수 내부에 호출할 함수를 감싸줄 wrapper함수를 만들어줍니다. 이름은 wrapper가 아니어도 무관합니다.
# 함수의 시작을 출력하면서 앞에 __name__메소드를 사용해서 해당 함수의 이름을 출력하도록 합니다. 변수인 함수를 넣어주고 끝을 시작과 동일하게 __name__메소드를 사용해서 작성합니다.
# wrapper함수에서 나와서 trace함수가 wrapper함수의 결과를 반환하도록 합니다.
# hello, world함수를 작성해주고 trace함수에 hello, world를 변수로 주고 변수에 할당해준 다음 함수를 호출해주면 아까 처럼 print로 일일이 작성하지 않아도 시작과 끝을 출력합니다.

# def trace(func):                             # 호출할 함수를 매개변수로 받음
#     def wrapper():
#         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         func()                               # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝')
#     return wrapper                           # wrapper 함수 반환
 
# @trace    # @데코레이터
# def hello():
#     print('hello')
 
# @trace    # @데코레이터
# def world():
#     print('world')
    
# hello()    # 함수를 그대로 호출
# world()    # 함수를 그대로 호출
    
# 데코레이터를 작성 후 함수를 변수로 넣어서 변수에 할당한 후 함수를 출력하지 않고 @데코리이터명을 함수 위에 붙여주고 함수를 출력하면 똑같은 효과가 나타납니다.

# def decorator1(func):
#     def wrapper():
#         func()
#         print('decorator1')
#     return wrapper
 
# def decorator2(func):
#     def wrapper():
#         print('decorator2')
#         func()
#     return wrapper
 
# # 데코레이터를 여러 개 지정
# @decorator1
# @decorator2
# def hello():
#     print('hello')
 
# hello()

# 데코레이터를 여러개 붙일때는 위에 여러개를 써주면 중복적용 됩니다.
# 단, 복수의 데코리이터의 실행 순서는 위에서부터 아래 순서로 실행됩니다.

# def trace(func):          # 호출할 함수를 매개변수로 받음
#     def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
#         r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
#         print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
#         return r          # func의 반환값을 반환
#     return wrapper        # wrapper 함수 반환
 
# @trace              # @데코레이터
# def add(a, b):      # 매개변수는 두 개
#     return a + b    # 매개변수 두 개를 더해서 반환
 
# print(add(10, 20))

# 인위 코드는 인수가 존재하는 데코레이터를 작성한 것입니다.
# trace는 마찬가지로 함수를 변수로 받고 내부에 wrapper함수는 꾸며줄 함수와 동일한 변수를 받아줍니다.
# 여기선 변수값과 그 결과값이 어떤 함수에 들어가서 나오는지를 표기해주는 데코리이터 임으로 변수 r = func(a, b)로 작성하여 함수값을 변수에 할당해줍니다.
# print와 format을 사용해서 함수명(변수1,변수2) 결과값변수로 작성하여 주고 그 다음 함수의 결과값을 한번더 반환하고 종료합니다.
# 실행해보면 어떤 함수에 어떤 변수를 넣어주면 어떤값이 나오는지 출력됩니다.

# def trace(func):                     # 호출할 함수를 매개변수로 받음
#     def wrapper(*args, **kwargs):    # 가변 인수 함수로 만듦
#         r = func(*args, **kwargs)    # func에 args, kwargs를 언패킹하여 넣어줌
#         print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
#                                      # 매개변수와 반환값 출력
#         return r                     # func의 반환값을 반환
#     return wrapper                   # wrapper 함수 반환
 
# @trace                   # @데코레이터
# def get_max(*args):      # 위치 인수를 사용하는 가변 인수 함수
#     return max(args)

# @trace                   # @데코레이터
# def get_min(**kwargs):   # 키워드 인수를 사용하는 가변 인수 함수
#     return min(kwargs.values())
 
# print(get_max(10, 20))
# print(get_min(x=10, y=20, z=30))

# args와 kwargs를 사용해서 가변인수나 키워드가변인수를 사용해 데코레이터를 만들 수 있습니다.
# 이때 args는 튜플을 kwargs는 딕셔너리를 인수로 넣어주게 되기때문에 변수앞에 *과 **오 언패킹을 해줘야합니다.

# def trace(func):
#     def wrapper(self, a, b):   # 호출할 함수가 인스턴스 메소드이므로 첫 번째 매개변수는 self로 지정
#         r = func(self, a, b)   # self와 매개변수를 그대로 넣어줌
#         print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))   # 매개변수와 반환값 출력
#         return r               # func의 반환값을 반환
#     return wrapper
 
# class Calc:
#     @trace
#     def add(self, a, b):    # add는 인스턴스 메소드
#         return a + b
 
# c = Calc()
# print(c.add(10, 20))

# 일반 함수가 아닌 메소드에서 데코레이터를 만들때는 변수에 꼭 self를 먼저 넣어줘야합니다.

# def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
#     def real_decorator(func):    # 호출할 함수를 매개변수로 받음
#         def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정
#             r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
#             if r % x == 0:       # func의 반환값이 x의 배수인지 확인
#                 print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
#             else:
#                 print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
#             return r             # func의 반환값을 반환
#         return wrapper           # wrapper 함수 반환
#     return real_decorator        # real_decorator 함수 반환
 
# @is_multiple(3)     # @데코레이터(인수)
# def add(a, b):
#     return a + b
 
# print(add(10, 20))
# print(add(2, 5))

# 이번에는 데코리에터(변수)와 같이 변수가 있는 데코레이터를 작성한 코드입니다.
# 먼저 데코레이터명(변수)와 같이 변수를 받는 함수(데코레이터)를 만들어줍니다.
# 그 안에 변수가 없는 데코레이터와 마찬가지로 함수를 변수로 받는 함수를 만들고 그 내부에 wrraper함수를 만들어서 받아들이는 함수와 같은 변수를 넣어줍니다.
# 위 코드에서는 함수의 값과 그 함수가 데코레이터 변수의 배수인지 아닌지를 출력하는 데코레이터임으로 우선 함수값을 변수로 할당합니다.
# if문으로 할당된 함수의 결과값을 받은 변수를 데코레이터가 받은 변수로 나눠서 나머지가 0인 경우와 아닌 경우를 출력해주고 마지막으로 함수 반환값을 한 번 더 넣어주고 함수를 종료합니다.
# 내부 데코레이터에서는 wrapper의 값을 반환하고 외부 데코레이터에서는 내부 데코레이터의 값을 반환합니다.
# 함수를 데코레이터에 변수를 넣어서 위에 달아주고 함수를 실행해주면 그 결과값이 나옵니다.
# 변수가 있는 데코레이터도 여러개 지정할 수 있습니다.
# 단, 이런식으로 작성된 코드로 데코레이터를 여러개 변수를 넣어서 실행하면 2번째 이후의 데코레이터 값은 제대로된 함수값을 불러오지 못하는 경우가 발생합니다.

# import functools
 
# def is_multiple(x):
#     def real_decorator(func):
#         @functools.wraps(func)    # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
#         def wrapper(a, b):
#             r = func(a, b)
#             if r % x == 0:
#                 print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
#             else:
#                 print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
#             return r
#         return wrapper
#     return real_decorator
 
# @is_multiple(3)
# @is_multiple(7)
# def add(a, b):
#     return a + b
 
# add(10, 20)

# functools모듈에서 @functools.wraps()를 사용해서 wrapper위에 넣어주면 중복해서 데코레이터를 사용할 경우에 함수명이 잘못표기되는 것을 방지합니다. 

# class Trace:
#     def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
#         self.func = func         # 호출할 함수를 속성 func에 저장
 
#     def __call__(self):
#         print(self.func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         self.func()                               # 속성 func에 저장된 함수를 호출
#         print(self.func.__name__, '함수 끝')
 
# @Trace    # @데코레이터
# def hello():
#     print('hello')
 
# hello()    # 함수를 그대로 호출

# 클래스로 데코레이터를 작성할 떄는 __init__메소드를 만들고 셀프와 함수를 변수로 받습니다.
# 변수로 받은 함수를 slef.func = 함수와 같이 속성에 저장해줍니다.
# __call__ 메소드를 만들어서 self를 변수로 받고 내부에 동일하게 작성을 하돼 앞에 self.를 붙여야 합니다.

# class Trace:
#     def __init__(self, func):
#         self.func = func
 
#     def __call__(self):
#         print(self.func.__name__, '함수 시작')
#         self.func()
#         print(self.func.__name__, '함수 끝')
 
# def hello():
#     print('hello')

# trace_hello = Trace(hello)
# trace_hello()

# 클래스로 만들어준 데코레이터는 @를 함수 앞에 붙이지 않고 변수에 클래스(함수)를 할당해주고 해당 변수를 함수로 호출해주면 똑같은 값을 반환합니다.

# class Trace:
#     def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
#         self.func = func         # 호출할 함수를 속성 func에 저장
 
#     def __call__(self, *args, **kwargs):    # 호출할 함수의 매개변수를 처리
#         r = self.func(*args, **kwargs) # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
#         print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
#                                             # 매개변수와 반환값 출력
#         return r                            # self.func의 반환값을 반환
 
# @Trace    # @데코레이터
# def add(a, b):
#     return a + b
 
# print(add(10, 20))
# print(add(a=10, b=20))

# 이번에는 매개변수를 받아서 처리하는 클래스로 만든 데코레이터입니다.
# __init__에서 self와 함수를 받아주고 self.함수 = 함수로 속성에 저장합니다.
# __call__메소드에서 self와 변수를 받아줍니다.

# class IsMultiple:
#     def __init__(self, x):         # 데코레이터가 사용할 매개변수를 초깃값으로 받음
#         self.x = x                 # 매개변수를 속성 x에 저장
 
#     def __call__(self, func):      # 호출할 함수를 매개변수로 받음
#         def wrapper(a, b):         # 호출할 함수의 매개변수와 똑같이 지정(가변 인수로 작성해도 됨)
#             r = func(a, b)         # func를 호출하고 반환값을 변수에 저장
#             if r % self.x == 0:    # func의 반환값이 self.x의 배수인지 확인
#                 print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
#             else:
#                 print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
#             return r               # func의 반환값을 반환
#         return wrapper             # wrapper 함수 반환
 
# @IsMultiple(3)    # 데코레이터(인수)
# def add(a, b):
#     return a + b
 
# print(add(10, 20))
# print(add(2, 5))

# 이번에는 변수가 있는 데코레이터를 클래스로 구현한 코드입니다.
# 클래스에서 __init__메소드를 만들고 self와 변수를 받아줍니다. self.변수 = 변수로 속성에 저장합니다.
# __call__메소드를 만들고 self, 함수를 변수로 받습니다. 그 내부에 wrapper함수를 만들고 변수를 받습니다.
# 구현할 데코레이터 기능을 만들고 warrper함수를 종료한 뒤 __call__메소드에서 warrper의 값을 반환합니다.

