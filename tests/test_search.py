import allure
from allure_commons.types import LabelType
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic("Wiki")
@allure.feature("Поиск")
class TestSearch:
    @allure.story("Поиск статьи")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_search_article(self):
        with allure.step("Пропуск приветственного экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

        with allure.step("Поиск"):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")

        with allure.step("Проверить поиск"):
            browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).should(have.size_greater_than(0))
            browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).first.should(have.text("Appium"))
