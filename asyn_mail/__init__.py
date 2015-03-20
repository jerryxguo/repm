
from django.core.mail import EmailMultiAlternatives
from threading import Thread

class EmailThread(Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, bcc, cc, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.bcc = bcc
       
        self.cc = cc
        self.html = html
        super(EmailThread, self).__init__()

    def run (self):
       
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list,  bcc = self.bcc, cc = self.cc)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)

def send_mail(subject, body, from_email, recipient_list, fail_silently, bcc,  cc, html, *args, **kwargs):
    EmailThread(subject, body, from_email, recipient_list, fail_silently, bcc, cc, html).start()
            

