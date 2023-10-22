# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:30:46 2023

@author: wangyilin
"""

import re

def read_lines(file_path):
    #生成迭代器，避免整个文件载入内存，适用于大文件的读写
    with open(file_path, 'r', encoding = 'utf-8') as f:
        for line in f:
            yield line.strip()#迭代器
def write_file(file_path, data_list):
    with open(file_path, 'w', encoding = 'utf-8') as f:
        for item in data_list:
            for data in item[0]:
                f.write(data)
                f.write(" ") 
            f.write('\n')


send1_data = []
send2_data = []

receivea_data = []
receiveb_data = []

for line in read_lines('send1.txt'):
    string = re.findall(r'(\d{6}\.\d{2}),(\d{4}\.\d{8}),([NS]),(\d{5}\.\d{8}),([EW])', line)
    #与字符串匹配的正则表达式，由chatgpt生成
    if string:
        send1_data.append(string)
    
for line in read_lines('send2.txt'):
    string = re.findall(r'(\d{6}\.\d{2}),(\d{4}\.\d{8}),([NS]),(\d{5}\.\d{8}),([EW])', line)
    if string:
        send2_data.append(string)
        
for line in read_lines('receivea.txt'):
    string = re.findall(
        r'(\d{6}\.\d{2}),(\d{4}\.\d{8}),([NS]),(\d{5}\.\d{8}),([EW])', line)
    if string:
        receivea_data.append(string)

for line in read_lines('receiveb.txt'):
    string = re.findall(r'(\d{2}:\d{2}:\d{2}).*?(\d{6}\.\d{2}),(\d{4}\.\d{8}),([NS]),(\d{5}\.\d{8}),([EW])', line)
    if string:
        receiveb_data.append(string)

write_file('./提取好的数据/send1_data.txt', send1_data)         
write_file('./提取好的数据/send2_data.txt', send2_data)                         
write_file('./提取好的数据/receivea_data.txt', receivea_data)         
write_file('./提取好的数据/receiveb_data.txt', receiveb_data)          
