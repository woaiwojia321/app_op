# 导包
import unittest
import time


def add(a, b):
    return a + b


# 创建一个测试类
class Test2( unittest.TestCase ):
    def begin_time(self):
        print( '开始时间', time.time() )

    def end_time(self):
        print( '结束时间', time.time() )

    def setUp(self):
        print('准备工作',time.time())

    def tearDown(self):
        print('结束工作',time.time())

    def test_add1(self):
        # self.begin_time()
        result = add( 0, 1 )
        print( '这是第一个', result )
        # self.end_time()

    def test_add2(self):
        # self.begin_time()
        result = add( 0, 2 )
        print( '这是第二个', result )
        # self.end_time()


if __name__ == '__main__':
    unittest.main()
