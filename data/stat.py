#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time : 2019-10-23 17:52
# @Author : Ethan
# @Email : yantan@bit.edu.cn
# @File : stat.py

with open('cyberbullying/test.txt') as f:
    lines = f.read().split('\n')
    tags, texts = zip(*[line.split("\t") for line in lines])
    print(f'total train examples: {len(lines)}\n')
    pos_num = len([tag for tag in tags if tag == "I"])
    nev_num = len(lines) - pos_num
    print(f'pos_num: {pos_num}, nev_num: {nev_num}\n')
    lens = [len(line.split(' ')) for line in texts]
    max_len = max(lens)
    min_len = min(lens)
    avg_len = sum(lens) / len(lens)
    print(f'max_len: {max_len}, min_len: {min_len}, avg_len: {avg_len}\n')
