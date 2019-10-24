#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2019-10-24 15:44
# @Author : Ethan
# @Email : yantan@bit.edu.cn
# @File : f1.py
from sklearn.metrics import precision_recall_fscore_support
import numpy as np

label_map = {'__label__T': 0, '__label__F': 1}

with open('result_tf.txt') as f:
    preds = f.read().split('\n')
    preds = list(filter(None, preds))
    preds = list(map(lambda i: label_map[i], preds))

with open('personality_tf.test') as f:
    labels = [line.split(' ')[0] for line in f.read().split('\n') if line]
    labels = list(map(lambda i: label_map[i], labels))

p, r, f, _ = precision_recall_fscore_support(labels, preds,
                                             beta=1,
                                             average='binary',
                                             warn_for=('f-score',))

preds = np.array(preds)
labels = np.array(labels)
acc = (preds == labels).mean()

print(acc, p, r, f)
