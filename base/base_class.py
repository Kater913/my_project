from datetime import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """ Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url:  ' + get_url)

    """ Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    """ Method assert word in str"""
    def assert_word_in_str(self, word, result):
        value_word = word.text
        assert result in value_word
        print('Good value str')

    """ Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot("/home/e.glushanina/PycharmProjects/my_project/screen/" + name_screenshot)

    """ Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Correct url')
