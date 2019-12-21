# -*- encoding=utf-8 -*-  
"""
Created on 2017年5月6日
@author: poetry
"""

import threading

result = {}


def print_info(func):
    for i in range(10):
        print(str(i), "\t", func)

    result[func] = func * 200


if __name__ == "__main__":
    t1 = threading.Thread(target=print_info, name="T1", args=("T1",))

    t2 = threading.Thread(target=print_info, name="T2", args=("T2",))

    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('-' * 50)
    print("all over")

    for item in result.items():
        print(item[0], item[1])

    print(result["T1"])
