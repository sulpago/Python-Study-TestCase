import threading
from random import randint


class SampleThreadA(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.input_A = 1
        self.input_B = 20
        self.thread_name = thread_name

    def run(self):
        size_of_run = self.size_of_run
        print("Thread " + str(self.thread_name) + " Start")
        cached_list = list()
        for i in range(0, size_of_run):
            temp_rand_int = randint(0, 100)
            cached_list.append(temp_rand_int)
        print("Thread " + str(self.thread_name) + " Done")


    def set_make_list_size(self, size_of_run):
        self.size_of_run = size_of_run
        print("Thread " + str(self.thread_name) + " set " + str(self.size_of_run))

    def make_random_by_range(self):
        make_random_number = randint(self.input_A, self.input_B)
        return make_random_number

    def make_random_list(self):
        size_of_run = self.size_of_run
        print("Thread " + str(self.thread_name) + " Start")
        cached_list = list()
        for i in range(0, size_of_run):
            temp_rand_int = randint(0, 100)
            cached_list.append(temp_rand_int)
        print("Thread " + str(self.thread_name) + " Done")
        return cached_list
