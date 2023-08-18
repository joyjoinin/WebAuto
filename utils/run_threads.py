import threading
from testcase.web.create_pick_auction import create_pick_auction
from testcase.web.create_pick_set_price import create_pick_set_price
from testcase.web.create_random_auction import create_random_auction
from testcase.web.create_random_set_price import create_random_set_price


def threads_flow():
    threads = [threading.Thread(target=create_pick_auction),
               threading.Thread(target=create_pick_set_price),
               threading.Thread(target=create_random_auction),
               threading.Thread(target=create_random_set_price)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def run_threads_flow():
    thread = threading.Thread(target=threads_flow)
    thread.start()
