from core import settings
class Twitter:

    def __init__(self):
        """
        Objects for Twitter tests
        """
        self.USER = settings.env('TWITTER_USER')
        self.PASSWORD = settings.env('TWITTER_PASSWORD')