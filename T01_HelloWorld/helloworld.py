
# 콘솔 창에 헬로우 월드 띄우기
print("Hello World")

# 혹시, 한글 출력 문제있나 확인할겸
print("헬로우 월드")

# 계산식 출력도 바로 됨
print(3 + 4)


# 함수 Define 출력하는 경우는 이렇게
def hello_function():
    print("hello function")


# 그리고 실행은 이렇게.
hello_function()


# 변수 입력은 이렇게
def test_function_01(get_input):
    # 숫자도 받아서 보여줄려면...
    message = "Get Input : " + str(get_input)
    print(message)


test_function_01("안녕?")
test_function_01(1)


# 변수 활용시 주의할 것~!!
def test_copy_01():
    origin_list = [0, 1, 2, 3, 4, 5]
    # 사실 이렇게 list 선언 안해도 되긴 함.
    copy_list = list()
    copy_list = origin_list
    copy_list.remove(2)
    print(str(origin_list))
    print(str(copy_list))


def test_copy_02():
    import copy
    origin_list = [0, 1, 2, 3, 4, 5]
    copy_list = list()
    copy_list = copy.deepcopy(origin_list)
    copy_list.remove(2)

    print(str(origin_list))
    print(str(copy_list))


test_copy_01()
test_copy_02()


# 여러개를 리턴하면, 기본적으로 tuple 형식으로~~
def test_return_type_01(input_message=None):
    print("Fake Return")
    return True, "FakeMessage", input_message


# 혹은 직접 type을 설정해서 return 하거나.
def test_return_type_02(input_message=None):
    print("Fake Return")
    return [True, "FakeMessage", input_message]


get_return_01 = test_return_type_01()
# 이렇게 하면, 해당 변수 의 type 확인이 가능하다!
print(type(get_return_01))
# 물론 이런것도 가능함
print(type(test_copy_02))
import os
print(type(os))

get_return_02 = test_return_type_02()
print(type(get_return_02))
