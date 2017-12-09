
# -*- coding: utf-8 -*-

import re
import pandas as pd
from gensim import models, corpora
import sys
import os
import glob

SCRIPT_DATA_DIR = './917/'
CHAR_DATA_DIR = './test_file/'
INDEX_DATA_DIR = './classify_novel/917.txt'


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

    #print(str(result_index).decode("string-escape"))
    #print(str(result_text).decode("string-escape"))
    return result_text, result_index, file_path


def main():

        r_t, r_i, file_path = make_train_file(CHAR_DATA_DIR)
        sentences = LabeledListSentence(r_t, r_i)
        model = models.Doc2Vec(alpha=0.025, min_count=5,
                               size=100, iter=20, workers=4)

        model.build_vocab(sentences)
        model.train(sentences, total_examples=sum([len(w) for w in file_path]), epochs=model.iter)
        model.save('./data/doc2vec.model')
        model = models.Doc2Vec.load('./data/doc2vec.model')

        x = '僕'
        print(model.most_similar(positive=[x]))


if __name__ == '__main__':

    main()
