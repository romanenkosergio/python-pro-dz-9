import os

import phonenumbers
from django.forms import Form, CharField, ValidationError, HiddenInput

from .twilio_client import client


class PhoneNumberForm(Form):
    phone = CharField(label="Please enter your phone number", max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            parsed_number = phonenumbers.parse(phone, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError("Invalid phone number")
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Invalid phone number")
