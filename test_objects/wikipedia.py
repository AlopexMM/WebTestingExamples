class Wikipedia:

    def __init__(self):

        # Strong tags
        self.strong_english = '//div/a/strong[text()="English"]'
        self.strong_spanish = '//div/a/strong[text()="Español"]'

        # Input tags
        self.input_search_box = '//div/input[@id="searchInput"]'

        self.INIT_PAGE = "https://wikipedia.org"