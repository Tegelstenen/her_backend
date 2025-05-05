# Download the helper library from https://www.twilio.com/docs/python/install
import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()  # take environment variables

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to="+46765851105",
    from_="+13412991224",
)

print(call.sid)
