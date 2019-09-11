# import unittest
# from test_case01 import Test1
# from test_case02 import Test2
#
# suite = unittest.TestSuite()
# # 逐类添加单个测试方法
# suite.addTest( Test1( 'test_add1' ) )
# suite.addTest( Test2( 'test_add2' ) )
# # 逐类添加多个测试方法
# suite.addTest( unittest.makeSuite( Test2 ) )
# # 初始化测试执行对象
# runner = unittest.TextTestRunner()
# runner.run( suite )
import unittest
#
# from test_case01 import Test3
#
# suite=unittest.TestSuite()
# suite.addTest(Test3('test_add3'))
# suite.addTest(unittest.makeSuite(Test3))
# runner=unittest.TextTestRunner()
# runner.run(suite)

# import unittest
# discover=unittest.TestLoader().discover('./cases/',pattern='soft*.py')
# discover=unittest.defaultTestLoader.discover('./cases',pattern='soft*.py')
# runner.run(discover)


#  作业 组装测试用例,执行
import unittest

from test_zuoye05 import TestTPShopLogin

suite = unittest.TestSuite()
suite.addTest( TestTPShopLogin( 'test_login' ) )
suite.addTest( unittest.makeSuite( TestTPShopLogin ) )
#  执行测试组件
runner = unittest.TextTestRunner()
runner.run( suite )
mgs=unittest.TestLoader().discover('./cases','sof*')
runner.run(mgs)