

# -*- coding: utf-8 -*-

from tqdm import tqdm
import codecs
from gensim import models
import gensim
import os
import glob
import MeCab
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import preprocessing

CHAR_DATA_DIR = './source/'  # Document of Source Book.


class LabeledListSentence(object):
    """
    Tag each document.
    """
    def __init__(self, words_list, labels):
        self.words_list = words_list
        self.labels = labels

    def __iter__(self):
        for i, words in enumerate(self.words_list):
            yield models.doc2vec.LabeledSentence(words, ['%s' % self.labels[i]])


def make_train_file(directory):

    """
    Add source book's document to list respectively.

    :param directory: Directory that Source Book's document which were done morpheme analysis.
    :return:

    result_text : Each documents will be arranged in list. [[910_日本文学],[911_詩歌],[912_戯曲],
    [913_小説],[914_評論/エッセイ/随筆],[915_日記/書簡/紀行],[916_記録/手配/流ポタージュ],[917_箴言],[919_漢詩文/日本漢文学]].

    result_index: List of Source Book's field.

    file_path: List which have Source Book's path (string). Like below.
    ['./source/919.txt','./source/914.txt','./source/915.txt','./source/917.txt','./source/916.txt','./source/912.txt','./source/913.txt','./source/911.txt','./source/910.txt']

    """

    result_text = []
    # This time, Omit 918.
    result_index = ['漢詩文,日本漢文学', '評論,エッセイ,随筆', '日記,書簡,紀行', '箴言', '記録,手記,ルポタージュ', '戯曲', '小説', '詩歌', '日本文学']

    # Get test_data_file's path and connects the all files.
    file_path = glob.glob(os.path.join(directory, '*.txt'))

    # Open each document files and insert into list separately.
    # Finally inset these list into result_text.
    for f_p in file_path:

        with codecs.open(f_p, 'r', 'utf-8') as f:
            for rows in f:
                result = preprocessing.normalize(rows)
                lines = result.split()
                result_text.append(lines)

    return result_text, result_index, file_path


def display_result(model, result_text, result_index):

    """
    :param model: Trained Doc2Vec model which is instance.
    :param result_text: List which is Source Book's document.
    :param result_index: List which is Source Book's field.
    :return:
    Degree of relatedness.
    """

    # Create instance of class "MeCab.Tagger" with system dictionary "mecab-ipadic-neologd".
    mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -Owakati")

    sentences = result_text
    answers = result_index

    # Infer a vector for given post-bulk training document.
    doc_vecs = []
    for sentence in sentences:
        doc_vecs.append(model.infer_vector(sentence))

    while True:
        print("\n")
        print("Please fill in a sentence")
        print("==============================================================================")
        line = input("> ")
        print("==============================================================================")
        print("\n")
        if not line:
            break
        # Convert a Input of sentence into a list of tokens.　
        # After that, turn it for vector processing.
        vec = model.infer_vector(gensim.utils.simple_preprocess(mecab.parse(line), min_len=1))
        # Calculate each document's cosine similarity.
        sims = cosine_similarity([vec], doc_vecs)
        # Re-sort cosine_similarity of each field in ascending order.
        index1 = np.sort(sims[0])
        index = np.argsort(sims[0])
        print(index1)
        # Show each cosine_similarity as bar chart.
        print("")
        for i in range(1, 10):
            print(answers[index[-i]])
            with tqdm(total=100) as pbar:
                for i in range(int(index1[-i] * 1000)):
                    pbar.update(0.1)


def main():

        result_text, result_index, file_path = make_train_file(CHAR_DATA_DIR)
        # Labeling each documents.
        sentences = LabeledListSentence(result_text, result_index)
        # Create model using ‘distributed memory’ (PV-DM)
        model = models.Doc2Vec(alpha=0.025, min_count=5, dm=1,
                               size=300, iter=600, workers=4, window=5)
        # Build vocabulary from a sequence of sentences.
        model.build_vocab(sentences)
        # Train model
        model.train(sentences, total_examples=sum([len(w) for w in file_path]), epochs=model.iter)
        model.save('./data/doc2vec.model')
        model = models.Doc2Vec.load('./data/doc2vec.model')

        display_result(model, result_text, result_index)


if __name__ == '__main__':

    main()
