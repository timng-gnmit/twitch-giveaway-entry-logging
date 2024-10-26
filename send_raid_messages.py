# for sending post request
import requests
import json

# load bot authorization data
from auth_data import bot_access_token, bot_client_id, user_access_token
'''
includes:
bot_access_token <- bot oAuth code
bot_client_id <- client id
user_access_token <- user access token, currently from Twitch CLI - https://dev.twitch.tv/docs/cli/
                     currently uses scopes channel:read:redemptions user:read:chat user:write:chat openid
'''

# for knowing which streamer to use
from users_info import streamer, user

# for converting to ids
from user2channelid import user2channelid

# for getting the raid messages
from raid_messages import raid_messages

'''
usage:
    send_raid_messages(verbose)
    
    inputs:
        verbose <- optional bool; if True, will print post request response
'''

def send_raid_messages(verbose=False):
    # note that in my implementation of raid_messages.py, all streamer names are not their display names
    # they were all set to lowercase for consistency
    if streamer.lower() in raid_messages.keys():
        messages = raid_messages[streamer.lower()]
        
        if verbose:
            print(messages)
        
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
        
        if type(messages) == list:
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
                
        elif type(messages) == str:
            data = {
                    "broadcaster_id" : str(channel_id),
                    "sender_id" : str(user_id),
                    "message" : messages
                }
            # send the message via post request
            post_response = requests.post(post_url, headers=post_headers, data=json.dumps(data))
            if verbose:
                print(json.loads(post_response.text))
    else:
        # if streamer not found in raid_messages.py, print to console
        print(f"no raid messages for streamer {streamer} found; update raid_messages.py if this is wrong")
        
    print("done")