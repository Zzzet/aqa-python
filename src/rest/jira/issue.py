import allure

from src.rest.jira_resource import JiraResource


class Issue(JiraResource):
    resource = "/issue"

    def __init__(self):
        super().__init__()
        self.key = None
        self.json_model = {
            "fields": {
            }
        }

    @allure.step
    def set_project(self, project):
        self.json_model["fields"]["project"] = {"key": project}
        return self

    @allure.step
    def set_issue_type(self, type):
        self.json_model["fields"]["issuetype"] = {"name": type}
        return self

    @allure.step
    def set_summary(self, summary):
        self.json_model["fields"]["summary"] = summary
        return self

    @allure.step
    def set_description(self, description):
        self.json_model["fields"]["description"] = description
        return self

    @allure.step
    def set_assignee(self, assignee):
        self.json_model["fields"]["assignee"] = {"name": assignee}

    @allure.step
    def set_priority(self, priority):
        self.json_model["fields"]["priority"] = {"name": priority}
        return self

    @allure.step
    def parse(self, r):
        self.status_code = r.status_code
        self.logger.info('response: %s', r.text)
        if r.status_code in [200, 201]:
            self.response = r.json()
            self.key = self.response["key"]
