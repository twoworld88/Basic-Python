# x = 10
# def foo():
#     print(x)
# foo()
# print(x)

# x와 같이 함수안에서도 출력이 가능하고 밖에서도 출력이 가능한 변수를 전역 변수라고 합니다.

# def foo():
#     x = 10
#     print(x)
# foo()
# print(x)

# x처럼 특정 지역 안에서 정의하여 그 지역에서만 사용이 가능한 변수를 지역변수라고 합니다.

# x = 10
# def foo():
#     x = 20
#     print(x)
# foo()
# print(x)

# 전역변수를 정의하고 함수내에서 전역변수를 바꾸려고 x를 다시 할당해도 전역변수에는 영향을 주지않고 새로운 지역변수 x가 정의됩니다.

# x = 10
# def foo():
#     global x
#     x = 20
#     print(x)
# foo()
# print(x)

# global 키워드를 사용해서 전역변수의 이름을 지정하면 함수내에서도 전역변수를 재정의할 수 있게 됩니다.

# def foo():
#     global x
#     x = 20
#     print(x)
# foo()
# print(x)

# 별도의 전역변수를 정의하지 않은 상태에서 global 키워드로 x를 전역변수로 선언하고 x를 정의하면 전역변수로 정의합니다.

# def print_hello():
#     hello = 'Hello, world!'
#     def print_massage():
#         print(hello)
#     print_massage()
# print_hello()

# print_hello() 함수를 호출하면 hello에 문자열 'Hello, world!'를 할당합니다.
# 다음으로 print_massage()함수를 정의합니다. print_massage()함수는 pinrt()함수로 변수 hello를 출력합니다.
# 마지막으로 print_massage()함수를 호출하며 함수 print_hello()가 종료됩니다.

# def a():
#     x = 10
#     def b():
#         x = 20
#     b()
#     print(x)
# a()

# 더 큰 지역은 작은 지역을 포함하며, 더 큰 지역에서 정의된 함수는 작은 지역에서 사용이 가능하지만 반대는 불가합니다.
# 마찬가지로 전역변수를 지역변수에서 재정의할 수 없던거처럼 작은 지역에서 더 큰 지역변수를 재정의 할 수 없습니다.

# def a():
#     x = 10
#     def b():
#         nonlocal x
#         x = 20
#     b()
#     print(x)
# a()

# 전역변수를 지역에서 정의하기 위해 global 키워드를 사용한 것처럼 nonlocal 키워드를 사용해서 유사한 효과를 줄 수 있습니다.

# def A():
#     x = 10
#     y = 100
#     def B():
#         x = 20
#         def C():
#             nonlocal x
#             nonlocal y
#             x = x + 30
#             y = y + 300
#             print(x)
#             print(y)
#         C()
#     B()
# A()

# A()가 실행되면서 x = 10, y = 100을 정의하고 함수 B()를 정의하고 함수 B()를 실행합니다.
# B()가 실행되면서 x = 20을 정의하지만 아직 더 큰 지역에서 정의한 x에 영향을 주지 못하고 함수 C()를 정의하고 함수 C()를 실행합니다.
# C()가 실행되면서 nonlocal x, nonlocal y로 지역변수의 경계가 사라지면서
# x 는 가장 마지막으로 정의한 20이 되고 x = 20 + 30으로 50이 되며 y = 100 + 300으로 400이 됩니다.
# print(x), print(y)로 인해 50과 400이 출력되며 함수가 종료됩니다.
# 사실 실무에서는 변수마다 다른 이름을 부여하기 때문에 이런 단계를 따지며 만들일은 거의 없습니다.

# x = 1
# def A():
#     x = 10
#     def B():
#         x = 20
#         def C():
#             global x
#             x = x + 30
#             print(x)
#         C()
#     B()
# A()

# 위와 마찬가지지만 global x는 전역과 지역의 경계를 허물어주는 것이 아니라 전역함수를 호출해와서 사용하는 것으로 변수를 다시 정의하지 않으면
# 처음에 정의한 전역함수가 적용돼서 x = 1 + 30으로 31이 됩니다.

# def calc():
#     a = 3
#     b = 5
#     def mul_add(x):
#         return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
#     return mul_add          # mul_add 함수를 반환, 함수 자체를 반환할 때는 ()를 붙이지 않습니다.
 
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))

# c(1) = calc(1)로 함수 calc(): 에 1을 넣어서 a = 3, b = 5를 정의하고 함수 mul_add를 정의한 후 mul_add함수를 return으로 반환하고 종료됩니다.
# 하지만 반환한 mul_add(1)로 mul_add함수가 호출되면서 3 * 1 + 5의 값이 반환됩니다.
# 이처럼 함수가 calc()이 종료된 후에도 calc()에서 정의한 지역변수를 변수 c는 사용하고 있습니다.
# 이렇게 함수를 둘러싸고 있는 지역의 변수, 코드 등을 계속 유지한체 내부 함수를 호출하여 사용하는 함수를 클로저라고 합니다.
# 여기서는 변수 c에 저장된 mul_add가 클로저입니다.

# def calc():
#     a = 3
#     b = 5
#     return lambda x : a * x + b
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))

# 이렇게 람다 표현식을 사용해서 클로저를 좀 더 간략하게 표현할 수 있습니다.

# def calc():
#     a = 3
#     b = 5
#     total = 0
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add
 
# c = calc()
# c(1)
# c(2)
# c(3)

# c(1)가 호출되면서 nonlocal total로 total의 지역개념이 없어지고 total = 0 + 3 * 1 + 5 = 8이 출력되며 total에 8이 저장됩니다.
# c(2)가 호출되면서 마찬가지로 total = 8 + 3 * 2 + 5 = 19가 출력되며 total에 19가 저장됩니다.
# c(3)이 호출되면서 마찬가지로 total = 19 + 3 * 3 + 5 = 33이 호출되며 함수가 종료합니다.

