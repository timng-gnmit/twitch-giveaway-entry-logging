**Still not figured out:**
- How do I get the user to grant more access to the app? My current idea is to get the user to click on a link, have the link send data to the logging app, and get the auth token from there. I am not sure if this is possible in Jupyter Notebooks.
- How do I deal with session_reconnect messages? This would also get fixed by completely understanding auth tokens, which I do not completely get yet.

# Twitch Giveaway Entry Logging Notebook
The `giveaway_entry_logging.ipynb` notebook was created as a way to automatically log giveaway entries for a Twitch streamer. Initially, I wanted to use pubsub with the `channel:read:redemptions` scope, but that requires the user to also be the streamer. My original intent was to just be able to fire this up as a moderator or even as a viewer so that the streamer doesn't have to worry about logging the entries by themself.

The `user2channelid.py` program is for generating channel ids from usernames. This is only possible through the Twitch API, and there are online services that offer to do this for "free," but I didn't know if they were accurate and they only gave me one try per month. While creating the giveaway entry logging notebook, I decided that it would be useful to figure out how to automatically generate these by myself, and you are free to use it as well.

**Usage**
```
channel_ids = user2channelids(users_list, auth_token, client_id)
	inputs:
		user_list <- list of strings with Twitch usernames
		auth_token <- app auth token from a POST request from https://id.twitch.tv/oauth2/token
		client_id <- unique app client id
	output:
		channel_ids <- dict with {username : channel_id} key-value pairs
```

# .gitignore
Here I will tell you generic contents of the .gitignore files, anonymized so I don't dox myself on Twitch. This is for if you want to use them for your implementation.

## redeems.txt
Contains my personal logs for the redeem collection. Has times, dates, and usernames and is therefore anonymized for privacy.

## auth_data.py
Contains the bot client id `bot_client_id`, client secret `bot_client_secret`, and user access token `user_access_token`. The user access token is generated with Twitch CLI using the command
```twitch token -u -s "channel:read:redemptions user:read:chat user:write:chat openid"```

`auth_data.py` also automatically generates a bot access token `bot_access_token`, used in `user2channelid()`. This is done with the following POST request:
```
bot_post_params = {"client_id" : bot_client_id,
                   "client_secret" : bot_client_secret,
                   "grant_type" : "client_credentials"}

response = requests.post(bot_post_url, data=bot_post_params)
response = response.text
response = json.loads(response)
bot_access_token = response["access_token"]
```

## users_info.py
contains two variables:
```
streamer = streamer_name
user = user_name
```
Note that the capitalization is not important for `users2channelid()`. The API response to the GET request uses a lowercase version of the user's name, so `users2channelid()` automatically lowercases whatever is in this file.

## raid_messages.py
Contains various raid messages in a dictionary `raid_messages`, organized as follows:
```
raid_messages = {
	"streamer1" : ["sub_repeated_raid_message_1 "*3,
		"follower_repeated_raid_message_1 "*3]
	,
	"streamer2" : ["sub_repeated_raid_message_2 "*6,
		"follower_raid_message_2 "]
	...
}
```
The string multiplication after the space would make a raid message such as `I have no raid message!` appear as
`I have no raid message! I have no raid message! I have no raid message!` (hence the space). This is for organizational purposes only. Note that in the example, `streamer2` has a follower raid message with no repeating. This happens sometimes. Finally, `send_raid_messages()` can handle if someone only has one raid message and it is in a string, not a list.

# Final notes
By using any program in this repository, you agree not to cause harm to or harass any Twitch streamers or collect data about them or their streams without their consent.