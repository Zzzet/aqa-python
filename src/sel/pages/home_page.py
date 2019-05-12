from sel.pages.notification import Notification
from sel.pages.header import Header
from util.driver_container import DriverContainer


class HomePage:

    notification = Notification()
    header = Header()
    def __init__(self):
        self.driver = DriverContainer().get_driver(DriverContainer)

