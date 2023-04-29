from core import settings
class Twitter:

    def __init__(self):
        """
        Objects for Twitter tests
        """

        self.INIT_PAGE = 'https://twitter.com'
        self.USER = settings.env('TWITTER_USER')
        self.PASSWORD = settings.env('TWITTER_PASSWORD')
        self.LOGIN_BUTTON = '//div/span/span[contains(text(), "Iniciar sesión")]'
        self.LOGIN_MODAL_USER_INPUT = '//input[@autocomplete="username"]'
        self.LOGIN_MODAL_NEXT_BUTTON = '//div/span/span[contains(text(), "Siguiente")]'
        self.LOGIN_MODAL_PASSWORD_INPUT = '//input[@autocomplete="current-password" and @name="password"]'
        self.LOGIN_MODAL_LOGIN_BUTTON = '//div[@data-testid="LoginForm_Login_Button"]/div/span/span[text()="Iniciar sesión"]'
        self.LOGIN_MODAL = '//div[@aria-labelledby="modal-header"]'
        self.USER_PORTAL = '//div[@aria-label="Menú de la cuenta"]/div/div/div/div/div/span/span[text()="' + \
                           settings.env('TWITTER_USERNAME') + '"]'
        self.SEARCH_BOX = '//input[@placeholder="Buscar en Twitter"]'
        self.SELENIUM_USER = '//span[text()="@SeleniumHQ"]'
        self.SELENIUM_ABOUT = '//span[text()="Selenium is a browser automation framework and ecosystem for developers and testers."]'
        self.TWEET_BUTTON = '//span[text()="Twittear" or .="Tweet"]'
        self.TWEET_MODAL_TEXTAREA = '//div[@aria-labelledby="modal-header"]//div[@role="textbox" and @aria-label="Texto del Tweet" and @data-testid="tweetTextarea_0"]'
        self.TWEET_MODAL_TWEET_BUTTON = '//div[@aria-labelledby="modal-header"]//span[text()="Twittear"]'
        self.HOME_BUTTON = '//div/span[text()="Inicio"]'
        self.TWEETER_HOME_LINK = 'https://twitter.com/' + settings.env('TWITTER_USER')
        self.TWEET_SECTION = '//section/h1[text()="Tweets de ' + settings.env('TWITTER_USERNAME') + '"]/parent::section'
