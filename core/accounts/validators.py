from django.core.exceptions import ValidationError
import re

def validate_iranian_cellphone_number(value):
    pattern_local = r'^09\d{9}$'
    pattern_international = r'^\+989\d{9}$'

    if not re.match(pattern_local, value) and not re.match(pattern_international, value):
        raise ValidationError('Enter a valid Iranian cellphone number.')

    if re.match(pattern_local, value):
        return

    if re.match(pattern_international, value):
        return
