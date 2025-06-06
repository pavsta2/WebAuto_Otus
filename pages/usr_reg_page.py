"""Модуль методов взаимодействия с элементами страницы авторизации в админку и ее локаторов"""
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserRegPage(BasePage):
    REG_FORM_TITLE = By.CSS_SELECTOR, "h1"
    FIRSTNAME_FLD = By.NAME, "firstname"
    LASTNAME_FLD = By.NAME, "lastname"
    EMAIL_FLD = By.NAME, "email"
    PASSWORD_FLD = By.NAME, "password"
    SUBSCR_BTN = By.ID, "input-newsletter"
    CONTINUE_BTN = By.XPATH, "//button[@class='btn btn-primary']"
    POLICY_AGREE_BTN = By.XPATH, '//*[@name="agree"]'
    MY_ACCOUNT_BTN = By.XPATH, '//span[contains(text(), "My Account")]'
    MY_ACCOUNT_OPTIONS = By.XPATH, '//*[@class = "dropdown-menu dropdown-menu-right show"]/*'

    @allure.step("Регистрация пользователя {fname} {lname}")
    def reg_user(self, fname: str, lname: str, email: str, password: str):
        self.logger.info('%s: Registrating user (first name: %s, last name: %s)' % (self.class_name, fname, lname))
        self.fill_the_field(self.FIRSTNAME_FLD, fname)
        self.fill_the_field(self.LASTNAME_FLD, lname)
        self.fill_the_field(self.EMAIL_FLD, email)
        self.fill_the_field(self.PASSWORD_FLD, password)
        self.click_elem(self.POLICY_AGREE_BTN)
        self.click_elem(self.CONTINUE_BTN)

    @allure.step("Заполнение полей формы регистрации пользователя {fname} {lname} без сабмита")
    def fill_reg_fields_only(self, fname: str, lname: str, email: str, password: str):
        self.logger.info('%s: Filling reg field only without submiting, user (first name: %s, last name: %s)'
                         % (self.class_name, fname, lname))
        self.fill_the_field(self.FIRSTNAME_FLD, fname)
        self.fill_the_field(self.LASTNAME_FLD, lname)
        self.fill_the_field(self.EMAIL_FLD, email)
        self.fill_the_field(self.PASSWORD_FLD, password)
