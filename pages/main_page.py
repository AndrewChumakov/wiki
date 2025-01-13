import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class MainPage:
    APP = "org.wikipedia.alpha:id"
    def __init__(self):
        self.onboarding_skip_button = browser.element((AppiumBy.ID, self.APP + "/fragment_onboarding_skip_button"))
        self.search = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        self.search_text = browser.element((AppiumBy.ID, self.APP + "/search_src_text"))
        self.list_item = browser.all((AppiumBy.ID, self.APP + "/page_list_item_title"))
        self.primary_text = browser.element((AppiumBy.ID, self.APP + "/primaryTextView"))
        self.onboarding_forward_button = browser.element((AppiumBy.ID, self.APP + "/fragment_onboarding_forward_button"))
        self.onboarding_done_button = browser.element((AppiumBy.ID, self.APP + "/fragment_onboarding_done_button"))
        self.text_view = browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView"))

    @allure.step("Проверить страницу приветственного экрана")
    def check_onboarding_screen(self, text):
        self.primary_text.should(have.text(text))

    @allure.step("Перейти на следующую страницу приветственного экрана")
    def forward_onboarding_screen(self):
        self.onboarding_forward_button.click()

    @allure.step("Закрыть приветственный экран")
    def done_onboarding_screen(self):
        self.onboarding_done_button.click()

    @allure.step("Проверить открытие страницы поиска")
    def check_main_screen(self,text):
        self.text_view.first.should(have.text(text))

    @allure.step("Пропустить приветственный экран")
    def skip_onboarding_screen(self):
        self.onboarding_skip_button.click()

    @allure.step("Найти статью")
    def search_article(self, text):
        self.search.click()
        self.search_text.type(text)

    @allure.step("Проверить поиск")
    def check_search(self, text):
        self.list_item.should(have.size_greater_than(0))
        self.list_item.first.should(have.text(text))

main_page = MainPage()