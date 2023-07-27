# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p1 = Point2D(x=30, y=20)    # 점1
# p2 = Point2D(x=60, y=50)    # 점2
 
# print('p1: {} {}'.format(p1.x, p1.y))    # 30 20
# print('p2: {} {}'.format(p2.x, p2.y))    # 60 50

# Point2D 클래스를 생성해서 점의 x, y인수는 x, y좌표가 되도록 속성을 부여합니다.
# p1, p2의를 인스턴스로 만들어줍니다.

# import math # math 모듈을 실행합니다.
 
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
 
# p1 = Point2D(x=30, y=20)    # 점1
# p2 = Point2D(x=60, y=50)    # 점2
 
# a = p2.x - p1.x    # 선 a의 길이
# b = p2.y - p1.y    # 선 b의 길이
 
# c = math.sqrt((a * a) + (b * b))    # a제곱과 b제곱을 더한 값을 더해준 후 제곱근을 구하는 math모듈의 메소드 sqrt 써서 제곱근을 구합니다.
# c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) # 제곱을 구하는 메소드인 pow함수를 사용해서 구해줘도 똑같은 값을 얻습니다.
# c = math.sqrt((a ** 2) + (b ** 2))    # ** 거듭제곱 연산자를 사용해도 똑같은 값을 얻습니다.
# print(c)  

# math함수 사용중 절대값을 반환해야 하는 경우가 있습니다 
# abs(값)을 사용하면 정수는 절대값을 정수로 실수는 절대값을 실수로 반환해줍니다.
# math.fabs(값)을 사용하면 무조건 절대값을 실수로 반환해줍니다.

# import math
# import collections
 
# Point2D = collections.namedtuple('Point2D', ['x', 'y'])    # namedtuple로 점 표현
 
# p1 = Point2D(x=30, y=20)    # 점1
# p2 = Point2D(x=60, y=50)    # 점2
 
# a = p1.x - p2.x    # 선 a의 길이
# b = p1.y - p2.y    # 선 b의 길이
 
# c = math.sqrt((a * a) + (b * b))
# print(c)    # 42.42640687119285

# collections 모듈을 사용하면 namedtuple을 사용하면 각 요소의 이름을 지정해 줄 수 있습니다.
# class명 = collections.namedtuple('자료형이름', ['요소명1', ...., '요소명2']) 와 같이 작성하면 클래스가 생성됩니다.
# 아직 어려운 개념이라 눈도장만 찍어두고 복습 또는 다른 책에서 추가로 공부해봅시다.

# class Rectangle:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
 
# rect = Rectangle(x1=20, y1=20, x2=40, y2=30)
 
# a = abs(rect.x2 - rect.x1)
# b = abs(rect.y2 - rect.y1)
# area = a * b
# print(area)

# 사각형의 넓이를 구해봤습니다 