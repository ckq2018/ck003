import os


class ReadTxt():
    def __init__(self, filename):
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    # os.getcwd() + os.sep + "data" + os.sep +
    def read_txt(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            list = []
            for data in f.readlines():
                list.append(data.strip().split("/"))
            return list

if __name__ == '__main__':
    # print(ReadTxt("../data/data.txt").read_txt())
    # a = ReadTxt("../data/data.txt").read_txt()
    # print(tuple(a[0]))
    # print(tuple(a[1]))

    for datas in ReadTxt("../data/data.txt").read_txt():
        print(datas)