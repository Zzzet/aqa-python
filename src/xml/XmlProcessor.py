import json
from src.util.FileUtils import get_abs_path
from pathlib import Path
import xmltodict


class XmlProcessor:
    filename = None
    document = None

    def __init__(self, file_name):
        self.filename = file_name

    def convert_to_dict(self):
        full_path = get_abs_path(self.filename)
        with open(full_path) as fd:
            self.document = xmltodict.parse(fd.read())
            return self

    def replace(self, old_value, new_value):
        for k, v in self.document.items():
            self._replace(self.document[k], old_value, new_value)

    def _replace(self, sub_doc, old_value, new_value):
        if isinstance(sub_doc, dict):
            for k, v in sub_doc.items():
                if v == old_value:
                    sub_doc[k] = new_value
                self._replace(sub_doc[k], old_value, new_value)
        if isinstance(sub_doc, list):
            for list_el in sub_doc:
                self._replace(list_el, old_value, new_value)

    def get_as_dict(self):
        return self.document

    def save_as_json(self, path):
        as_js = json.dumps(self.document)
        with open(get_abs_path(path), "w") as fd:
            fd.write(as_js)


def main():
    xmlproc = XmlProcessor("samples/xml/test_data.xml").convert_to_dict()
    xmlproc.replace("YOUR_FIRST_NAME", "fname")
    xmlproc.replace("YOUR_LAST_NAME", "lname")
    xmlproc.replace("YOUR_YYYY", "1000")
    xmlproc.replace("YOUR_Month", "april")
    xmlproc.replace("YOUR_DD", "1")
    xmlproc.replace("YOUR_COMPANY", "qwertuy")
    xmlproc.replace("YOUR_PROJECT", "sdgfdfg")
    xmlproc.replace("YOUR_ROLE", "adadad")
    xmlproc.replace("YOUR_ROOM", "1087")
    xmlproc.replace("YOUR_HOBBY", "AAZ")
    updated = xmlproc.get_as_dict()
    xmlproc.save_as_json("samples/json/updated_test_data.json")


if __name__ == "__main__":
    main()
