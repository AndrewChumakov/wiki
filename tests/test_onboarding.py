import allure
from allure_commons.types import LabelType
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

@allure.epic("Wiki")
@allure.feature("Приветственный экран")
class TestOnboarding:
    @allure.story("Переход по страницам приветственного экрана")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("NORMAL")
    def test_onboarding(self):
        with allure.step("Открыть приветственный экран"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")). \
                should(have.text("The Free Encyclopedia\n…in over 300 languages"))

        with allure.step("Перейти на вторую страницу приветственного экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")). \
                should(have.text("New ways to explore"))

        with allure.step("Перейти на третью страницу приветственного экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")). \
                should(have.text("Reading lists with sync"))

        with allure.step("Перейти на четвертую страницу приветственного экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")). \
                should(have.text("Data & Privacy"))

        with allure.step("Закрыть приветственный экран"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()

        with allure.step("Проверить открытие страницы поиска"):
            browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).first.should(have.text("Search Wikipedia"))

    @allure.story("Пропуск страницы приветственного экрана")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("NORMAL")
    def test_skip_onboarding(self):
        with allure.step("Пропуск приветственного экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

        with allure.step("Проверить открытие страницы поиска"):
            browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).first.should(have.text("Search Wikipedia"))
