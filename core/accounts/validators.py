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

def validate_national_code(value):
    pattern = r'^\d{10}$'
    if not re.match(pattern, value):
        raise ValidationError('کد ملی باید 10 رقم باشد و تنها شامل اعداد باشد.')

    # اعتبارسنجی بر اساس الگوریتم کد ملی ایران
    check_digit = int(value[-1])
    sum_digits = sum(int(digit) * (10 - idx) for idx, digit in enumerate(value[:-1]))
    remainder = sum_digits % 11

    if remainder < 2:
        if check_digit != remainder:
            raise ValidationError('کد ملی معتبر نمی‌باشد.')
    else:
        if check_digit != 11 - remainder:
            raise ValidationError('کد ملی معتبر نمی‌باشد.')
        
def validate_only_letters(value):
    pattern = r'^[a-zA-Zآ-ی\s]+$'
    if not re.match(pattern, value):
        raise ValidationError('این فیلد فقط می‌تواند شامل حروف باشد.')