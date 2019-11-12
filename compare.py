# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:42:17 2019

@author: admin
"""
import os

CA_PATH = r'D:\NewCA\CA'

d = {}

if os.path.exists(CA_PATH):
    for name1 in os.listdir(CA_PATH):
        f1 = os.path.join(CA_PATH, name1)
        d[name1] = {}
        for name2 in os.listdir(f1):
            f2 = os.path.join(f1, name2)
            for name3 in os.listdir(f2):
                year = name3[5:9]
                if year not in d[name1]:
                    d[name1][year] = set()
                number = int(name3[10:-7])
                d[name1][year].add(number)

for project_year in d:
    for accept_year in d[project_year]:
        with open('{0}_{1}.txt'.format(project_year,accept_year),'w') as f:
            s = d[project_year][accept_year]
            l = list(s)
            all_s = set(range(l[0],l[-1]+1))
            gap_s = all_s - s
            f.write(str(gap_s))


                