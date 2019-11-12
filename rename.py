# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:23:33 2019

@author: admin
"""

import shutil
import os

CA_PATH = r'D:\NewCA\CA'
COPY_PATH = r'D:\NewCA\Copy'
WORK_PATH = r'D:\NewCA\Work'
SCRIPT_PATH = r'E:\Anaconda3\Scripts\pdf2txt.py'

if os.path.exists(COPY_PATH):
    shutil.rmtree(COPY_PATH)
    
if os.path.exists(WORK_PATH):
    shutil.rmtree(WORK_PATH)
    
if os.path.exists(CA_PATH):
    shutil.copytree(CA_PATH, COPY_PATH)
    shutil.copytree(CA_PATH, WORK_PATH)
    for name1 in os.listdir(WORK_PATH):
        f1 = os.path.join(WORK_PATH, name1)
        for name2 in os.listdir(f1):
            f2 = os.path.join(f1, name2)
            for name3 in os.listdir(f2):
                f3 = os.path.join(f2, name3)
                outfile = r'D:\NewCA\tmp.txt'
                command = 'python '+ SCRIPT_PATH+ ' -o ' + outfile + ' ' + '"'+f3+'"'
                #print(command)
                os.system(command)
                new_name = None
                with open(outfile, 'r' , encoding='utf-8')  as tmptxt:
                    tmp = tmptxt.readlines()
                    new_name = tmp[6][:-1] + '.pdf'
                f4 = os.path.join(f2, new_name)
                #print(f3,f4)
                os.rename(f3, f4)