import os

from celery import shared_task

from .twilio_client import client


@shared_task
def send_sms_task(phone_number):
    verify_sid = os.environ.get('TWILIO_VERIFY_SID')
    verification = client.verify.v2.services(verify_sid).verifications.create(to=phone_number, channel="sms")
    print(verification.status)