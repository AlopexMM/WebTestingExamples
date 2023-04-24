class WebTestObject:
    """This is the base object for web testing"""
    
    def __init__(self, xpath: str = "", tag: str = "") -> None:
        """
        @rtype: None
        """
        self.xpath = xpath
        self.tag = tag
        return

    def __repr__(self):
        return f"xpath: {self.xpath}, tag: {self.tag}"