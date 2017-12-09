
# -*- coding: utf-8 -*-

import re
import pandas as pd
from gensim import models, corpora
import sys
import os
import glob

DATA_DIR = './917/'


class LabeledListSentence(object):
    def __init__(self, words_list, labels):
        self.words_list = words_list
        self.labels = labels

    def __iter__(self):
        for i, words in enumerate(self.words_list):
            yield models.doc2vec.LabeledSentence(words, ['%s' % self.labels[i]])


def main():

        """
        all_file = [bokuha_char, jimokuki_char, jixtuponnnohari_char, jyujyunokotoba_char, jyujyunokotoba2_char,
                    kaigara_char, karuizawade_char, kujyaku_char, orokanaotokonohanashi_char, seiganhakutou_char]
        """
        files = glob.glob(os.path.join(DATA_DIR, '*.csv'))
        pattern = r'\.\/917\/(.*)\.csv'
        matches = re.finditer(pattern, files[0])
        for match in matches:
            print(match.groups()[0])

        word_list = []
        word_index = []
        df_list = []
        for file in files:
            tmp_df = pd.read_csv(file, header=None, encoding="utf-8")
            tmp_df['filename'] = '917/'+os.path.basename(file).split('.')[0]
            df_list.append(tmp_df)
        df = pd.concat(df_list, ignore_index=True)

        word_list.append(df[0])
        word_index.append(df['filename'])

        sentences = LabeledListSentence(word_list[0], word_index[0])

        model = models.Doc2Vec(alpha=0.025, min_count=5,
                               size=100, iter=20, workers=4)

        #model.build_vocab(sentences)

        #model.train(sentences, total_examples=sum([len(wakati) for wakati in files]), epochs=model.iter)

       # model.save('./data/doc2vec.model')

        model = models.Doc2Vec.load('./data/doc2vec.model')

        word_index[0] = model.docvecs.offset2doctag

        x = u'は'
        print(model.most_similar(positive=[x]))
        #print(str(result).decode("string-escape"))


if __name__ == '__main__':

    main()
