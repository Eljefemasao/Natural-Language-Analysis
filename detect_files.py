

# -*- coding: utf-8 -*-

import codecs
from gensim import models
import gensim
from tqdm import tqdm
import os
import glob

import MeCab
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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
    result_index = ['日本文学', '詩歌', '戯曲',  '小説', '評論,エッセイ,随筆', '日記,書簡,紀行', '記録,手記,ルポタージュ', '箴言', '漢詩文,日本漢文学']  #今回918は省きます。

    # gets test_data_file's path and connects the all files.
    file_path = glob.glob(os.path.join(directory, '*.txt'))

    for f_p in file_path:

        with codecs.open(f_p, 'r', 'utf-8') as f:
            for rows in f:
                lines = rows.split()
                result_text.append(lines)

    return result_text, result_index, file_path


def display_result(model, result_index):

    # 入力titleに紐ずけされたdocumentと似たdocumentの類似度を算出しパーセンテージの高いものから表示

    print("\n")

    # detect similar word with its degree of relatedness number.
    char = '僕'
    print("<<Word analyzing about: %s>>" % char)
    print("\n")
    results = model.most_similar(positive=[char])
    print(results)
    for result in results:
        print(result[0])

        with tqdm(total=100) as pbar:
            for i in range(int(result[1] * 1000)):
                pbar.update(0.1)

    print("\n")

    print("\n")

    title = 4
    print("<<Book's title analyzing about: title=%s>>" % result_index[title])

    print("<<Index = %s>>" % result_index)
    results1 = model.docvecs.most_similar(positive=[title])#(positive=[title])
    print(results1)
    for result1 in results1:
        print(result1[0])

        with tqdm(total=100) as pbar:
            for i in range(int(result1[1] * 1000)):
                pbar.update(0.1)

    print("\n")

    final_tuple = results1[0]
    print(final_tuple[0])


def main():

        result_text, result_index, file_path = make_train_file(CHAR_DATA_DIR)
        sentences = LabeledListSentence(result_text, result_index)

        model = models.Doc2Vec(alpha=0.001, min_count=5, dm=1,
                               size=300, iter=600, workers=4, window=5)

        model.build_vocab(sentences)
        #model.train(sentences, total_examples=sum([len(w) for w in file_path]), epochs=model.iter)
        #model.save('./data/doc2vec.model')
        model = models.Doc2Vec.load('./data/doc2vec.model')

        display_result(model, result_index)

        mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -Owakati")

        questions = result_text
        answers = result_index

        doc_vecs = []
        for question in questions:
            doc_vecs.append(model.infer_vector(question))

        while True:
            line = input(">> ")
            if not line:
                break

            vec = model.infer_vector(gensim.utils.simple_preprocess(mecab.parse(line), min_len=1))
            sims = cosine_similarity([vec], doc_vecs)
            index = np.argsort(sims[0])

           # print(questions[index[-1]])
            print()
            print(answers[index[-1]])
            print(sims)
            print()
            print(answers[index[-2]])
            print()
            print()
            print(answers[index[-3]])
            print()
            print()
            print(answers[index[-4]])
            print()


if __name__ == '__main__':

    main()
