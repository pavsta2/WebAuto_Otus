"""Модуль для фикстур и хуков"""
import logging
import datetime
import pytest
from selenium import webdriver
import allure
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
    parser.addoption('--log_level', action='store', default='INFO')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'

@pytest.fixture
def get_base_url(request):
    """Фикстура получения адреса главной страницы"""
    return f"http://{request.config.getoption('--app_url')}"


@pytest.fixture
def get_catalog_url(request):
    """Фикстура получения адреса страницы каталога"""
    return f"http://{request.config.getoption('--app_url')}/en-gb/catalog/desktops"


@pytest.fixture
def get_macbook_card_url(request):
    """Фикстура получения адреса карточки macbook"""
    return f"http://{request.config.getoption('--app_url')}/en-gb/product/desktops/macbook"


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
    log_level = request.config.getoption('--log_level')

    logger = logging.getLogger(request.node.name)
    logfile_handler = logging.FileHandler(f'Logs/{request.node.name}.log')
    logfile_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s %(asctime)s'))
    logger.addHandler(logfile_handler)
    logger.setLevel(log_level)

    logger.info('Test is started at %s' % datetime.datetime.now())

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

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info('Browser %s started for test %s' % (browser_type, request.node.name))

    yield driver
    logger.info('Test is finished at %s' % datetime.datetime.now())

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()
