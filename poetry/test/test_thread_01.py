# -*- encoding=utf-8 -*-  
"""
Created on 2017年5月6日
@author: poetry
"""

import threading
import queue
from numpy import empty


q = queue.Queue()
def print_info(func):
    for i in range(10):
        print(str(i), "\t", func)
    
    q.put((func * 2, func))
         
if __name__ == "__main__":
    t1 = threading.Thread(target=print_info, name="T1", args=("T1",))
    
    t2 = threading.Thread(target=print_info, name="T2", args=("T2",))
    
    t1.setDaemon(True)
    t2.setDaemon(True)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print ('-' * 50)
    print("all over")
    result = []
    while not q.empty():
        result.append(q.get())
    
    for item in result:
#             print (item[1],item[0])
        
        if item[1] == print_info.__name__:
            print (item[1],item[0])
        else:
            print("no")
            print(print_info.__name__)
    
