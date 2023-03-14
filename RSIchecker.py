import time
import requests
import smtplib, ssl


#
#  Replace inside od Quotes. dont add quotes to port number
#

Server_host = "YOUR EMAIL PROVIDER HOST"
sender_email = "SENDER_EMAIL"
receiver_email = "RECIEVER_EMAIL"
port = EMAIL_PORT
app_password = "YOUR EMAIL PASSWORD"


# URL of the website to monitor
url = "https://status.robertsspaceindustries.com/"
url2 = "https://robertsspaceindustries.com/patch-notes"


prev_content = " "

while True:
    try:

        response = requests.get(url)
        content = response.text
    except requests.exceptions.RequestException as e:
        print(e)
        continue

    if content != prev_content:

        message = """\
        From: Star.Citizen.Update@NotRSI.com
        Subject: STAR CITIZEN SERVER STATUS CHANGE

        check https://status.robertsspaceindustries.com/ for current status change

        """

        context = ssl.create_default_context()



        with smtplib.SMTP_SSL(Server_host, port, context=context) as server:
            server.login("YOUR_EMAIL", app_password)
            server.sendmail(sender_email, receiver_email, message)


    # Update the previous content
    prev_content = content


# Patch patch-notes

prev_content2 = " "

    try:
        response = requests.get(url2)
        content = response.text
    except requests.exceptions.RequestException as e:
        print(e)
        continue
    if content2 != prev_content2:
        message2 = """\
        From: Star.Citizen.Update@NotRSI.com
        Subject: STAR CITIZEN SERVER PATCH UPDATE

        check https://robertsspaceindustries.com/patch-notes for current patch update

        """
        context = ssl.create_default_context()


        with smtplib.SMTP_SSL("Server_host", port, context=context) as server:
            server.login("YOUR_EMAIL", app_password)
            server.sendmail(sender_email, receiver_email, message2)


    # Update the previous content
    prev_content2 = content2

    time.sleep(60)
    print("Rechecking")
