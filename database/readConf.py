import configparser as cparser
from config import set

'''读取config.ini配置文件，并根据配置文件中的动作，以字典的方式返回参数'''
class ReadIni:
    #fine为config.ini配置文件，option为动作
    def __init__(self,file,option):
        self.file = file
        self.option = option

    def ReadIniFile(self):
        info = dict()
        cf = cparser.ConfigParser()
        cf.read(self.file,'UTF-8')
        keys = cf.options(self.option)
        for key in keys:
            info[key] = cf.get(self.option,key)
        # print(info)
        return info

if __name__ == '__main__':
    ri = ReadIni(set.TEST_CONFIG,'DstSSH')
    ri.ReadIniFile()