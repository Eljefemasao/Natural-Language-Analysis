
# -*- coding: utf-8 -*-

import re
import pandas as pd
from gensim import models, corpora
from tqdm import tqdm
import sys
import os
import glob


SCRIPT_DATA_DIR = './917/'           # Original data which was already handled a monopheme analysis processing.
CHAR_DATA_DIR = './test_file/'       # Single Words data which was extract from original data.
INDEX_DATA_DIR = './classify_novel/917.txt'   # Original data's file name which mean title of book. Number is 10.


class LabeledListSentence(object):
    def __init__(self, words_list, labels):
        self.words_list = words_list
        self.labels = labels

    def __iter__(self):
        for i, words in enumerate(self.words_list):
            yield models.doc2vec.LabeledSentence(words, ['%s' % self.labels[i]])


def make_train_file(d):

    result_text = []
    result_index = []

    # get test_data_file's path and connect the all files.
    file_path = glob.glob(os.path.join(d, '*.txt'))

    for f_p in file_path:
        pre_text = []
        with open(f_p, 'r') as f:
            for rows in f:
                lines = rows.strip()
                pre_text.append(lines)
            result_text.append(pre_text)

    with open(INDEX_DATA_DIR, 'r') as index:
        for row in index:
            line = row.strip()
            result_index.append(line)

    return result_text, result_index, file_path, result_index


def main():

        r_t, r_i, file_path, result_index = make_train_file(CHAR_DATA_DIR)
        sentences = LabeledListSentence(r_t, r_i)
        model = models.Doc2Vec(alpha=0.025, min_count=5,
                               size=100, iter=20, workers=4)

        model.build_vocab(sentences)
        model.train(sentences, total_examples=sum([len(w) for w in file_path]), epochs=model.iter)
        model.save('./data/doc2vec.model')
        model = models.Doc2Vec.load('./data/doc2vec.model')

        # detect similar word with its degree of relatedness number.
        print("\n")

        x = '神経'
        print("<<Word analyzing about: %s>>" % x)
        print("\n")
        results = model.most_similar(positive=[x])
        for result in results:
            print(result[0])

            with tqdm(total=100) as pbar:
                for i in range(int(result[1]*1000)):
                    pbar.update(0.1)

        print("\n")

        # detect similar document with its degree of relatedness number.
        y = 9
        print("<<Book's title analyzing about: Index[%d]>>" % y)
        print("<<Index = %s>>" % result_index)

        print("\n")
        results1 = model.docvecs.most_similar(positive=[y])
        for result1 in results1:
            print(result1[0])

            with tqdm(total=100) as pbar:
                for i in range(int(result1[1]*1000)):
                    pbar.update(0.1)

        print("\n")


if __name__ == '__main__':

    main()
