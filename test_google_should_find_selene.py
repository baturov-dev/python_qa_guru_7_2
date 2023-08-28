from selene import browser, be, have


def test_search_result(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_invalid_search_result(open_google):
    browser.element('[name="q"]').should(be.blank).type('uiuiuiuiuiuiuiuiuiiuuuiuuuu').press_enter()
    browser.element('[id="result-stats"]').should(have.text("Результатов: примерно 0"))