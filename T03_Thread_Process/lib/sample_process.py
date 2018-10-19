from random import randint


def SampleProcess(process_name, size_of_run):
    size_of_run = size_of_run
    print("Process " + str(process_name) + " Start")
    cached_list = list()
    for i in range(0, size_of_run):
        temp_rand_int = randint(0, 100)
        cached_list.append(temp_rand_int)
    print("Process " + str(process_name) + " Done")
