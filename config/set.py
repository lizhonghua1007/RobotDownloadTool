__auther__="李中华"
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# TEST_CONFIG = os.path.join(BASE_DIR,"config","config.ini")

# # 打包exe时，弃用。打包exe之后，把exe拷到根目录下
# BASE_DIR = os.path.dirname(os.getcwd())
# 程序运行时
BASE_DIR = os.getcwd()
TEST_CONFIG = os.path.join(BASE_DIR,"config","config.ini")
logoImage = os.path.join(BASE_DIR,'image','logo.png')
# print(BASE_DIR)
# print(TEST_CONFIG)

