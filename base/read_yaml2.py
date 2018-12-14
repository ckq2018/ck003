import os

import yaml

class DataRead2():
    def __init__(self, filename):
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    # os.getcwd() + os.sep + "data" + os.sep +

    def read_yaml2(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    list = []
    for data in DataRead2("../data/data_read2.yaml").read_yaml2():
        list.append((data.get("username"), data.get("password")))


    print(list)

