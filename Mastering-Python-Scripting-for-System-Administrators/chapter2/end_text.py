from twilio.rest import Client

account_sid =
auth_token =
client = Client(account_sid, auth_token)

message = client.sms.messages.create(
    body = "My name is Carol Li",
    to=""
    from_=""
)
print(message.sid)

