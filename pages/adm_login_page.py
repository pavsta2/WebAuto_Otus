"""Модуль методов взаимодействия с элементами страницы авторизации в админку и ее локаторов"""
import os
import allure
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from pages.base_page import BasePage

load_dotenv()


class AdmLoginPage(BasePage):
    AUTH_FORM_TITLE = By.XPATH, "//div[@class='card-header']"
    USERNAME_FLD_TITLE = By.XPATH, "//label[@for='input-username']"
    PASS_FLD_TITLE = By.XPATH, "//label[@for='input-password']"
    USERNAME_FLD = By.NAME, "username"
    PASS_FLD = By.NAME, "password"
    LOGIN_BTN = By.XPATH, "//button[@class='btn btn-primary']"
    USERNAME_IN_HEADER = By.XPATH, "//span[@class='d-none d-md-inline d-lg-inline']"
    LOGOUT_BTN = By.XPATH, "//a[@class='nav-link']"

    @allure.step("Авторизация в админку")
    def login(self):
        self.logger.info('%s: Login administration page' % self.class_name)
        self.fill_the_field(self.USERNAME_FLD, os.getenv("OPENCART_USERNAME"))
        self.fill_the_field(self.PASS_FLD, os.getenv("OPENCART_PASSWORD"))
        # Нажимаем кнопку Login
        self.click_elem(self.LOGIN_BTN)
