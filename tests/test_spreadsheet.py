import pyconafrica_tutorial_functions
from pyconafrica_tutorial_functions import get_workbook_data
from openpyxl import Workbook

class TestSpreadsheet(object):
    def test_get_workbook_data_output(self):
        assert isinstance(get_workbook_data('pycon_africa_tutorial.xlsx'), Workbook) 