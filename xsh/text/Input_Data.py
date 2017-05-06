# -*- coding:UTF-8
'''
Created on 2017年5月6日

@author: xsh
'''

import codecs 
import numpy as np


class Read_Date():
    
    def __init__(self):
#         self.train_label = []
#         self.train_data = []
#         self.test_label = []
#         self.test_data = []
        self.dictionary = {}
        self.reverse_dictionary = {}
    def read_data(self,train_file="",test_file=""):
        fileReader = codecs.open(train_file, "rb", "utf-8").readlines()
        train_data = []
        test_data = []
        train_label = []
        test_label = []
        for i in fileReader:
            i=i.strip()
#             print(i[i.index(' ')+1:])
            label=i[:i.index(':')]
            self.dictionary[label] = len(self.dictionary)+1
            train_label.append(i[:i.index(':')])
            train_data.append(i[i.index(' ')+1:])
            
        fileReader = codecs.open(test_file, "rb", "utf-8").readlines()
#         self.train_data = []
        for i in fileReader:
            i=i.strip()
#             print(i[i.index(' ')+1:])
            test_label.append(i[:i.index(':')])
            test_data.append(i[i.index(' ')+1:])
        
        self.reverse_dictionary = {value:key for key,value in self.dictionary.items()}
        
        return train_data,train_label,test_data,test_label
if __name__ == "__main__":
    train_file = "./corpus/train.txt"
    test_file = "./corpus/test.txt"
    Read_Date().read_data(train_file, test_file)
    
    
