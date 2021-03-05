#!/usr/bin/env python3
from collections import Counter
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import csv, os

directory_in = "/home/gs/Documents/projetos/is_finder/arquivos/"
directory = os.fsencode(directory_in)

def main():
    dict_all ={}
    for file in os.listdir(directory):
        file_name = os.fsdecode(file)
        file_basename = file_name.split('.')[0]
        if file_name.endswith(".csv"):
            file_path = directory_in + file_name
            dict_all[file_basename] = get_sums(file_path)
    heatmap(dict_all)

def get_sums(file):
    with open(file, "r") as csv_read:
        in_csv = csv.reader(csv_read, delimiter=";")
        next(in_csv)
        family_list = []
        for row in in_csv:
            family_list.append(row[1])
        family_count = dict(Counter(family_list))
    return family_count

def heatmap(dict_in):
    matrix_pd = pd.DataFrame(dict_in).T.fillna(0)
    plt.figure(figsize=(16, 3.5))
    ax = plt.axes()
    sb.heatmap(matrix_pd, ax=ax, linewidths=0.1)
    ax.set_title('IS Finder $\it{E. coli}$')
    plt.xlabel("Família")
    plt.ylabel("Cepas")
    plt.savefig('is_finder_heatmap_linha.png', bbox_inches='tight')

main()
