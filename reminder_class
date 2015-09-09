from twilio import rest

class Reminder():
    def __init__(self, sid, token, mobile_no, twilio_no, text):
        self.sid = sid
        self.token = token
        self.mobile_no = mobile_no
        self.twilio_no = twilio_no
        self.sms_text = text

    def send_text(self):
        account_sid = self.sid
        auth_token  = self.token
        client = rest.TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(body= self.sms_text,
        to= self.mobile_no,   
        from_= self.twilio_no) 
        print message.sid
