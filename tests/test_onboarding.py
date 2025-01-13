import allure
from allure_commons.types import LabelType

from data.main_screen import MainText
from data.onboarding_screen import OnboardingText
from pages.main_page import main_page


@allure.epic("Wiki")
@allure.feature("Приветственный экран")
@allure.label(LabelType.TAG, "smoke")
@allure.severity("NORMAL")
class TestOnboarding:
    @allure.story("Переход по страницам приветственного экрана")
    def test_onboarding(self):
        main_page.check_onboarding_screen(OnboardingText.FIRST_SCREEN)
        main_page.forward_onboarding_screen()
        main_page.check_onboarding_screen(OnboardingText.SECOND_SCREEN)
        main_page.forward_onboarding_screen()
        main_page.check_onboarding_screen(OnboardingText.THIRD_SCREEN)
        main_page.forward_onboarding_screen()
        main_page.check_onboarding_screen(OnboardingText.FORTH_SCREEN)
        main_page.done_onboarding_screen()
        main_page.check_main_screen(MainText.SEARCH_TEXT)

    @allure.story("Пропуск страницы приветственного экрана")
    def test_skip_onboarding(self):
        main_page.skip_onboarding_screen()
        main_page.check_main_screen(MainText.SEARCH_TEXT)
