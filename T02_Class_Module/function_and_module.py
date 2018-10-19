from T02_Class_Module.this_is_class import TestClass
from T02_Class_Module.this_is_module import module_for_test

def class_tester():
    # Class를 설정하는데, 초기 init에서 사용하는 변수를 설정해야 함.
    a_class = TestClass("A_Class")
    b_class = TestClass("B_Class")

    # 각 class별 할당된 값을 확인해볼수 있음.. (class name 으로)
    a_class.check_static_num()
    b_class.check_static_num()

    # static 함수는 이렇게 사용도 하지만..
    print(str(a_class.this_is_static_method(10)))
    print(str(b_class.this_is_static_method(20)))
    # 그냥 불러서 사용할수도 있다.
    print(str(TestClass.this_is_static_method(30)))

    # A의 class method만 바꾸어 주지만...
    a_class.this_is_class_method(55)

    # 둘다 바꾼것을 확인할수 있음.
    a_class.check_static_num()
    b_class.check_static_num()

    # 또한, 그냥 불러서도 할당이 가능.
    TestClass.this_is_class_method(10)
    a_class.check_static_num()
    b_class.check_static_num()

    # 둘다 class를 할당해서, class
    print(type(a_class))
    print(type(b_class))

def module_tester():
    tester = module_for_test.tester()
    # 이거는 모듈
    print(type(module_for_test))
    # 이거는 function
    print(type(module_for_test.tester))
    # return이 없으므로 nonetype
    print(type(tester))

class_tester()
module_tester()