# 지금까지 대부분의 작업은 기본 내장함수를 이용해서 코딩을 했습니다.
# 하지만 기본 내장함수로는 구현할 수 있는 한계가 너무나 명확하기에 외장 모듈이나 패키지, 라이브러리를 받아서 사용합니다.
# 모듈이란 특정 기능을 .py파일 단위로 작성해놓은 것을 말합니다.
# 패키지란 특정 기능과 관련된 여러 개의 모듈을 묶어 놓은 걱으로 모듈에 네임스페이스를 제공합니다.
# 라이브러리 모듈과 패키지를 묶어놓은 것을 말하며, 파이썬에 기본으로 내장된 모듈 패키지 내장함수를 포괄하여 표준 라이브러리라 칭합니다.

# import math

# print(math.pi)
# print(math.sqrt(4.0))
# print(math.sqrt(2.0))
# print(math.sqrt(9))

# import 모듈명 을 입력해서 모듈을 불러올 수 있습니다.
# 모듈명.모듈내장함수명 을 입력해서 함수를 사용할 수 있습니다.
# 변수가 필요한 경우 모듈명.모듈내장함수명(변수)와 같이 작성합니다.

# import math as m

# print(math.sqrt(4))
# print(m.sqrt(9))

# import 모듈명 as 간이호칭 과 같이 작성하면 간이호칭을 부여할 수 있습니다.
# 간이호칭을 지정하면 모듈을 호출할때 모듈명 대신 간이호칭을 넣어줘도 호출됩니다.
# 단, 간이호칭을 지정하면 본래 모듈명을 썼을 경우 예외가 발생합니다.

# from math import pi, sqrt

# print(pi)
# print(sqrt(4.0))

# from 모듈명 import 변수명 또는 함수명 또는 클래스명을 입력해주면 해당 변수나 함수 또는 클래스만을 호출해서 가져옵니다.
# from 모듈명 import 변수명, 함수명, 클래스명 과 같이 ,로 구분하여 여러개 넣어주면 한꺼번에 호출할수도 있습니다.
# from 모듈명 import * 이라 작성하면 해당 모듈의 모든 변수, 함수, 클래스를 호출해옵니다.

# from math import pi as p
# from math import sqrt as s

# print(p)
# print(s(9.0)) 

# from 모듈명 import 변수명 또는 함수명 또는 클래스명 as 간이호칭 으로 작성하면 불러온 변수, 함수, 클래스에 간이호칭을 부여할 수 있습니다.

# from math import pi as p, sqrt as s

# print(p)
# print(s(9.0)) 

# from 모듈명 import 변수명 as 간이호칭, 함수명 as 간이호칭, 클래스명 as 간이호칭 과 같이 ,로 구분해서 여러개를 한꺼번에 입력할수도 있습니다.

# import urllib.request

# response = urllib.request.urlopen('https://www.google.co.kr')
# print(response.status)

# 패키지의 사용은 import 패키지명.모듈명 으로 패키지 내부에 있는 모듈을 불러올 수 있습니다.
# 모듈 사용때와 마찬가지로 import 패키지명.모듈명1, 패키지명.모듈명2 모듈 여러개를 한꺼번에 불러올 수 있습니다.
# 다음으로 패키지에 포함된 모듈의 변수와 함수, 클래스는 패키지명.모듈명.변수, 패키지명.모듈명.함수(), 패키지명.모듈명.클래스()로 호출할 수 있습니다.

# import urllib.request as r

# response = r.urlopen('https://www.google.co.kr')
# print(response.status)

# 패키지에 있는 모듈을 사용할 떄도 모듈사용과 마찬가지로 as 간이호칭을 달아서 간이호칭을 지정할 수 있습니다.

# from urllib.request import Request, urlopen

# req = Request('https://www.google.co.kr')
# response = urlopen(req)
# print(response.status)

# from 패키지명.모듈명 import 변수명 또는 함수명 또는 클래스명을 입력해주면 해당 변수나 함수 또는 클래스만을 호출해서 가져옵니다.
# from 패키지명.모듈명 import 변수명, 함수명, 클래스명 과 같이 ,로 구분하여 여러개 넣어주면 한꺼번에 호출할수도 있습니다.
# from 패키지명.모듈명 import * 이라 작성하면 해당 모듈의 모든 변수, 함수, 클래스를 호출해옵니다.

# from urllib.request import Request as r, urlopen as u

# req = r('https://www.google.co.kr')
# response = u(req)
# print(response.status)

# from 패키지명.모듈명 import 변수명 또는 함수명 또는 클래스명 as 간이호칭 으로 작성하면 불러온 변수, 함수, 클래스에 간이호칭을 부여할 수 있습니다.
# from 패키지명.모듈명 import 변수명 as 간이호칭, 함수명 as 간이호칭, 클래스명 as 간이호칭 과 같이 ,로 구분해서 여러개를 한꺼번에 입력할수도 있습니다.

# import requests

# r = requests.get('https://www.google.co.kr')
# print(r.status_code)

# 모듈이나 패키지를 설치할 때는 명령프롬프트나 터미널에 pip install 모듈명 또는 패키지명 을 입력하면 됩니다.
