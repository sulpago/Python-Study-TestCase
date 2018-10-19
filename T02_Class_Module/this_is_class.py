class TestClass(object):
    static_num = 10

    def __init__(self, class_name):
        self.class_name = class_name

    @staticmethod
    def this_is_static_method(test_num):
        print("static_method")
        return TestClass.static_num + test_num

    @classmethod
    def this_is_class_method(cls, set_static_num):
        print("class_method")
        cls.static_num = set_static_num

    def check_static_num(self):
        print("check " + str(self.class_name) + "  static num " + str(self.static_num))

    def __this_is_inner_function(self, a, b):
        print("this is inner function")
        return a + b

    def this_can_called(self, a, b):
        return a + b


