# -*- coding:UTF-8 -*- 
'''
Created on 2017年5月6日

@author: xsh
'''

import codecs 
import numpy as np
import pickle as pick
import threading
import time
import nltk 
from nltk.stem import WordNetLemmatizer 
from boto.dynamodb2.types import NUMBER
lemmatizer = WordNetLemmatizer()

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
        self.count_train = None
        self.count_test = None
        self.lemmatizer = WordNetLemmatizer()
    def _read_raw_data(self, fileName=None, name=None):
        
        assert fileName != None 
        
        _data = []
        _label = []
        
        print(fileName, "start process ...")
        fileReader = codecs.open(fileName, "rb", "utf-8").readlines()
        for i in fileReader:
            i = i.strip()

            labeltep = i[:i.index(':')]
            if labeltep not in self.dictionary_label:
                self.dictionary_label[labeltep] = len(self.dictionary_label) + 1
            
            _label.append(str(self.dictionary_label[labeltep]) + "\n")
            
            tep_data = i[i.index(' ') + 1:]
            _data.append(self._clear_data(tep_data))
            
#         print(_label)     
        t2data = ""
        t2label = ""
        if "train_raw.txt" in fileName:
            t2data = fileName.replace("train_raw.txt", "train_data.txt")
            t2label = fileName.replace("train_raw.txt", "train_label.txt")
            
        elif "test_raw.txt" in fileName:
            t2data = fileName.replace("test_raw.txt", "test_data.txt")
            t2label = fileName.replace("test_raw.txt", "test_label.txt")
            
        t2d = open(t2data, "w")
        for line in _data:
            t2d.writelines(line)
            t2d.write("\n")
        t2d.close()
        
        
        label2vec = []
        label_size = len(self.dictionary_label)
        for i in _label:
            __label2vec = ['0']*label_size
            __label2vec[int(i)-1] = '1'
            label2vec.append(__label2vec)
        
        
        t2l = open(t2label, "w")
        for l2v in label2vec:
#             print(l2v)
            t2l.writelines(" ".join(l2v))
            t2l.write("\n")
        t2l.close()
#         print(len(_label))
            
            
            
            
            
            
        if name != None:
            self.result_data[name] = [_data, _label]
            print(name, "\t", fileName, "is successful")
        else:
            print(fileName, "is successful")
            
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
    
    def _read_pkl(self, filename, name=None):
        
        assert name != None
        
        print(name, " start load ...")
        _fr = open(filename, "rb")
        id2words = pick.load(_fr)
        _fr.close()
        self.result_data[name] = id2words
        print(name, " load successful")
        return id2words
    
    def _clear_data_read(self):
        fileReader = codecs.open("./data/English_StopWords.txt", "rb", "utf-8").readlines()
        for i in fileReader:
            i = i.strip()
            self.clear_data.add(i)
      
    def _clear_data(self, line):
        tep1 = [w.strip() for w in line.strip().split()]
        tep2 = []
        for w in tep1:
            if w.lower() not in self.clear_data:
                if w.lower() not in self.words_dictionary:
                    self.words_dictionary[w.lower()] = len(self.words_dictionary) + 1
#                 tep2.append(w)
                tep2.append(str(self.words_dictionary[w.lower()]))
#         print(tep2)
        return ' '.join(tep2)


    def read_raw_data_save2_number(self):
        t0 = time.time()
        train_file = "./corpus/train_raw.txt"
        test_file = "./corpus/test_raw.txt"
        
        t1 = threading.Thread(target=self._read_raw_data, name="train", args=(train_file, "train",))
        t2 = threading.Thread(target=self._read_raw_data, name="test", args=(test_file, "test",))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
        out_words = open("./data/words.pkl", "wb")
        self.reverse_dictionary_words = {value:key for key, value in self.words_dictionary.items()}
        pick.dump(self.reverse_dictionary_words, out_words)
        
        self.reverse_dictionary_label = {value:key for key, value in self.reverse_dictionary_label.items()}
        out_category = open("./data/category.pkl", "wb")
        pick.dump(self.reverse_dictionary_label, out_category)
        print("Consume time ", time.time() - t0)
    
    def _read_label(self, filename):
        _label = []
#         _label = []
        fr = open(filename, "r")
        for w in fr.readlines():
            _label.append(np.array([int(i) for i in w.strip().split()]))
        return _label
    
    def _read_data(self, filename):
        _data = []
#         _label = []
        fr = open(filename, "r")
        for w in fr.readlines():
            _data.append(np.array([int(i) for i in w.strip().split()]))
#             _data.append(np.array(re))
            
        return np.array(_data)
    
    
    def _read_data2(self, filename):
        _data = []
#         _label = []
        fr = open(filename, "r")
        for w in fr.readlines():
            ids_ = [i.lower() for i in w.strip().split()]
#             print (ids_)
            re=[]
            for j in ids_:
                j1 = int(j)
#                 print(self.result_data["id2words"].keys())
                if j1 in self.result_data["id2words"].keys():
#                     print("zai")
                    tep = self.id2Vec(j1) 
                    if tep!=None:
                        re.append(tep)
#             print(len(re))
            _data.append(np.array(re))
            
        return _data
    
    def id2Vec(self,number):
#         print(number)
        keys = self._stem(self.result_data["id2words"][number])
        
        for key in keys:
            if key in self.result_data["word2vec"].keys():
                return self.result_data["word2vec"][key]
        
#         print(keys)
        return None    
    
    def read_data(self, data_file, label_file, name=None):    
        assert name != None
        _data = self._read_data(data_file)
        _label = self._read_label(label_file)
        self.result_data[name] = [_data, _label]
        return [_data, _label]
    
    
    def next_batch(self, batch_size=64, name=None):
        assert self.count_test != None and self.count_train != None and name != None
        
#         count = 0
        if name == "train":
            count = self.count_train
        elif name == "test":
            count = self.count_test
#             print("train")
#             start = self.count_train * batch_size<len()
        end = (count + 1) * batch_size
        if end > len(self.result_data[name][0]):
            end = len(self.result_data[name][0])
        
        start = count * batch_size
#         print(start,end,self.count_train)
        
        
        count += 1
#             print(len(self.result_data[name][1]))
        count = count % (len(self.result_data[name][1]) // batch_size + 1)
        __data = self.result_data[name][0][start:end]
        __label = self.result_data[name][1][start:end]
        
        if name == "train":
            self.count_train = count
        elif name == "test":
            self.count_test = count 
        
        __res_data = []
        for lines in __data:
#             print(lines)
            tep_data = []
            for _id in lines:
                tt = self.id2Vec(int(_id))
                if type(tt)!=None:
                    tep_data.append(np.array(tt))
            __res_data.append(np.array(tep_data))
            
#         print(__label)
        
        
        return [np.array(__res_data),np.array(__label)]
    def _label2vec(self,number):
        print(len(self.category))
        _res = [0]*len(self.category)
        _res[number-1] = 1
        return np.array(_res)
    
    def _stem(self,word):
        res = []
        nlist = ['a','n','v']
        for i in nlist:
            w_stem=self.lemmatizer.lemmatize(word,i)
            if w_stem not in res:
                res.append(w_stem)
                
        word = word.lower()
        for i in nlist:
            w_stem=self.lemmatizer.lemmatize(word,i)
            if w_stem not in res:
                res.append(w_stem)
                 
        return res
    
    
    def load(self):
        t0 = time.time()
        self.count_test = 0
        self.count_train = 0
        t1 = threading.Thread(target=self._read_pkl, name="id2words",
                              args=("./data/words.pkl", "id2words",))
        t2 = threading.Thread(target=self._read_pkl, name="category",
                              args=("./data/category.pkl", "category",))
        t3 = threading.Thread(target=self._read_pkl, name="word2vec",
                              args=("E:\TensorFlow\wordvectors\CH.Gigaword.300B.300d.pk",
                                    "word2vec",))
        
        t4 = threading.Thread(target=self.read_data, name="read_data",
                              args=("./corpus/train_data.txt", "./corpus/train_label.txt", "train",))
        t5 = threading.Thread(target=self.read_data, name="read_data",
                              args=("./corpus/test_data.txt", "./corpus/test_label.txt", "test",))
        
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        
        print("Consume time ", (time.time() - t0))


if __name__ == "__main__":
    read = Read_Date()
    print("start process ...")
    read.read_raw_data_save2_number()
    print("process successful")
    print("*"*50)
    print("start load ...")
    read.load()
#     需要将names还原成name也就是原型
#     print(read.result_data["word2vec"]['what'])
    
    print(lemmatizer.lemmatize("names"))
    print("load successful")
#     data = read.next_batch(batch_size=32, name="test")
#     data = read.next_batch(batch_size=32, name="test")
#     print(data[0])
#     print(data[1])
    data = read.next_batch(batch_size=8, name="test")
    print(len(data))
    print(len(data[0]))
    print(len(data[0][0]))
    print(len(data[0][2]))
    print(len(data[0][2][1]))
    print(len(data[1]))
    print(len(data[1][2]))
    
    
#     for i in range(5000):
#         data = read.next_batch(batch_size=8, name="test")
#         print("*"*30)
#         print(len(data[0]))
# #         print(data[0])
# #         print(data[1])
# 
#     print(read.id2Vec(3))

