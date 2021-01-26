#!/usr/bin/env python
# coding: utf-8

import dask.bag as db


b = db.read_text(['C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg36.txt',
                 'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\4300-0.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg514.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg1497.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg3207.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg6130.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg19033.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\handout\\data\\pg42671.txt']).filter(lambda x: len(str(x)) >= 1)



freqs = b.str.lower().frequencies(sort=True).topk(40, key=1)
freqs.compute()






