

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

    path = ['/Users/masaaki/Downloads/917/13_14563.html.csv',
            '/Users/masaaki/Downloads/917/158_15132.html.csv',
            '/Users/masaaki/Downloads/917/43751_27955.html.csv',
            '/Users/masaaki/Downloads/917/65_14907.html.csv',
            '/Users/masaaki/Downloads/917/3224_20895.html.csv',
            '/Users/masaaki/Downloads/917/46922_33262.html.csv',
            '/Users/masaaki/Downloads/917/2368_13456.html.csv',
            '/Users/masaaki/Downloads/917/2326_13463.html.csv',
            '/Users/masaaki/Downloads/917/2323_13460.html.csv',
            '/Users/masaaki/Downloads/917/3784_27297.html.csv'
            ]

    for i in range(len(path)):
        convert_file(path[i])


if __name__ == '__main__':

    main()
