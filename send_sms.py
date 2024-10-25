import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='atsk_1d5f8863882955d8435ece0a0ea5f96166e2d49189a4fa118136cd8cf0ae502592484228'
)

sms = africastalking.SMS

class send_sms():

    def send(self):
        #TODO: Send message
        def sending(self):
            # Set the numbers in international format
            recipients = ["+256758831249"]
            # Set your message
            message = "Hey AT Ninja!";
            # Set your shortCode or senderId
            sender = "765839"
            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')
