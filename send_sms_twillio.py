from twilio.rest import TwilioRestClient

account_sid = "ACb0ff49f0211fe5df0eb1e3e4bf6c48f8" # Your Account SID from www.twilio.com/console
auth_token  = "ad20a0acdbf2888844c9e0a2d43b738c"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+19717082510",    # Replace with your phone number
    from_="+12292990002") # Replace with your Twilio number

print message.sid