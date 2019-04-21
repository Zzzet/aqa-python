from pathlib import Path

import json
from src.xml.XmlProcessor import XmlProcessor
from src.util.FileUtils import get_abs_path
from dictdiffer import diff

test_data_path = "samples/xml/test_data.xml"
upd_test_data_path = "samples/json/updated_test_data.json"
control_upd_json_path = "samples/test_resources/xml_tests/updated_test_data.json"
control_upd_xml_path = "samples/test_resources/xml_tests/updated_test_data.xml"
control_orig_json_path = "samples/test_resources/xml_tests/original_test_data.json"


class TestXmlProcessor:
    def setup_method(self, method):
        upd_test_data = Path(get_abs_path(upd_test_data_path))
        if upd_test_data.is_file():
            upd_test_data.unlink()


    def test_input_xml_exists(self):
        upd_test_data = Path(get_abs_path(test_data_path))
        assert upd_test_data.is_file(), "Test xml file should be existing"

    def test_loaded_xml_equal_expected(self):
        xml_as_dict = XmlProcessor(test_data_path) \
            .convert_to_dict().get_as_dict()

        with open(get_abs_path(control_orig_json_path), 'r') as f:
            orig_js = json.load(f)

        result = diff(xml_as_dict, orig_js)
        assert list(result) == [], "Should be no differences between XmlProcessor output dict and control json"

    def test_fields_updated(self):
        xmlproc = XmlProcessor(test_data_path).convert_to_dict()
        self.replace_values(xmlproc)
        test_dict = xmlproc.get_as_dict()

        control_dict = XmlProcessor(control_upd_xml_path) \
            .convert_to_dict().get_as_dict()

        result = diff(test_dict, control_dict)

        assert list(result) == [], "Should be no differences between updated XmlProcessor output and control xml"

    def test_json_file_created(self):
        XmlProcessor(test_data_path) \
            .convert_to_dict() \
            .save_as_json(upd_test_data_path)

        js_file = Path(get_abs_path(upd_test_data_path))
        assert js_file.is_file()

    def test_json_content_correct(self):
        xmlproc = XmlProcessor(test_data_path).convert_to_dict()
        self.replace_values(xmlproc)
        xmlproc.save_as_json(upd_test_data_path)

        with open(get_abs_path(control_upd_json_path), 'r') as f:
            control_js = json.load(f)

        with open(get_abs_path(upd_test_data_path), 'r') as f:
            test_js = json.load(f)

        result = diff(control_js, test_js)
        assert list(result) == [], "Should be no differences between XmlProcessor output and control json"

    def replace_values(self, xmlproc):
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
