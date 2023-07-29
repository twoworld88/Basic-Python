# def number_generator():
#     yield 0
#     yield 1
#     yield 2

# for i in number_generator():
#     print(i)

# 함수 안에 yield 키워드를 사용해서 이터레이터를 만들어 줬습니다.
# 이와 같이 yield 키워드를 사용해서  이터레이터를 생성해주는 함수를 제네레이터 또는 발생자라고 합니다.

# g = number_generator()
# print(dir(g))

# 제네레이터도 dir로 확인하면 __iter__, __next__ 메소드를 보유하고 있습니다.

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# 이터레이터는 __next__ 함수에서 return으로 직접 값을 반환했고 StopIteration 예외도 직접 발생시켰습니다.
# 하지만 제네레이터는 yield 키워드로 지정한 값을 __next__의 반환값으로 들어가서 반환되어 나오고 지정한 수가 끝나면 예외를 지정하지 않았음에도 StopIteration 예외가 발생합니다.

# class Counter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < self.stop:
#             r = self.current
#             self.current += 1
#             return r
#         else:
#             raise StopIteration
        

# def number_generator():
#     yield 0
#     yield 1
#     yield 2

# 위 이터레이터와 아래 제네레이터가 반환해 주는 값은 결과적으로 0 1 2 지만 그 과정이 상이합니다.
# 이터레이터는 next함수로 호출하면 return값을 반환하고 함수가 종료되면서 변환식에 의해 변환된 self.current가 다시 할당되며 함수가 반복되어 값을 반환합니다.
# 제네레이터는 next함수로 호출하면 값을 yield가 함수밖으로 반환하여 실행을 양보하고 대기합니다. 다시 호출하면 yield가 함수 밖으로 반환하여 실행을 양보하고 다시 대기합니다.
# 함수를 실행하고 반환하고 종료하고 ...... 실행하고 반환하고 종료하고 를 반복하고, 함수를 실행하고 반환하고 ...... 반환하고 종료하고 를 반복하느냐 단계의 차이가 있습니다.
# 이런 특징 때문에 제네레이터의 yield가 gene, gen, generator등이 아니라 양보하다라는 뜻의 yield가 쓰이는 겁니다.

# def number_generator(stop):
#     n = 0              # 숫자는 0부터 시작
#     while n < stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
#         yield n        # 현재 숫자를 바깥으로 전달
#         n += 1         # 현재 숫자를 증가시킴
 
# for i in number_generator(3):
#     print(i)

# 함수를 이용해서 제네레이터를 만들었습니다. n = 0으로 0부터 시작하는 변수를 생성하고 while문으로 n이 제네레이터 함수의 변수 stop보다 작을 때 반복되게 합니다.
# 그 다음 yield n을 실행하고 n += 1 로 n을 1씩 증가시키며 반복되게 합니다.
# 그럼 0 ~ stop에 할당된 인수 전까지 반복되는 제네레이터가 생성됩니다.

# def upper_generator(x):
#     for i in x:
#         yield i.upper()

# fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
# for i in upper_generator(fruits):
#     print(i)

# yield에 함수를 넣어주면 그 함수가 반환하는 값을 밖으로 전달해줍니다.

# def number_generator():
#     x = [1, 2, 3]
#     for i in x:
#         yield i

# for i in number_generator():
#     print(i)

# 함수 내부에서 반복가능한 객체 x에서 하나씩 꺼내서 yield를 통해 밖으로 전달하고 있습니다 
# 이런 경우 yield from을 이용해 더욱 간단하게 만들 수 있습니다.

# def number_generator():
#     x = [1, 2, 3]
#     yield from x

# for i in number_generator():
#     print(i)

# yield fro 반복가능한객체 or 이터레이터 or 제네레이터객체 와 같이 작성하면 for문을 작성한 것과 같이 해당 객체에서 값을 하나씩 꺼내 밖으로 전달합니다.

# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1
 
# def three_generator():
#     yield from number_generator(3)    # 숫자를 세 번 바깥으로 전달
 
# for i in three_generator():
#     print(i)

# 함수를 사용해서 제네레이터를 만들어주고 제네레이터객체를 yield from에 넣어줘도 원하는 결과를 출력하며 잘 실행됩니다.

# x = [i for i in range(50) if i % 2 == 0]
# y = (i for i in range(50) if i % 2 == 0)
# print(x)
# print(y)

# 리스트 표현식을 만들고 대괄호를 괄호로 치환하면 제네레이터 표현식이 됩니다.
# 리스트는 요소를 처음부터 다 만들어 두지만 제네레이터 표현식은 필요할때 호출되어 만들기 때문에 메모리를 절약할 수 있습니다.