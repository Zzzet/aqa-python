from src.sel.pages.notification import Notification
from src.sel.pages.header import Header
from src.util.driver_container import DriverContainer


class HomePage:

    notification = Notification()
    header = Header()
    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

