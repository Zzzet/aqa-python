import allure
import requests
import logging


class JiraResource:
    default_auth = None
    url = "https://jira.hillel.it"
    api_endpoint = "/rest/api/2"

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.auth = self.default_auth
        self.response = None
        self.status_code = None

    @staticmethod
    def set_basic_auth(cls, auth):
        cls.default_auth = auth

    @allure.step
    def post(self):
        self.logger.info('post() %s, json_model: %s', self.resource, self.json_model)
        r = requests.post(self.url + self.api_endpoint + self.resource,
                          auth=self.auth,
                          json=self.json_model)
        self.parse(r)
        return self

    @allure.step
    def put(self):
        self.logger.info('put(): %s, json_model: %s', self.resource, self.json_model)
        r = requests.put(self.url + self.api_endpoint + self.resource + "/" + self.key,
                         auth=self.auth,
                         json=self.json_model)
        self.parse(r)
        return self

    @allure.step
    def get(self):
        self.logger.info('get(): %s, json_model: %s', self.resource, self.json_model)
        r = requests.get(self.url + self.api_endpoint + self.resource + "/" + self.key,
                         auth=self.auth)

        self.parse(r)
        return self

    def parse(self, r):
        pass
