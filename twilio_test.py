from twilio.rest import Client

config = open('config.txt').readlines()
twilio_sid=config[0].rstrip()
twilio_auth_token=config[1]
twilio_from_number=config[2]
twilio_to_number=config[3]

client = Client(twilio_sid, twilio_auth_token)

message = client.messages.create(
                     body="You have a fine bottom",
                     from_=twilio_from_number,
                     to=twilio_to_number
                 )

print(message.sid)