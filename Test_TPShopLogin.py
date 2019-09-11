import unittest
from selenium import webdriver
import time


class Test_TPShopLogin( unittest.TestCase ):
    """登录模块测试类"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get( 'http://localhost/' )
        self.driver.maximize_window()
        self.driver.implicitly_wait( 10 )

    def tearDown(self):
        time.sleep( 3 )
        self.driver.quit()

    def test_login(self):

        self.driver.find_element_by_link_text( '登录' ).click()
        self.driver.find_element_by_id( 'username' ).send_keys( '13112112112' )
        self.driver.find_element_by_id( 'password' ).send_keys( '123456' )
        self.driver.find_element_by_name( 'sbtbutton' ).click()
        mgs = self.driver.find_element_by_css_selector( '.layui-layer-content' ).text

        # mgs= self.driver.find_element_by_class_name('layui-layer-content').text
        print( mgs )


if __name__ == '__main__':
    unittest.main()
