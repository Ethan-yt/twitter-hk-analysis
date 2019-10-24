#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2019-10-23 17:52
# @Author : Ethan
# @Email : yantan@bit.edu.cn
# @File : stat.py

with open('personality_tf.train') as f:
    lines = f.read().split('\n')
    tags = [line.split(" ")[0] for line in lines]
    pos_num = len([tag for tag in tags if tag == "__label__T"])
    nev_num = len(lines) - pos_num
    print(f'pos_num: {pos_num}, nev_num: {nev_num}\n')
