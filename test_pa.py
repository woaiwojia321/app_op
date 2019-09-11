import unittest
from parameterized import parameterized


def add(a, b):
    return a + b

def add_data():
    return [[0,0,0],[0,1,1],[1,1,2]]

# class Test_add(unittest.TestCase):
#     def test_add01(self):
#         add_date=[(0,0,0),(0,1,1),(1,1,2)]
#         for x,y,z in add_date:
#             result=add(x,y)
#             self.assertEqual(z,result)

class Test_Pa01( unittest.TestCase ):
    # @unittest.skip('这个方法也跳过')
    @parameterized.expand( [(1, 1, 2), (2, 2, 3), (1, 2, 3)] )
    def test_add001(self, x, y, expect):
        result = add( x, y )
        self.assertEqual( expect, result )
        print( '这是结果', result )


class Test_Pa02(unittest.TestCase):
    test_date=[[0,0,0],[0,1,1],[1,1,2]]
    @parameterized.expand(test_date)
    def test_addpa(self,x,y,expect):
        result=add(x,y)
        self.assertEqual(expect,result)
        print(result)
# @unittest.skip('跳过此类')
class Test_Pa03(unittest.TestCase):

    @parameterized.expand(add_data)
    def test_addpa(self,x,y,expect):
        result=add(x,y)
        self.assertEqual(expect,result)
        print(result)







if __name__ == '__main__':
    unittest.main()
