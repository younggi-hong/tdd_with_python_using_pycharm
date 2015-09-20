
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # mira 는 내용을 입력하지 않고 입력창에서 Enter 를 누른다.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # 홈 페이지가 리프레쉬 되고 에러 메시지가 출력된다.
        # "아이템은 빈칸일 수 없습니다."
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 그래서 입력창에 내용을 입력 후 Enter 를 누른다. 정상 동작한다.
        self.get_item_input_box().send_keys("Buy milk\n")
        self.check_for_row_in_list_table('1: Buy milk')

        # 다시 두번째 아이템도 빈칸으로 입력한다.
        self.get_item_input_box().send_keys('\n')

        # 비슷한 경고 메시지가 나타난다.
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 입력창에 내용을 채우고 Enter 를 누른다.
        # 정상 동작한다.
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):

        # mira 는 리스트를 추가한다.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy bread\n')
        self.check_for_row_in_list_table('1: Buy bread')

        # 같은 리스트를 추가한다.
        self.get_item_input_box().send_keys('Buy bread\n')

        # 중복 추가하면 안된다는 메시지를 확인 한다.
        self.check_for_row_in_list_table('1: Buy bread')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")

