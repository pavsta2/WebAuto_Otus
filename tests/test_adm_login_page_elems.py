"""Модуль проверок наличия элементов на странице авторизации в админку"""
from pages.adm_login_page import AdmLoginPage


class TestAdminLoginPage:
    """Проверки страницы авторизации в админку"""
    def test_window_title(self, browser, get_auth_admin_url):
        """Проверка заголовка страницы авторизации в админку"""
        browser.get(get_auth_admin_url)
        assert browser.title == 'Administration'

    def test_title_auth(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка формы авторизации и его текста"""
        browser.get(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.AUTH_FORM_TITLE)
        assert el.text == 'Please enter your login details.'

    def test_username_fld_title(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка поля юзернейма и его текста"""
        browser.get(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.USERNAME_FLD_TITLE)
        assert el.text == 'Username'

    def test_pass_fld_title(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка поля пароля и его текста"""
        browser.get(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.PASS_FLD_TITLE)
        assert el.text == 'Password'

    def test_username_fld(self, browser, get_auth_admin_url):
        """Проверка наличия поля ввода юзернейма и его плейсхолдера"""
        browser.get(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.USERNAME_FLD)
        assert el.get_attribute('placeholder') == 'Username'

    def test_pass_fld(self, browser, get_auth_admin_url):
        """Проверка наличия поля ввода пароля и его плейсхолдера"""
        browser.get(get_auth_admin_url)
        el = AdmLoginPage(browser).get_element(AdmLoginPage.PASS_FLD)
        assert el.get_attribute('placeholder') == 'Password'
