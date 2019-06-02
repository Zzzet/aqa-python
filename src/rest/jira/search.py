import allure

from src.rest.jira_resource import JiraResource
import requests
import logging


class Search(JiraResource):
    resource = "/search"

    def __init__(self):
        super().__init__()
        self.key = None
        self.response = None
        self.json_model = {
            "startAt": 0,
            "maxResults": 10
        }

    @allure.step
    def set_jql(self, query):
        self.json_model["jql"] = query
        return self

    @allure.step
    def parse(self, r):
        self.status_code = r.status_code
        self.logger.info('response: %s', r.text)
        self.response = r.json()
