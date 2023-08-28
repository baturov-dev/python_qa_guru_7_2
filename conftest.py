import pytest
from selene.core.configuration import Config
from selene import browser


@pytest.fixture()
def set_window_size():
    Config.window_width = 1920
    Config.window_height = 1080


@pytest.fixture()
def open_google(set_window_size):
    browser.open('https://google.com')
    yield
    browser.quit()