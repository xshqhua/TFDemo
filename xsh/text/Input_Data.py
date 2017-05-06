# -*- coding:UTF-8
'''
Created on 2017年5月6日

@author: xsh
'''

import codecs 
import numpy as np
import pickle as pick
import threading
import time

class Read_Date():
#     def __init__(self):
    def __init__(self):
#         self.train_label = []
#         self.train_data = []
#         self.test_label = []
#         self.test_data = []
        self.result_data = {}
        self.dictionary_label = {}
        self.reverse_dictionary_label = {}
        self.category = set()
        self.clear_data = set()
        self.words_dictionary = {}
        self.reverse_dictionary_words = {}
        self._clear_data_read()
    def _read_raw_data(self, fileName=None, name=None):
        
        assert fileName != None 
        
        _data = []
        _label = []
        
        print(fileName,"start process ...")
        fileReader = codecs.open(fileName, "rb", "utf-8").readlines()
        for i in fileReader:
            i = i.strip()

            labeltep=i[:i.index(':')]
            if labeltep not in self.dictionary_label:
                self.dictionary_label[labeltep] = len(self.dictionary_label)+1
            
            _label.append(str(self.dictionary_label[labeltep])+"\n")
            
            tep_data = i[i.index(' ') + 1:]
            _data.append(self._clear_data(tep_data))
            
#         print(_label)     
        
        if "train_raw.txt" in fileName:
            train2data = fileName.replace("train_raw.txt","train_data.txt")
            train2label = fileName.replace("train_raw.txt","train_label.txt")
            
            t2d = open(train2data,"w")
            for line in _data:
                t2d.writelines(line)
                t2d.write("\n")
            t2d.close()
            
            open(train2label,"w").writelines(_label)
            
        elif "test_raw.txt" in fileName:
            test2data = fileName.replace("test_raw.txt","test_data.txt")
            test2label = fileName.replace("test_raw.txt","test_label.txt")
            
            t2d = open(test2data,"w")
            for line in _data:
                t2d.writelines(line)
                t2d.write("\n")
            t2d.close()
            open(test2label,"w").writelines(_label)
            print(len(_label))
            
        if name!=None:
            self.result_data[name] = [_data, _label]
            print(name,"\t",fileName,"is successful")
        else:
            print(fileName,"is successful")
            
        return [_data, _label]

    def _read_word2vec(self):
#         _fr = open(r"E:\TensorFlow\wordvectors\CH.Gigaword.300B.300d.pk","rb")
        print("word2vec start load ...")
        _fr = open(r"E:\TensorFlow\wordvectors\EN.glove.840B.300d.pk", "rb")
        w2v = pick.load(_fr)
        _fr.close()
        self.result_data["word2vec"] = w2v
        print("word2vec load successful")
        return w2v
    
    def _read_words(self):
#         _fr = open(r"E:\TensorFlow\wordvectors\CH.Gigaword.300B.300d.pk","rb")
        print("word2vec start load ...")
        _fr = open(r"./data/words.pkl", "rb")
        id2words = pick.load(_fr)
        _fr.close()
        self.result_data["id2words"] = id2words
        print("word2vec load successful")
        return id2words
    
    def _read_pkl(self,filename,name=None):
        
        assert name != None
        
        print(name," start load ...")
        _fr = open(filename, "rb")
        id2words = pick.load(_fr)
        _fr.close()
        self.result_data[name] = id2words
        print(name," load successful")
        return id2words
    
    def _clear_data_read(self):
        fileReader = codecs.open("./data/English_StopWords.txt", "rb", "utf-8").readlines()
        for i in fileReader:
            i = i.strip()
            self.clear_data.add(i)
      
    def _clear_data(self,line):
        tep1 = [w.strip() for w in line.strip().split()]
        tep2 = []
        for w in tep1:
            if w.lower() not in self.clear_data:
                if w.lower() not in self.words_dictionary:
                    self.words_dictionary[w.lower()] = len(self.words_dictionary)+1
#                 tep2.append(w)
                tep2.append(str(self.words_dictionary[w.lower()]))
#         print(tep2)
        return ' '.join(tep2)


    def read_raw_data_save2_number(self):
        t0 = time.time()
        train_file = "./corpus/train_raw.txt"
        test_file = "./corpus/test_raw.txt"
        
        t1 = threading.Thread(target=self._read_raw_data, name="train", args=(train_file,"train",))
        t2 = threading.Thread(target=self._read_raw_data, name="test", args=(test_file,"test",))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
        out_words = open("./data/words.pkl","wb")
        self.reverse_dictionary_words = {value:key for key,value in self.words_dictionary.items()}
        pick.dump(self.reverse_dictionary_words,out_words)
        
        self.reverse_dictionary_label = {value:key for key,value in self.reverse_dictionary_label.items()}
        out_category = open("./data/category.pkl","wb")
        pick.dump(self.reverse_dictionary_label,out_category)
        print("Consume time ",time.time() - t0)
        

    def load(self):
        t0 = time.time()
        t1 = threading.Thread(target=self._read_pkl, name="id2words",
                              args=("./data/words.pkl","id2words",))
        t2 = threading.Thread(target=self._read_pkl, name="category",
                              args=("./data/category.pkl","category",))
        t3 = threading.Thread(target=self._read_pkl, name="word2vec",
                              args=("E:\TensorFlow\wordvectors\CH.Gigaword.300B.300d.pk",
                                    "word2vec",))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        
        print("Consume time ",(time.time()-t0))


if __name__ == "__main__":
    read = Read_Date()
    print("start process ...")
    read.read_raw_data_save2_number()
    print("process successful")
    print("*"*50)
    print("start load ...")
    read.load()
    print("load successful")

