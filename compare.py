# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:42:17 2019

@author: admin
"""
import os
import pandas as pd

CA_PATH = r'D:\NewCA\CA'

d = {}

if os.path.exists(CA_PATH):
    for name1 in os.listdir(CA_PATH):
        f1 = os.path.join(CA_PATH, name1)
        name1 = int(name1)
        d[name1] = {}
        for name2 in os.listdir(f1):
            f2 = os.path.join(f1, name2)
            for name3 in os.listdir(f2):
                year = int(name3[5:9])
                if year not in d[name1]:
                    d[name1][year] = set()
                number = int(name3[10:-5])
                #print(name3,number)
                d[name1][year].add(number)
                
for project_year in d:
    total = 0
    for year in d[project_year]:
        total += len(d[project_year][year])
    print('{0}年项目 已做 {1}'.format(project_year,total))
    
    data_path = 'D:\\NewCA\\{0}.xls'.format(project_year)
    gap_path = 'D:\\NewCA\\{0}_gap.txt'.format(project_year)
    df = pd.read_excel(data_path)
    df = df.set_index('序号',drop=False)
    drop_xuhao = []
    for i in range(len(df)):
        yanshou_year = df.iloc[i]['验收年份']
        yanshou_num = df.iloc[i]['验收编号']
        if yanshou_year not in d[project_year].keys():
            continue
        if yanshou_num not in d[project_year][yanshou_year]:
            continue
        drop_xuhao.append(df.iloc[i]['序号'])
    if len(drop_xuhao) != len(df):
        df2 = df.drop(index = drop_xuhao)
        gap_string = ','.join(df2['项目编号'])
        with open(gap_path,'w') as f:
            f.write(gap_string)
    
        
        
            
        
                