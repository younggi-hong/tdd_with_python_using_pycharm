
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # mira 는 내용을 입력하지 않고 입력창에서 Enter 를 누른다.
        # 홈 페이지가 리프레쉬 되고 에러 메시지가 출력된다.
        # "아이템은 빈칸일 수 없습니다."
        # 그래서 입력창에 내용을 입력 후 Enter 를 누른다. 정상 동작한다.
        # 다시 두번째 아이템도 빈칸으로 입력한다.
        # 비슷한 경고 메시지가 나타난다.
        # 입력창에 내용을 채우고 Enter 를 누른다.
        # 정상 동작한다.

        self.fail("write me!")
