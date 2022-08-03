from urllib import response
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def getOTP():
    import random
    otp = random.randint(100000, 999999)
    return otp
def email():
        subject = 'Thank you for working'
        message = 'Hi Meena '+str(getOTP())+' is your OTP'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['nishukolimi04@gmail.com',]
        try:
            send_mail( subject, message, email_from, recipient_list )     
        except Exception as e:
            print(e)

