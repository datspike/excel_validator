import validator.BaseValidator as BaseValidator
from builtins import str


class HeaderValidator(BaseValidator.BaseValidator):
    message = "This value is not equal to described header"

    def validate(self, value):

        # possible null values
        if value is None:
            return False

        value = super(HeaderValidator, self).validate(value)

        if type(value) is str and value == self.header:
            return True
        else:
            return False

    def __init__(self, params):
        super(HeaderValidator, self).__init__(params)
        if 'header' in params:
            self.header = params.get('header')
