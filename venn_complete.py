#!/usr/bin/env python3

import csv
import sys
import os
import argparse
from collections import defaultdict

#Arguments entry
parser = argparse.ArgumentParser()
programs = parser.add_mutually_exclusive_group(required=True)

programs.add_argument("-s", "--saturnv", action='store_true', help="Select SaturnV files")
programs.add_argument("-g", "--genapi", action='store_true', help="Select GenAPI files")
parser.add_argument("infile", type= str, help="Entry file")
parser.add_argument("outdir", type=str, help="Directory for output")

args = vars(parser.parse_args())

csatv = args["saturnv"]
cgenapi = args["genapi"]
in_file = args["infile"]
out_dir = args["outdir"]

if not os.path.isfile(in_file):
    print("Arquivo de entrada não existente")

if out_dir[-1] == '/':
    out_dir = out_dir[:-1]
elif out_dir[-1] == '.':
    out_dir = os.getcwd()
elif not os.path.isdir(out_dir):
    print("Diretório de saída não existente")

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