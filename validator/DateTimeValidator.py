import validator.BaseValidator as BaseValidator
from datetime import datetime
from builtins import str

class DateTimeValidator(BaseValidator.BaseValidator):

    message = "This value is not valid datetime"
    format = None  # should be an strptime date format "%Y-%m-%d"

    def validate(self, value):

        #possible null values
        if value is None:

            return True

        value = super(DateTimeValidator, self).validate(value)

        if type(value) is datetime:
            try:
                value = value.strftime(self.format)
            except ValueError:
                
                return False
        try:
            if type(value) is str:
                datetime.strptime(value, self.format)

                return True

        except ValueError:

            return False

        return False

    def __init__(self, params):
        super(DateTimeValidator, self).__init__(params)
        if 'format' in params:
            self.format = params.get('format')
        else:
            self.format = "%Y-%m-%d"
