import os

import yaml


class BaseYaml():
    def __init__(self, filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+ filename

    # os.getcwd() + os.sep + "data" + os.sep +
    def base_yaml(self):

        with open(self.filename, "r", encoding="utf_8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    print(BaseYaml("../data/data_read.yaml").base_yaml())
