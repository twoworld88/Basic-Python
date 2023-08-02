# import square2

# print(square2.base)
# print(square2.square(3))

# 모듈이란 다시 한 번 이야기하지만 클래스와 함수, 변수들의 집합으로 되어 있는 .py파일을 말한다.
# 패키지란 그 모듈 파일을 모아놓은 폴더라 할 수 있다.
# 직접 만들어서 사용할 수 있으며 이 경우 같은 폴더에 저장되어 있어야 사용가능하다.

# import Person

# maria = Person.Person('마리아', 20, '서울시 서초구 반포동')
# maria.greeting()

# from Person import Person

# maria = Person('마리아', 20, '서울시 서초구 반포동')
# maria.greeting()

# 모듈을 불러와서 클래스를 실행할수도 있고 모듈의 클래스만 불러와서 실행하는 것도 가능하다.

# import hello

# print('main.py __name__:', __name__)

# __name__함수는 프로그램이 실행될 때 가장 최초로 시작하는 프로그램의 __name__에 항상 __main__을 반환해줍니다.
# __main__에서 불러오는 모듈에 있는 __name__함수에는 그 모듈명이 반환됩니다.

# import calc

# print(calc.add(10, 50))

# calc가 모듈로 호출되어 사용됐기 때문에 if __name__ == '__main__':는 실행되지 않습니다.
# 하지만 직접 함수를 호출해서 사용하는 것은 가능합니다.

# import calcpkg.geometry
# import calcpkg.operation

# print(calcpkg.operation.add(10, 20))
# print(calcpkg.operation.mul(10, 20))
# print(calcpkg.geometry.triangle_area(30, 40))
# print(calcpkg.geometry.rectangle_area(30, 40))

# calcpkg폴더를 만들고 그 안에 __init__.py파일과 모듈기능할 코드를 작성한 .py파일을 저장하니 패키지가 생성되었다.
# 이 때, __init__.py 파일은 아무런 내용이 없어도 작동한다.

# from calcpkg.operation import add, mul

# print(add(10, 20))
# print(mul(10, 20))

# from 패키지명.모듈명 import 변수명, 함수명, 클래스명 사용도 가능하다.
# 이런 패키지에 있는 모듈에 __name__함수를 넣어서 값을 반환하면 모듈명이 아닌 패키지명.모듈명이 반환된다.

# import requests

# print(requests.__path__)

# __path__함수를 사용하면 모듈이 저장되어 있는 위치를 탐색할 수 있습니다.

# import calcpkg

# print(calcpkg.operation.add(10, 20))
# print(calcpkg.operation.mul(10, 20))
# print(calcpkg.geometry.rectangle_area(30, 40))
# print(calcpkg.geometry.triangle_area(30, 40))

# 패키지를 생성해주었던 __init__.py 파일에 from . import 내장되어 있는 모듈명 을 작성해주면 이런 형식으로 작성되어 있는 모듈은 패키지명만 호출해도 작동합니다.
# 이 때 패키지에 저장된 모든 모듈을 사용하고 싶다면 from . import *로 작성하시면 됩니다.

# from calcpkg import *

# print(add(10, 20))
# print(mul(10, 20))
# print(triangle_area(30, 40))
# print(rectangle_area(30,40))

# __init__.py파일에 추가로 from .모듈명 import 내장된 클래스, 내장된 함수, 내장된 변수를 쭉 나열해서 적어주고 저장하면 한꺼번에 호출해놓고 사용할 수 있게 됩니다.
# 이 때 모듈에 내장된 모든 클래스, 함수, 변수를 사용하고 싶다면 from .모듈명 import *로 작성하시면 됩니다.
# 공개하고 싶은 소스가 있고 그렇지 않은 소스가 있을 수 있다. __all__=['공개할 클래스명', '공개할 함수명', '공개할 변수명']을 __init__.py에 추가해주면 __all__에 리스트로 할당된 것들만 공개됩니다.
# 파이썬의 패키지는 패키지 안에 패키지 즉, 하위 패키지를 생성할 수 있습니다.
# 패키지 폴더 아래 폴더를 만들고 마찬가지로 __init__.py와 모듈파일을 넣어주면 됩니다.
# 하위 패키지를 사용할 때는 import 패키지명.하위패키지명.모듈명 으로 호출해주면 됩니다.
# 하위 패키지도 모든 기능을 가져와서 사용하고 싶다면 패키지에 있는 __init__.py파일에 from .하위패키지명.모듈명 import * 로 호출해주면 됩니다.
# 패키지에 하위패키지1, 하위패키지2가 있을 때, 하위 패키지2에서 작성되고 있는 코드에서 하위패키지 1에 있는 모듈의 함수를 사용하고 싶을 때가 있을 겁니다.
# 이럴 때는 from ..하위패키지1 import 모듈명 으로 작성해서 모듈을 가져올 수 있습니다.
# from ..하위패키지1.모듈명 import 클래스명, 함수명, 변수명 으로 특정 클래스나 함수, 변수를 가져올 수 있습니다.
# from ..하위패키지1.모듈명 import *을 통해 특정 모듈을 모두 불러올 수도 있습니다.
# 모듈과 패키지의 독스트링은 '''독스트링'''으로 작성하며, 모듈명.__doc__ 와 패키지명.__doc__로 호출합니다.


