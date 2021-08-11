import smtplib

smtpobj=smtplib.SMTP('smtp.gmail.com',587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login('shuklautkarsh73@gmail.com', 'abc')
smtpobj.sendmail('shuklautkarsh73@gmail.com', 'utkarshshukla6373@gmail.com','subject: SMTP check .\n this is test email' )
smtpobj.quit()