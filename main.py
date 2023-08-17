import threading
from time import sleep
from testcase.web.test1 import test1
from testcase.web.test2 import test2
from testcase.web.test3 import test3
from testcase.web.test4 import test4


def threads_flow():
    threads = [threading.Thread(target=test1), threading.Thread(target=test2), threading.Thread(target=test3),
               threading.Thread(target=test4)]
    for thread in threads:
        thread.start()
        sleep(30)
    for thread in threads:
        thread.join()


def run_threads_flow():
    thread = threading.Thread(target=threads_flow)
    thread.start()


if __name__ == '__main__':
    run_threads_flow()
