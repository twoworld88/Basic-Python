# import turtle as t

# t.shape('turtle')

# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)

# t.mainloop()

# turtle모듈의 t메소드의 기능만을 불러와서 사각형을 그려보는 코드입니다.
# fd = forward, rt = right 이며, bk = backward, left = lt도 있습니다.
# mainloop는 위 코드를 실행하고 입력을 하기 전까지 대기하게 만드는 코드입니다.

# import turtle as t

# t.shape('turtle')
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.mainloop()

# for문을 이용하여 사각형을 그리는 코드입니다.

# import turtle as t

# t. shape('turtle')
# for i in range(5):
#     t.forward(100)
#     t.right(360 / 5) # 360을 5로 나눈 값을 외각으로 함.
# t.mainloop()

# for문을 이용하여 오각형을 그리는 코드입니다.
# 연산자를 넣어줘도 작동합니다.

# import turtle as t

# n = int(input())

# t.shape('turtle')

# for i in range(n):
#     t.forward(100)
#     t.right(360 / n)

# t.mainloop()

# input으로 입력한 숫자를 n이란 변수에 할당하여 n각형을 만드는 코드입니다.

# import turtle as t

# t.shape('turtle')
# t.color('blue') # 펜의 색을 지정
# t.begin_fill() # 색칠할 영역의 시작
# for i in range(6):
#     t.forward(60)
#     t.right(360 / 6)
# t.end_fill() # 색칠할 영역의 끝
# t.mainloop()

# 파란색으로 육각형을 그리고 그 안을 파란색으로 채우는 코드입니다.
# t.color()에 값은 웹색깔을 넣어줘도 작동합니다.
# 웹색깔은 16진수 3개로 색상을 표현해놓은 것이며, 아래서 확인가능합니다.
# 웹 색상: https://ko.wikipedia.org/wiki/웹_색상
# HTML Color Picker: https://www.w3schools.com/colors/colors_picker.asp

# import turtle as t
# t.shape('turtle')
# t.circle(120)
# t.mainloop()

# 반지름이 120인 원을 그리는 코드입니다.

# import turtle as t

# n = 60

# t.shape('turtle')
# t.speed('fastest') # 원을 그리는 속도

# for i in range(n):
#     t.circle(120)
#     t.right(360 / n) # 원을 그려주는 각도를 바꿔준다.

# t.mainloop()

# 60번 각도를 360/60도씩 틀어서 매우 빠른속도로 원을 그려주는 코드입니다.
# 속도는 다음과 같이 구분됩니다(숫자로는 0 ~ 10, 문자로는 5가지)
# 'fastest' : 0
# 'fast' : 10
# 'normal' : 6
# 'slow' : 3
# 'slowest' : 1

# import turtle as t

# t.shape('turtle')
# t.speed('fastest')

# for i in range(300):
#     t.forward(i)
#     t.right(91)

# t.mainloop()

# # i만큼 앞으로 이동하며, 91도씩 각도를 바꿔줍니다.
# t.shape()에 다음과 같이 입력하여 거북이가 아닌 다른 모양을 선택할 수 있습니다.
# t.shape()을 입력해서 실행해주면 현재 선택된 모양이 무엇인지 출력합니다.
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic' 등이 있습니다.