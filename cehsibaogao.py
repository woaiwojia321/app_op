import unittest
from HTMLTestRunner import HTMLTestRunner
import time
#生成套件
suite=unittest.TestLoader().discover('./',pattern='test_pa*')

# 设置报告路径名及文件名
now=time.strftime('%Y%m%d_%H%M%S')
file_name='./file{}.html'.format(now)

# 写入流
'''stream写入文件流
   verbosity:1简单信息 2详细信息
   

'''
with open(file_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,verbosity=2,
                          title='web 自动化测试',
                          description='系统:win10 浏览器:谷歌 开发语言:Python')
    runner.run(suite)

