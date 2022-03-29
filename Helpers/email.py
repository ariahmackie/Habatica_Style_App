import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, receiver_address, subject, message):
        self.receiver_address = receiver_address
        self.sender_address = "from@example.com"
        self.subject = subject
        self.message = message
        self.setup_mail()

    def setup_mail(self):
        self.setup_mime()
        self.create_smtp_session()

    def setup_mime(self):
        self.mime = MIMEMultipart()
        self.mime['From'] = self.sender_address
        self.password = "1d6c9f3bd096e6"
        self.mime['To'] = self.receiver_address
        self.mime['Subject'] = self.subject
        self.mime.attach(MIMEText(self.message, 'plain'))

    def create_smtp_session(self):
        self.session = smtplib.SMTP('smtp.mailtrap.io', 2525)
        self.session.starttls()
        self.session.login('b6bb29b8c131ee', self.password)
        self.text = self.mime.as_string()

    def send(self):
        self.session.sendmail(self.sender_address, self.receiver_address, self.text)
        self.session.quit()
        print("sent email")
