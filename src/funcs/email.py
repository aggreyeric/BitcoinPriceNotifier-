import smtplib
from funcs.bitcoin import callprice


def email_send():
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security which makes the connection more secure
    smtpobj.starttls()
    senderemail_id="sendermail@gmail.com"
    senderemail_id_password="######"
    receiveremail_id="receivermail@gmail.com"
    # Authentication for signing to gmail account
    smtpobj.login(senderemail_id, senderemail_id_password)
    # message to be sent
    message = str(callprice())
    # sending the mail - passing 3 arguments i.e sender address, receiver address and the message
    smtpobj.sendmail(senderemail_id,receiveremail_id, message)
    # Hereby terminate the session
    smtpobj.quit()
    print("Email send successfully")



