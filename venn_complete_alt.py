#!/usr/bin/env python3

import csv,sys,os
import argparse
from collections import defaultdict

#Arguments entry
def GetParams(string,list):
	i = list.index(string)
	return list[i+1]

cmds = sys.argv()

try:
    if "-h" not in cmds:
        in_file = GetParams("-file",cmds)
        if not os.path.isfile(in_file):
            print("Arquivo de entrada não existente")
            sys.exit(0)
        out_dir = GetParams("-dir",cmds)
        if out_dir[-1] == '/':
            out_dir = out_dir[:-1]
        elif out_dir[-1] == '.':
            out_dir = os.getcwd()
        elif not os.path.isdir(out_dir):
            print("Diretório de saída não existente")
            sys.exit(0)
    elif "-h" in cmds:
        print("help")
except:
    print(
"""
Error: 
please use 'venn_complete.py (-s | -g) -file input_file -dir output_directory'
-s for SaturnV file or -g for GenaAPI file""")
    sys.exit(0)


def saturnv(): 
    index = 0
    num = 0
    with open(in_file) as tsv_read:
        csv_reader = csv.reader(tsv_read, delimiter='\t')        
        for row in csv_reader:
            if num == 0:
                while index < len(row):
                    row[index] = row[index].replace('#', '')
                    row[index] = row[index].replace('.faa', '')
                    globals()[f'f{index}'] = open(f"{out_dir}/gene_presence_{row[index]}.txt", "w+")
                    index += 1
                num += 1
                index = 0
            elif num >= 1:
                while index < len(row):
                    if row[index] != '-':
                        globals()[f'f{index}'].write(f'x{num}\n')
                    index += 1    
                num += 1    
                index = 0

def genapi():
    index = 0
    num = 0
    with open(in_file) as tsv_read:
        csv_reader = csv.reader(tsv_read, delimiter='\t')        
        for row in csv_reader:
            if num == 0:
                while index < len(row):
                    globals()[f'f{index}'] = open(f"{out_dir}/gene_presence_{row[index]}.txt", "w+")
                    index += 1
                num += 1
                index = 1
            elif num >= 1:
                while index < len(row):
                    if row[index] == '1':
                        globals()[f'f{index}'].write(f'x{num}\n')
                    index += 1    
                num += 1
                index = 1

if csatv:
    saturnv()
elif cgenapi:
    genapi()