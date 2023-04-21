from core.webTestObject import WebTestObject


class EnglishStrong(WebTestObject):
    def __init__(self):
        super().__init__(xpath='//div/a/strong[text()="English"]')


class SpanishStrong(WebTestObject):
    def __init__(self):
        super().__init__(xpath='//div/a/strong[text()="Español"]')


class SearchInputBox(WebTestObject):
    def __init__(self):
        super().__init__(xpath='//div/input[@id="searchInput"]')