import datetime
from random import randint
from multiprocessing import Process
from multiprocessing import freeze_support
from T03_Thread_Process.lib.sample_threading import SampleThreadA
from T03_Thread_Process.lib.sample_process import SampleProcess


class StopWatcher(object):
    def start(self):
        start_time = datetime.datetime.now()
        print("-" * 20)
        print("Start time : " + str(start_time))
        print("-" * 20)
        self.start_time = start_time

    def stop(self):
        end_time = datetime.datetime.now()
        print("-" * 20)
        print("End time : " + str(end_time))
        print("-" * 20)
        self.end_time = end_time
        self.take_time()

    def take_time(self):
        end_time = self.end_time
        start_time = self.start_time
        run_time = end_time - start_time
        print("-" * 20)
        print("Take Time : " + str(run_time))
        print("-" * 20)


def just_run(size_of_run):
    watcher = StopWatcher()
    watcher.start()
    cached_list = list()
    for i in range(0, size_of_run):
        temp_rand_int = randint(0, 100)
        cached_list.append(temp_rand_int)
    watcher.stop()


def thread_run(size_of_run, run_thread_num):
    watcher = StopWatcher()
    watcher.start()

    each_run_for_thread = size_of_run // run_thread_num

    threading_jobs = []

    # Thread를 세팅하고, thrading josb 리스트에 각 job을 할당하자.
    for idx_thread in range(0, run_thread_num):
        cached_thread = SampleThreadA("Th" + str(idx_thread))
        if idx_thread == 0:
            # 첫번째 쓰레드에 나머지 몰아주자.
            first_thread_burden = size_of_run - (each_run_for_thread * (run_thread_num - 1))
            cached_thread.set_make_list_size(first_thread_burden)
        else:
            cached_thread.set_make_list_size(each_run_for_thread)
        threading_jobs.append(cached_thread)

    # 각 리스트에 할당된 스레드 실행!
    print("Run Thread")
    for thread_worker in threading_jobs:
        thread_worker.start()

    # 결과값 기다리자.
    print("Wait for Thread job done")
    for thread_worker in threading_jobs:
        thread_worker.join()

    # 나중에 결과 받을려면queue를 써서 할당 받아야....

    watcher.stop()


def process_run(size_of_run, run_process_num):
    watcher = StopWatcher()
    watcher.start()

    each_run_for_process = size_of_run // run_process_num

    process_jobs = []

    for idx_process in range(0, run_process_num):
        temp_process_name = "PID_" + str(idx_process)
        if idx_process == 0:
            first_process_burden = size_of_run - (each_run_for_process * (run_process_num - 1))
            cached_process = Process(target=SampleProcess, args=(temp_process_name, first_process_burden))
        else:
            cached_process = Process(target=SampleProcess, args=(temp_process_name, each_run_for_process))
        process_jobs.append(cached_process)

    # 각 리스트에 할당된 프로세스 실행!
    print("Run Process")
    for process_worker in process_jobs:
        process_worker.start()

    # 결과값 기다리자.
    print("Wait for Process job done")
    for process_worker in process_jobs:
        process_worker.join()

    watcher.stop()

def run_benck_mark():
    run_epoch = 10000000
    just_run(run_epoch)
    # thread_run(run_epoch, 2)
    process_run(run_epoch, 4)

# 윈도우 에서는 꼭!!!  freeze_support를 호출해야 한다.
if __name__ == '__main__':
    freeze_support()
    run_benck_mark()
