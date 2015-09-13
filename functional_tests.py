from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 미라는 멋진 to-do 서비스가 있다는 것을 듣고 사이트에 방문 하였다.
        self.browser.get('http://localhost:8000')

        # 그녀는 메인 페이지 제목이 to-do lists 라는 것을 확인 했다.
        self.assertIn('To-Do', self.browser.title)

        # 헤더 제목을 확인한다.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # to-do 아이템을 확인한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        # text box 에 "Buy milk" 를 입력 한다.
        inputbox.send_keys('Buy milk')

        # enter 를 입력하면, 페이지는 업데이트 되고 "1: Buy milk" 란 to-do 리스트가
        # 생성 된다.
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # "Sing a song" 을 추가한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Sing a song")
        inputbox.send_keys(Keys.ENTER)

        # 등록된 item 을 확인한다.
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Sing a Song')

        self.fail('Finish the test!')




if __name__ == '__main__':
    unittest.main(warnings='ignore')


