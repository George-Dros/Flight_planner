from twilio.rest import Client

account_sid = "YOUR TWILIO ACCOUNT"
twil_token = "YOUR TWILLIO TOKEN"


class NotificationManager:
    def __init__(self):

        self.client = Client(account_sid, twil_token)

    def send_sms(self, message):

        message = self.client.messages.create(
            body=message,
            from_="YOUR TWILLIO FREE PHONE NUMBER",
            to="YOUR PHONE NUMBER"
        )
