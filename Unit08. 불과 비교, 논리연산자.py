# 비교 연산자는 값을 비교하는 것과 객체를 비교하는 것으로 나뉜다.
# 값을 비교하는 비교 연산자 : >, <, ==, >=, <=, != # 항상 먼저 있는 값을 기준으로 크고 작음을 판단한다.
# 객체를 비교하는 비교 연산자 : is, is not

# 값과 객체의 차이는?
# 예를 들어 값을 비교할 때 1 과 1도 같지만 1 과 1.0도 같습니다.
# 하지만 객체를 비교할 때 1 과 1은 같지만 1 과 1.0은 다릅니다. 
# 객체의 메모리 주소 값을 비교하기 때문인데 메모리 주소값의 확인은 id함수로 합니다.
# print(id(1)) # 140726873547560
# print(id(1.0)) # 2392329010864

# **** 값을 비교할 때 is, is not을 사용할 경우 변수지정등의 상황에서 제대로된 비교가 되지 않을 수 있기 때문에 사용하지 않습니다.

# 논리 연산자는 not, and, or가 있습니다.
# not은 논리 값 자체를 반대로 뒤집습니다.
# and는 모든 값이 True거나 False여야만 해당 값을 출력합니다.
# or 는 하나이상의 값이 True거나 모두 False여야만 해당 값을 출력합니다.
# 논리 연산자의 연산순서는 not, and, or 순서입니다.

# 논리와 비교 연산자가 혼용될 경우 비교연산을 우선하고 논리연산을 시행하며, 연산자와 수식이 혼용될 경우 수식을 시행하고 연산자를 시행합니다.
# 연산자에서는 첫째값으로 결과가 확실해지면 다음 연산을 시행하지 않습니다.

# print(False and True)
# print(True and False)
# 예를 들어 False and True 일 경우 이미 앞의 False에서 전체 연산이 결정됨으로 바로 False를 출력합니다.
# 하지만 True and False 일 경우 앞은 참이지만 뒤는 False이므로 False를 출력합니다.
# 위 두 개의 코드는 결과가 같지만 위 코드는 앞의 False가 출력된 것이고 아래 코드는 뒤 False가 출력된 것이라 볼 수 있습니다.

# print(0 and 'python')
# print(1 and '')
# 예를 들어서 0 and 'python'을 할 경우 앞에 0이 False이므로 연산이 종료되고 0을 출력합니다.
# 그리고 1 and ''을 항 경우 뒤의 앞의 1은 True고 ''이 False이므로 끝까지 연산된 후 ''을 출력합니다.