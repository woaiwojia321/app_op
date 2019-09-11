# 导包
import unittest


def add(a, b):
    return a + b


# 创建一个测试类
class Test1( unittest.TestCase ):

    def test_add1(self):
        result = add( 0, 1 )
        print( '这是第一个', result )
        self.assertEqual(result,1)
    def test_add2(self):
        result = add( 2, 2 )
        print( '这是第二个', result )
        self.assertEqual(result,4)

if __name__ == '__main__':
    unittest.main()


# import unittest
# import time
# def setUpModule():
#     print('.....模块开始准备')
#
#
# def tearDownModule():
#     print('.....模块结束工作')

#
# class Test3( unittest.TestCase ):
#     @classmethod
#     def setUpClass(cls):
#         print( '这是类开始准备工作' )
#
#
#
#     def setUp(self):
#         print( '实例对象方法开始' )
#
#     def tearDown(self):
#         print( '实例对象方法结束' )
#
#     def test_add3(self):
#         print( '我是练习用的1' )
#
#     def test_add10(self):
#         print( '这是练习2' )
#     @classmethod
#     def tearDownClass(cls):
#         print( '这是类的结束工作' )
#
# if __name__ == '__main__':
#     unittest.main()
