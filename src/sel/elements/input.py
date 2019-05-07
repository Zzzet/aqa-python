from sel.elements.base_element import BaseElement


class Input(BaseElement):

    def __init__(self, selector):
        self.selector = selector

    def type(self, text):
        self.wait_until_visible().send_keys(text)
        pass

    def get_text(self):
        return self.wait_until_visible().text