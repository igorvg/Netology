import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


# GMAIL_SMTP = "smtp.gmail.com"
# GMAIL_IMAP = "imap.gmail.com"
#
# l = 'login@gmail.com'
# password = 'qwerty'
# subject = 'Subject'
# recipients = ['vasya@email.com', 'petya@email.com']
# message = 'Message'
# header = None


class Email:

    def __init__(self, login, password, GMAIL_SMTP="smtp.gmail.com",
                 GMAIL_IMAP="imap.gmail.com", header=None):

        self.login = login
        self.password = password
        self.header = header
        self.gmail_smtp = GMAIL_SMTP
        self.gmail_imap = GMAIL_IMAP

    def identify(self):

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)

        return ms

    def send_message(self, subject, recipients, message):

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = self.identify()
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def recieve_message(self):

        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return email_message
