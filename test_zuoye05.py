import  unittest
from selenium import webdriver
import time
class TestTPShopLogin(unittest.TestCase):
    '''定义一个tpshop登录测试类'''
    def setUp(self):
        '''定义工作准备'''
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.now=time.strftime('%Y%m%d_%H%M%S')

    def tearDown(self):
        '''定义工作结束'''
        time.sleep(2)
        self.driver.quit()
    def test_login(self):
        '''测试操作'''
        self.driver.find_element_by_link_text( '登录' ).click()
        self.driver.find_element_by_id( 'username' ).send_keys( '13112112112' )
        self.driver.find_element_by_id( 'password' ).send_keys( '123456' )
        self.driver.find_element_by_name( 'sbtbutton' ).click()
        mgs = self.driver.find_element_by_css_selector( '.layui-layer-content' ).text
        print( mgs )
        '''断言'''
        try:
            self.assertIn('验证码为空',mgs)
        except AssertionError as e:
            self.driver.get_screenshot_as_file('./_{}_{}.png'.format(self.now,e))
            raise e

if __name__=='__main__':
    unittest.main()