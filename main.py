import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'John Reynolds'
email['to'] = 'email@gmail.com'
email['subject'] = 'Testing Bot'

email.set_content(html.substitute({'name': 'John'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('username', 'password')
  smtp.send_message(email)

