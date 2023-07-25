# def plus_ten(x):
#     return x + 10
# print(plus_ten(1))

# plus_ten = lambda x : x + 10
# print(plus_ten(1))

# 위 코드는 def으로 만든 함수고 아래 코드는 lambda(람다)함수라고 한다.
# 람다함수는 식 형태로 되어 있다고 하여 람다 표현식이라고 부릅니다.

# print((lambda x : x + 10)(1))

# (람다표현식)(인수)와 같이 코드를 짜면 인수를 람다표현식에 대입한 값을 반환합니다.

# print((lambda x : y = 10; x + y)(1))

# y = 10
# print((lambda x : x + y)(1))

# 람다 표현식 내부에서 변수를 만들 수 없습니다. 단, 밖에 할당되어 있는 변수를 사용할 수는 있습니다.

# def plus_ten(x):
#     return x + 10
# print(list(map(plus_ten, [1, 2, 3])))

# print(list(map(lambda x : x + 10, [1, 2, 3])))

# 람다 표현식을 사용하는 대표적인 경우가 map함수를 사용하는 경우다.
# 맵 합수는 int, float, str을 input과 함께 써서 입력한 인수를 변환시키는 용도로 많이 썼지만 이렇게 직접 만든 함수에 활용할 수 있다.
# 3줄의 def으로 만든 함수를 람다 표현식으로 표현하면 1줄로 축약된다.

# a = list(range(1, 11))
# print(list(map(lambda x : str(x) if x % 3 == 0 else x, a)))

# 람다 표현식에서 if를 사용할 때는 반드시 else도 사용해줘야합니다.
# 람다 표현식에서 if는 식(if) if 조건식 else 식(else)으로 사용해야 합니다.

# a = list(range(1, 11))
# print(list(map(lambda x : str(x) if x % 3 == 0 else float(x) if x % 5 == 0 else int(x), a)))

# 람다표현식은 elif의 사용이 불가하다.
# 때문에 식(if1) if 조건식(if1) else 식(if2) if 조건식(if2) else 식(else) 와 같이 만들어 줘야한다.
# 너무 복잡하고 알아보고 힘들기 때문에 차라리 elif가 필요한 것부터는 def함수를 사용하는 것이 좋다.

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# c = [11, 12, 13, 14, 15]

# print(list(map(lambda x, y : x * y, a, b)))
# print(list(map(lambda x, y, z : (x + y) * z, a, b, c)))

# 람다에 내부에서 변수를 선언하는 것은 불가하지만 객체를 복수로 넣는 것은 가능합니다.
# 객체를 ,로 구분하여 넣어주면 됩니다.

# def f(x):
#     return x > 5 and x < 10

# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# print(list(filter(f, a)))

# print(list(filter(lambda x : x > 5 and x < 10, a)))

# filter(함수, 객체) 와 같이 filter 함수를 사용하면 함수조건에 맞는 시퀸스 자료형의 객체를 꺼내옵니다.

# from functools import reduce

# def f(x, y):
#     return x + y

# a = [1, 2, 3, 4, 5]
# print(reduce(f, a))

# print(reduce(lambda x, y : x + y, a))

# reduce(함수, 객체) 와 같이 reduce 함수를 사용하면 시퀀스 자료형의 요소를 하나씩 순차적으로 대입하여 누적된 값을 반환합니다.
# 위 코드에선 (1, 2)가 할당되어 3, (3, 3)이 할당되어 6, (6, 4)가 할당되어 10, (10, 5)가 할당되어 15가 최종적으로 반환되었습니다.
# reduce함수는 파이썬3부터 내장함수가 아니라 functools에 포함된 함수임으로 호출을 해주고 사용해야 합니다.
