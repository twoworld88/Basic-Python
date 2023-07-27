# def ten_div(x):
#     return 10 / x
# ten_div(0)

# 어떤 수를 0으로 나누는 경우 ZerodivisionError가 발생합니다.

# try:
#     x = int(input('나눌 숫자를 입력해주세요 : '))
#     y = 10 / x
#     print(y)
# except:
#     print('올바른 숫자를 넣어주세요.')

# try는 실행해야할 코드를 적어줍니다.
# except는 예외가 발생했을때 실행할 코드를 적어주면 예외가 발생했을 때 실행해줍니다.
# 이렇게 예외처리가 발생해도 멈추지 않고 실행되도록 할 수 있습니다.

# y = [10, 20, 30]
# try:
#     index, x = map(int, input('"인덱스_나누는 숫자"를 입력하세요 : ').split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:
#     print('정상적인 index를 입력해 주세요.')

# except 예외명: 으로 작성해주면 예외명의 예외가 발생했을 경우에만 except에 작성된 코드를 실행 합니다.

# y = [10, 20, 30]
# try:
#     index, x = map(int, input('"인덱스_나누는 숫자"를 입력하세요 : ').split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print('숫자를 0으로 나눌 수 없습니다.', e)
# except IndexError as e:
#     print('정상적인 index를 입력해 주세요.', e)

# except 예외명 as 변수: 로 작성하고 예외시 발생 코드에 변수를 넣어서 출력해주면 예외 내용이 출력됩니다,
# 이 때, 변수는 except의 e를 사용하는 경우가 대부분입니다.

# try:
#     x = int(input('나눌 숫자를 입력하세요 : '))
#     y = 10 / x
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:
#     print(y)

# else는 예외가 발생하지 않았을 때 실행될 코드를 작성하면 예외가 발생하지 않았을 경우에 실행해 줍니다.

# try:
#     x = int(input('나눌 숫자를 입력하세요 : '))
#     y = 10 / x
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:
#     print(y)
# finally:
#     print('코드의 실행이 종료되었습니다.')

# finally를 사용하고 코드를 작성하면 예외가 발생하든 발생하지 않든 언제나 마지막에 finally에 작성된 코드를 실행해줍니다.

# x = int(input('나눌 숫자를 입력하세요 : '))
# try:
#     y = 10 / x
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:
#     print(y)
# finally:
#     print('코드의 실행이 종료되었습니다.')

# try는 별도의 스택 프레임을 생성하지 않기 때문에 try내부에서 만든 변수를 밖에서도 쓸 수 있고 밖에서 만든 변수도 사용가능합니다.

# try:
#     x = int(input('3의 배수를 입력하세요 : '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.') # 예외를 발생시킴. 예외메세지는 생략가능
#     print(x)
# except Exception as e:
#     print('예외가 발생했습니다.', e)

# 3의 배수를 넣으면 정상적으로 해당 인수를 출력합니다.
# 3의 배수가 아닌 것은 넣어주면 raise로 인해 Exception 예외가 발생합니다.
# Exception 예외가 발생했을 경우 except의 코드가 실행되면서 해당 예외의 메세지가 출력되도록 되어있습니다.

# def three_multiple():
#     x = int(input('3의 배수를 입력하세요 : '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)

# try:
#     three_multiple()
# except Exception as e:
#     print('예외가 발생하였습니다.', e)

# 함수 내부에 try except가 없는 상태에서 raise로 예외를 발생시켰습니다.
# 이런 경우 에러가 발생한 순간 코드가 종료되는 것이 아니라 일단 상위 블럭인 함수밖으로 나와서도 try except가 없으면 코드가 종료되며 예외메세지가 뜹니다.
# 이 코드는 상위 블럭에 try except가 있으므로 종료되며 예외메세지를 띄우는게 아니라 해당 except에 맞는 코드가 실행됐습니다.

# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요 : '))
#         if x % 3 != 0:
#             raise Exception('3의 배수가 아닙니다.')
#         print(x)
#     except Exception as e:
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise

# try:
#     three_multiple()
# except Exception as e:
#     print('스크립트 파일에서 예외가 발생했습니다.', e)

# 예외를 함수내부에서 처리 했음에도 그 다음에 raise를 넣어주면 해당 예외를 다시 발생시켜서 함수 밖으로 넘깁니다.
# 함수 밖 try except에서 동일한 예외로 다시 처리해줄 수 있습니다.

# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요 : '))
#         if x % 3 != 0:
#             raise Exception('3의 배수가 아닙니다.')
#         print(x)
#     except Exception as e:
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise RuntimeError('three_multiple 함수에서 런타임 에러가 발생했습니다')

# try:
#     three_multiple()
# except RuntimeError as e:
#     print('스크립트 파일에서 예외가 발생했습니다.', e)

# 예외를 다시 발생시키면서 raise 예외명('예외메세지')를 적어주면 해당 예외와 예외메세지를 반환합니다.

# try:
#     x = int(input('3의 배수를 입력하세요 : '))
#     assert x % 3 == 0, '3의 배수가 아닙니다.'
#     print(x)
# except AssertionError as e:
#     print('예외가 발생했습니다.', e)

# assert 조건식, '예외메세지'와 같이 작성하면 조건식이 참이면 진행, 거짓이면 예외를 발생시키게 할 수 있습니다.
# 이 때 발생하는 예외는 AssertionErroe이며, 디버깅 모드에서만 사용이 가능한 방법입니다.
# 파이썬은 기본적으로 디버깅 모드이기에 사용이 가능합니다.
# assert가 있는 파일을 실행할 때, python -O 스크립트파일.py 와 같이 대문자 O를 붙여서 실행하면 assert는 실행되지 않습니다.

# class NotThreemultipleError(Exception):
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다.') 

# def three_mutiple():
#     try:
#         x = int(input('3의 배수를 입력하세요 : '))
#         if x % 3 != 0:
#             raise NotThreemultipleError
#         print(x)
#     except Exception as e:
#         print('예외가 발생했습니다.', e)
# three_mutiple()

# class 예외명(Exception):
#   def __init__(self):
#       super().__init__('에러메세지') 와 같이 작성해서 새로운 예외를 만들 수 있습니다.

# class NotThreemultipleError(Exception):
#     pass

# def three_mutiple():
#     try:
#         x = int(input('3의 배수를 입력하세요 : '))
#         if x % 3 != 0:
#             raise NotThreemultipleError('3의 배수가 아닙니다.')
#         print(x)
#     except Exception as e:
#         print('예외가 발생했습니다.', e)
# three_mutiple()

# 파생클래스를 만들고 pass해주고 예외발생 부분에서 메세지를 넣어줘도 똑같은 효과를 볼 수 있습니다.