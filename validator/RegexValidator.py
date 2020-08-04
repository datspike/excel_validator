import validator.BaseValidator as BaseValidator
import re
from builtins import str

class RegexValidator(BaseValidator.BaseValidator):

    pattern = None
    message = "This value do not match pattern"

    def validate(self, value):

        #possible null values
        if value is None:
            return True

        value = super(RegexValidator, self).validate(value)
        if type(value) is not str:
            value = str(value)

        if re.match(self.pattern, value):
            return True

        return False

    def __init__(self, params):
        super(RegexValidator, self).__init__(params)

        if 'pattern' in params:
            self.pattern = params.get('pattern').replace('\\\\', '\\')
        else:
            raise ValueError("Missing pattern parameter")
