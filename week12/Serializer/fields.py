from validate_email import validate_email


class Field:
    def transform(self, value):
        return value

    def validate(self, value):
        return False


class CharField(Field):
    def transform(self, value):
        return str(value)

    def validate(self, value):
        return True


class EmailField(CharField):
    def validate(self, value):
        return validate_email(value)


class DateTimeField(Field):
    def transform(self, value):
        return value.isoformat()

    def validate(self, value):
        return True
