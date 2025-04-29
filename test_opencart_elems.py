"""Модуль проверок наличия элементов на страницах Opencart"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestMainPage:
    """Проверки главной страницы"""
    def test_window_title(self, browser, get_base_url):
        """Проверка заголовка окна главной страницы"""
        browser.get(get_base_url)
        assert browser.title == 'Your Store'

    def test_carousel_presence(self, browser, get_base_url):
        """Проверка наличия компонента навигации карусели"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "carousel-indicators")), message='No such element')

    def test_search_field(self, browser, get_base_url):
        """Проверка наличия поискового поля и текста плейсхолдера в нем"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.NAME, "search")), message='No such element')
        assert el.get_attribute('placeholder') == 'Search'

    def test_header_cart_button(self, browser, get_base_url):
        """Проверка наличия кнопки корзины и текста в ней"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header-cart > div > button")),
                        message='No such element')
        assert el.text == '0 item(s) - $0.00'

    @pytest.mark.parametrize('test_button_list',
                             [['Desktops',
                               'Laptops & Notebooks',
                               'Components',
                               'Tablets',
                               'Software',
                               'Phones & PDAs',
                               'Cameras',
                               'MP3 Players']],
                             ids=['valid option list'])
    def test_nav_bar(self, browser, get_base_url, test_button_list):
        """Проверка наличия панели с кнопками каталога и наименований этих кнопок"""
        browser.get(get_base_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-item")),
                        message='No such element')
        tabs_list = []
        for i in el:
            tabs_list.append(i.text)
        assert tabs_list == test_button_list


class TestCatalogDesktopsPage:
    """Проверки страницы каталога Desktops"""
    def test_window_title(self, browser, get_catalog_url):
        """Проверка заголовка окна страницы каталога Desktops"""
        browser.get(get_catalog_url)
        assert browser.title == 'Desktops'

    def test_catalog_title(self, browser, get_catalog_url):
        """Проверка заголовка раздела каталога"""
        browser.get(get_catalog_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2")), message='No such element')
        assert el.text == 'Desktops'

    @pytest.mark.parametrize('test_opt_list',
                             [['Default',
                               'Name (A - Z)',
                               'Name (Z - A)',
                               'Price (Low > High)',
                               'Price (High > Low)',
                               'Rating (Highest)',
                               'Rating (Lowest)',
                               'Model (A - Z)',
                               'Model (Z - A)']],
                             ids=['valid option list'])
    def test_sort_select_field(self, browser, get_catalog_url, test_opt_list):
        """Проверка наличия селект-поля с опциями сортировки и наименования этих опций"""
        browser.get(get_catalog_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.ID, "input-sort")), message='No such element')
        opt_list = []
        for option in Select(el).options:
            opt_list.append(option.text)
        assert opt_list == test_opt_list

    @pytest.mark.parametrize('test_opt_list',
                             [['10',
                               '25',
                               '50',
                               '75',
                               '100']],
                             ids=['valid option list'])
    def test_show_limit_select_field(self, browser, get_catalog_url, test_opt_list):
        """Проверка наличия селект-поля с опциями ограничения кол-ва эл-ов на странице и наименования этих опций"""
        browser.get(get_catalog_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.ID, "input-limit")), message='No such element')
        opt_list = []
        for option in Select(el).options:
            opt_list.append(option.text)
        assert opt_list == test_opt_list

    def test_breadcrumb_bar(self, browser, get_catalog_url):
        """Проверка наличия панели breadcrumb и наименования текущего местоположения (последнего элемента')"""
        browser.get(get_catalog_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "breadcrumb-item")),
                        message='No such element')
        assert el[-1].text == 'Desktops'


class TestProductCard:
    """Проверки страницы карточки товара"""
    def test_window_title(self, browser, get_apple_cinema_card_url):
        """Проверка заголовка страницы карточки товара"""
        browser.get(get_apple_cinema_card_url)
        assert browser.title == 'Apple Cinema 30'

    def test_like_button(self, browser, get_apple_cinema_card_url):
        """Проверка наличия лайк-кнопки и текста его тултипа"""
        browser.get(get_apple_cinema_card_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")),
                        message='No such element')
        assert el.get_attribute('title') == 'Add to Wish List'

    def test_textarea_field(self, browser, get_apple_cinema_card_url):
        """Проверка наличия текстового поля с плейсхолдером Textarea"""
        browser.get(get_apple_cinema_card_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='option[209]']")),
                        message='No such element')
        assert el.get_attribute('placeholder') == 'Textarea'

    def test_add_to_cart_btn(self, browser, get_apple_cinema_card_url):
        """Проверка наличия кнопки добавления в корзину и текста в ней"""
        browser.get(get_apple_cinema_card_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.ID, "button-cart")),
                        message='No such element')
        assert el.text == 'Add to Cart'

    def test_tab_description(self, browser, get_apple_cinema_card_url):
        """Проверка наличия таба с описанием товара и текста заголовка этого таба"""
        browser.get(get_apple_cinema_card_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#tab-description']")),
                        message='No such element')
        assert el.text == 'Description'


class TestAdminLoginPage:
    """Проверки страницы авторизации в админку"""
    def test_window_title(self, browser, get_auth_admin_url):
        """Проверка заголовка страницы авторизации в админку"""
        browser.get(get_auth_admin_url)
        assert browser.title == 'Administration'

    def test_title_auth(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка формы авторизации и его текста"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='card-header']")),
                        message='No such element')
        assert el.text == 'Please enter your login details.'

    def test_username_fld_title(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка поля юзернейма и его текста"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='input-username']")),
                        message='No such element')
        assert el.text == 'Username'

    def test_pass_fld_title(self, browser, get_auth_admin_url):
        """Проверка наличия заголовка поля пароля и его текста"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='input-password']")),
                        message='No such element')
        assert el.text == 'Password'

    def test_username_fld(self, browser, get_auth_admin_url):
        """Проверка наличия поля ввода юзернейма и его плейсхолдера"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.NAME, "username")),
                        message='No such element')
        assert el.get_attribute('placeholder') == 'Username'

    def test_pass_fld(self, browser, get_auth_admin_url):
        """Проверка наличия поля ввода пароля и его плейсхолдера"""
        browser.get(get_auth_admin_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.NAME, "password")),
                        message='No such element')
        assert el.get_attribute('placeholder') == 'Password'


class TestUserRegPage:
    """Проверки страницы регистрации юзера"""
    def test_window_title(self, browser, get_user_reg_url):
        """Проверка заголовка страницы регистрации юзера"""
        browser.get(get_user_reg_url)
        assert browser.title == 'Register Account'

    def test_reg_page_title(self, browser, get_user_reg_url):
        """Проверка наличия заголовка формы регистрации и его текста"""
        browser.get(get_user_reg_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")),
                        message='No such element')
        assert el.text == 'Register Account'

    def test_fname_fld(self, browser, get_user_reg_url):
        """Проверка наличия поля ввода имени и его плейсхолдера"""
        browser.get(get_user_reg_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.NAME, "firstname")),
                        message='No such element')
        assert el.get_attribute('placeholder') == 'First Name'

    def test_lname_fld(self, browser, get_user_reg_url):
        """Проверка наличия поля ввода фамилии и его плейсхолдера"""
        browser.get(get_user_reg_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.NAME, "lastname")),
                        message='No such element')
        assert el.get_attribute('placeholder') == 'Last Name'

    def test_subscribe_chbx(self, browser, get_user_reg_url):
        """Проверка наличия чекбокса подписки"""
        browser.get(get_user_reg_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.ID, "input-newsletter")),
                        message='No such element')
        assert el.get_attribute('type') == 'checkbox'

    def test_continue_btn(self, browser, get_user_reg_url):
        """Проверка наличия кнопки Continue и текста этой кнопки"""
        browser.get(get_user_reg_url)
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        el = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")),
                        message='No such element')
        assert el.text == 'Continue'
