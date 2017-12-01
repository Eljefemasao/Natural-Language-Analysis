
import os


def convert_file(f):

    result = []
    file1 = open(f, 'r')
    for i in file1:
        i.strip('')
        row = i.split(',')
        result.append(row[0])
    print(str(result).decode("string-escape"))

    name = f.split('/')
    rename = name[-1].split('.')

    new_file1 = open('test_file_'+rename[0]+'.txt', 'w')
    new_file1.write("\n".join(result))

    file1.close()
    new_file1.close()


def main():

    path = ['/Users/masaaki/info_test4_toma/keisokaiseki/917/bokuha.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/jimokuki.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/jixtuponnnohari.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/jyujyunokotoba.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/jyujyunokotoba2.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/kaigara.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/karuizawade.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/kujyaku.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/orokanaotokonohanashi.csv',
            '/Users/masaaki/info_test4_toma/keisokaiseki/917/seiganhakutou.csv'
            ]

    for i in range(len(path)):
        convert_file(path[i])


if __name__ == '__main__':

    main()
