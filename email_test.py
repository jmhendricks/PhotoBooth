from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders

import smtplib
import os

addr_to   = 'specialcodehere@tumblr.com' # The special tumblr auto post email address
addr_from = 'username@gmail.com' # change to your gmail address
user_name = 'username' # change to your gmail username without the @gmail.com
password = 'secretpasswordhere' # your password
file_path = '20140427010031.gif' #the name of the gif to send

msg = MIMEMultipart()
msg['Subject'] = 'photo post via email'
msg['From'] = addr_from
msg['To'] = addr_to

file_path = os.path.join(file_path)
fp = open(file_path, 'rb')
part = MIMEBase('image', 'gif')
part.set_payload( fp.read() )
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_path))
fp.close()
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(user_name, password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print "Email sent succussfully"