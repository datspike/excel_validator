from openpyxl.utils.datetime import from_excel
from past.builtins import long


import validator.DateTimeValidator as DateTimeValidator

class ExcelDateValidator(DateTimeValidator.DateTimeValidator):

    def validate(self, value):

       if isinstance(value, long):
           value = from_excel(value)

       return DateTimeValidator.DateTimeValidator.validate(self, value)

    def __init__(self, params):
        super(ExcelDateValidator, self).__init__(params)
