def text_should_be(element, text_to_test):
    assert text_to_test == element.text

def should_be_under(should_be_up, should_be_under):
    assert should_be_up.location['y'] < should_be_under.location['y']

def url_should_be(driver, url_to_test):
    assert url_to_test == driver.current_url

def title_should_be(driver, title_to_test):
    assert title_to_test == driver.title

def should_be_displayed(element):
    assert element.is_displayed()

def should_be_clickable(element):
    assert element.is_enabled()

def placeholder_should_be(element, expected_value):
    assert element.get_attribute('placeholder') == expected_value