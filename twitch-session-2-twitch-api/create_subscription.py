import os
import requests
import json

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")
broadcaster_user_id = "522799961"
scopes = "user:read:follows"
# for local development you can expose your server with ngrok
callback_url = os.getenv("CALLBACK_URL")

# GET YOUR ACCESS SERVER

response = requests.post(url=
    "https://id.twitch.tv/oauth2/token?"
    f"client_id={client_id}"
    f"&client_secret={client_secret}"
    "&grant_type=client_credentials"
    f"&scope{scopes}"
)

data = json.loads(response.content)
access_token = data.get("access_token")
print(json.dumps(data, sort_keys=True, indent=4))

# CREATE SUBSCRIPTIONS

response = requests.post(
    url="https://api.twitch.tv/helix/eventsub/subscriptions",
    headers={"Client-ID": client_id, "Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
    json={
        "type": "channel.follow",
        "version": "1",
        "condition": {
            "broadcaster_user_id": broadcaster_user_id
        },
        "transport": {
            "method": "webhook",
            "callback": callback_url,
            "secret": "s3cRe7s3cRe7"
        }
    }
)

print(json.dumps(data, sort_keys=True, indent=4))