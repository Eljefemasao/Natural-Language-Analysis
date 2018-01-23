
# -*- coding: utf-8 -*-

import re
from gensim import models, corpora
from tqdm import tqdm
import os
import sys
import glob

CHAR_DATA_DIR = './source/'  # Text of Source Book


class LabeledListSentence(object):
    def __init__(self, words_list, labels):
        self.words_list = words_list
        self.labels = labels

    def __iter__(self):
        for i, words in enumerate(self.words_list):
            yield models.doc2vec.LabeledSentence(words, ['%s' % self.labels[i]])


def make_train_file(directory):

    result_text = []
    result_index = [910, 911, 912, 913, 914, 915, 916, 917, 919]  #今回918は省きます。

    # gets test_data_file's path and connects the all files.
    file_path = glob.glob(os.path.join(directory, '*.txt'))

    for f_p in file_path:
        pre_text = []
        with open(f_p, mode='r', encoding='ISO-8859-1') as f:
            for rows in f:
                lines = rows.split(' ')
                pre_text.append(lines)
            result_text.append(pre_text)
    print(result_text)
    return result_text, result_index, file_path, result_index


def display_result(model, result_index):

    field = {910: '日本文学', 911: '詩歌', 912: '戯曲', 913: '小説', 914: '評論,エッセイ,随筆', 915: '日記,書簡,紀行', 916: '記録,手記,ルポタージュ', 917: '箴言', 919: '漢詩文,日本漢文学'}

    # 入力titleに紐ずけされたdocumentと似たdocumentの類似度を算出しパーセンテージの高いものから表示
    title = 5
    print("<<Book's title analyzing about: title=%s>>" % result_index[title])
    print("<<Index = %s>>" % result_index)

    print("\n")
    results1 = model.docvecs.most_similar(positive=[title])
    for result1 in results1:
        print(result1[0])

        with tqdm(total=100) as pbar:
            for i in range(int(result1[1] * 1000)):
                pbar.update(0.1)

    print("\n")

    result_number = 915
    print(field[result_number])


def main():

        r_t, r_i, file_path, result_index = make_train_file(CHAR_DATA_DIR)
        sentences = LabeledListSentence(r_t, r_i)
        model = models.Doc2Vec(alpha=0.025, min_count=5,
                               size=100, iter=20, workers=4)

        model.build_vocab(sentences)
        model.train(sentences, total_examples=sum([len(w) for w in file_path]), epochs=model.iter)
        model.save('./data/doc2vec.model')
        model = models.Doc2Vec.load('./data/doc2vec.model')

        display_result(model, result_index)


if __name__ == '__main__':

    main()
