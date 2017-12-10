
import pandas as pd
import glob
import os

DATA_DIR = './917/'
DATA_DIR2 ='/Users/masaaki/env1/bin/info_test4_toma/keisokaiseki/917/'

def convert_file(f):

    result = []
    file1 = open(f, 'r')
    for i in file1:
        i.strip('')
        row = i.split(',')
        result.append(row[0])


    name = f.split('/')
    rename = name[-1].split('.')

    new_file1 = open('test_file_'+rename[0]+'.txt', 'w')
    new_file1.write("\n".join(result))

    file1.close()
    new_file1.close()


def main():

    
    source_path  = glob.glob(os.path.join(DATA_DIR2,'*.csv'))
    print(soruce_path)
    for i in range(len(source_path)):
        convert_file(source_path[i])


if __name__ == '__main__':

    main()
