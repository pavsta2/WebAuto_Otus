"""Модуль для фикстур и хуков"""
import pytest
from selenium import webdriver

from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default="Chrome", help="Which browser to open")
    parser.addoption("--app_url", default='192.168.0.100:8081', help='App base url')
    parser.addoption("--ya_driver", default='/Users/darinastarshinova/yandexdriver',
                     help='Ya driver storage')
    parser.addoption("--headless", action='store_true', help='Headless mode')


@pytest.fixture
def get_base_url(request):
    """Фикстура получения адреса главной страницы"""
    return f"http://{request.config.getoption('--app_url')}"


@pytest.fixture
def get_catalog_url(request):
    """Фикстура получения адреса страницы каталога"""
    return f"http://{request.config.getoption('--app_url')}/en-gb/catalog/desktops"


@pytest.fixture
def get_apple_cinema_card_url(request):
    """Фикстура получения адреса карточки Apple Cinema"""
    return f"http://{request.config.getoption('--app_url')}/en-gb/product/desktops/apple-cinema"


@pytest.fixture
def get_auth_admin_url(request):
    """Фикстура получения адреса авторизации в админку"""
    return f"http://{request.config.getoption('--app_url')}/administration/"


@pytest.fixture
def get_user_reg_url(request):
    """Фикстура получения адреса страницы регистрации юзера"""
    return f"http://{request.config.getoption('--app_url')}/index.php?route=account/register"


@pytest.fixture()
def browser(request):
    driver = None
    driver_storage = request.config.getoption('--ya_driver')
    browser_type = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    if browser_type == 'Chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_type == 'Yandex':
        options = ChromiumOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(
            options=options,
            service=ChromiumService(executable_path=f'{driver_storage}/yandexdriver')
        )
    elif browser_type == 'Firefox':
        options = FFOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Firefox(options=options)
    yield driver

    driver.quit()
