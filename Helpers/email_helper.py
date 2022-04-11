"""Module for Sending Emails for Authentication and Updates"""

import sys
import os
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    """To send an email initialize and then use send().
     All other setup is handled during initialization."""

    def __init__(self, receiver_address, subject, message):
        """Inputs: email to send to, the subject (title),
        and the message (body). Calls setup_mail as a side effect"""
        self.receiver_address = receiver_address
        self.sender_address = "from@example.com"
        self.subject = subject
        self.message = message
        self.__setup_mail()

    def __setup_mail(self):
        self.__setup_mime()
        self.__create_smtp_session()

    def __setup_mime(self):
        self.mime = MIMEMultipart()
        self.mime['From'] = self.sender_address
        self.password = "1d6c9f3bd096e6"
        self.mime['To'] = self.receiver_address
        self.mime['Subject'] = self.subject
        self.mime.attach(MIMEText(self.message, 'plain'))

    def __create_smtp_session(self):
        self.session = smtplib.SMTP('smtp.mailtrap.io', 2525)
        self.session.starttls()
        self.session.login('b6bb29b8c131ee', self.password)
        self.text = self.mime.as_string()

    def send(self):
        """Send email. Requires no arguments"""
        self.session.sendmail(self.sender_address, self.receiver_address, self.text)
        self.session.quit()
        print("sent email")
