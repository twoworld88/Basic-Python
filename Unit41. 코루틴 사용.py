# def add(a, b):
#     c = a + b
#     print(c)
#     print('add 함수')

# def calc():
#     add(1, 2)
#     print('calc 함수')

# print(calc())

# calc함수가 실행되면 그 과정에서 add함수가 실행되는 구조입니다.
# 이런 구조에서 calc함수의 작동과정을 메인 루틴, add함수의 작동과정을 서브 루틴이라고 합니다.
# 서브 루틴은 메인 루틴에 종속적이며, 메인 루틴의 함수를 실행하는 과정에 실행됐다가 종료되면서 루틴 자체가 사라집니다.

# def number_coroutine():
#     while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
#         x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
#         print(x)
 
# co = number_coroutine()
# next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행), co.send(None)을 넣어줘도 실행된다.(코루틴객체.send(None))
 
# co.send(1)    # 코루틴에 숫자 1을 보냄
# co.send(2)    # 코루틴에 숫자 2을 보냄
# co.send(3)    # 코루틴에 숫자 3을 보냄

# x = (yield) 와 같이 yield에 괄호를 씌워서 변수에 할당해주면 값을 밖으로 내주는게 아니라 밖에서 받아옵니다.
# 값을 받아오게 하려면 객체.send(값)을 작성하면 (yield)가 값을 가져갑니다.
# next(co)로 함수를 최초 호출하면 무한루프 함수이기 때문에 계속 작동됩니다.
# co.send(1) ~ co.send(3)이 실행되는 과정에서도 서브루틴인 while문은 계속 작동중이며, 메인 루틴에서 보내는 값이 있을때마다 가져와서 실행하는 것입니다.
# 이렇게 메인 루틴의 작동을 위해서 실행되지만 종료되지 않고 계속해서 대기하며 메인 루틴과 상호작용하도록 만들어진 객체를 코루틴객체라고 합니다.
# 코루틴이란 cooperative routine을 의미하는데 서로 협력하는 루틴이라는 뜻입니다.

# def sum_coroutine():
#     total = 0
#     while True:
#         x = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
#         total += x
 
# co = sum_coroutine()
# print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
 
# print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
# print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
# print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

# 변수1 = (yeild 변수2)와 같이 작성하면 해당 밖에서 값을 가져와서 대입하고 반환된 값을 밖으로 보내줍니다.
# 위 코드에서는 next(co)로 코루틴을 실행하면서 최초값으로 지정된 total의 0이 밨으로 반환되어 나옵니다.
# co.send(1)에서 1을 보내고 0 + 1 = 1을 반환 받습니다.
# co.send(2)에서 2를 보내고 1 + 2 = 3을 반환 받습니다.
# co.send(3)에서 3을 보내고 3 + 3 = 6을 반환 받습니다.
# 코루틴에서는 next는 실행시키는 용도로 사용하고 send는 코드를 실행하고 값을 보내야할 때 사용합니다.
# 제네레이터는 next함수로 호출하고 next함수를 반복적으로 호출하여 값을 얻어냅니다.
# 코루틴은 next함수로 호출하여 시작만 한 뒤 send로 값을 얻어냅니다.

# def number_coroutine():
#     while True:
#         x = (yield)
#         print(x * 2, end=' ')
 
# co = number_coroutine()
# next(co)
 
# for i in range(20):
#     co.send(i)
 
# co.close()    # 코루틴 종료

# 코루틴객체.close() 메소드를 사용해서 코루틴을 종료할 수 있습니다.

# def number_coroutine():
#     try:
#         while True:
#             x = (yield)
#             print(x, end=' ')
#     except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
#         print()
#         print('코루틴 종료')
 
# co = number_coroutine()
# next(co)
 
# for i in range(20):
#     co.send(i)
 
# co.close()

# 코루틴이 종료된때는 GeneratorExit 예외가 발생합니다.
# 때문에 위와 같이 try except 구문을 활용하여 종료시점에 종료메세지를 줄 수 있습니다.

# def sum_coroutine():
#     try:
#         total = 0
#         while True:
#             x = (yield)
#             total += x
#     except RuntimeError as e:
#         print(e)
#         yield total    # 코루틴 바깥으로 값 전달
 
# co = sum_coroutine()
# next(co)
 
# for i in range(20):
#     co.send(i)
 
# print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))

# 코루틴객체.throw(예외명, 예외메세지)를 작성해주면 예외를 밖으로 던져서 반환되도록 해줍니다.
# 1 ~ 19까지 더해주고나면 더 이상 더 할 수가 없으므로 RuntimeError가 발생하고 예외가 Throw 메소드로 인해 밖으로 던져져 나옵니다.
# yield 키워드로 total의 마지막값이 같이 나오면서 종료됩니다.

# def accumulate():
#     total = 0
#     while True:
#         x = (yield)         # 코루틴 바깥에서 값을 받아옴
#         if x is None:       # 받아온 값이 None이면
#             return total    # 합계 total을 반환
#         total += x
 
# def sum_coroutine():
#     while True:
#         total = yield from accumulate()    # accumulate의 반환값을 가져옴
#         print(total)
 
# co = sum_coroutine()
# next(co)
 
# for i in range(1, 11):    # 1부터 10까지 반복
#     co.send(i)            # 코루틴 accumulate에 숫자를 보냄
# co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
 
# for i in range(1, 101):   # 1부터 100까지 반복
#     co.send(i)            # 코루틴 accumulate에 숫자를 보냄
# co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄