from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 미라는 멋진 to-do 서비스가 있다는 것을 듣고 사이트에 방문 하였다.
        self.browser.get('http://localhost:8000')

        # 그녀는 메인 페이지 제목이 to-do lists 라는 것을 확인 했다.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


        # 그녀는 to-do item 을 선택했다.
        # ....




if __name__ == '__main__':
    unittest.main(warnings='ignore')


