import allure
from allure_commons.types import LabelType

from data.main_screen import SearchText
from pages.main_page import main_page


@allure.epic("Wiki")
@allure.feature("Поиск")
class TestSearch:
    @allure.story("Поиск статьи")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_search_article(self):
        main_page.skip_onboarding_screen()
        main_page.search_article(SearchText.APPIUM)
        main_page.check_search(SearchText.APPIUM)
