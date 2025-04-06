# for sending post request
import requests
import json

# for knowing which streamer to use
from users_info import streamer, user

# for converting to ids
from user2channelid import user2channelid

'''
usage:
    send_arson_messages(verbose)
    
    inputs:
        verbose <- optional bool; if True, will print post request response
'''

def send_arson_messages(bot_access_token, bot_client_id, user_access_token, verbose=False):
    post_url = 'https://api.twitch.tv/helix/chat/messages'
    post_headers = {"Authorization": "Bearer " + user_access_token,
                    "Client-Id" : bot_client_id,
                    "Content-Type" : "application/json"}
    # get ids
    users_list = [streamer, user]
    twitch_ids = user2channelid(users_list, bot_access_token, bot_client_id)

    # save them to local variables
    channel_id = twitch_ids[streamer]
    user_id = twitch_ids[user]

    messages = [
        "TwitchLit CurseLit TwitchLit",
        "CurseLit TwitchLit CurseLit"
        ]
    
    for message in messages:
        data = {
                    "broadcaster_id" : str(channel_id),
                    "sender_id" : str(user_id),
                    "message" : message
                }
        # send the message via post request
        post_response = requests.post(post_url, headers=post_headers, data=json.dumps(data))
        if verbose:
            print(json.loads(post_response.text))

    print("🔥")