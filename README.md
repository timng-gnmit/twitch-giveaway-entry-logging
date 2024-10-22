**Still not figured out:**
- How do I get the user to grant more access to the app? My current idea is to get the user to click on a link, have the link send data to the logging app, and get the auth token from there. I am not sure if this is possible in Jupyter Notebooks.
- How do I deal with session_reconnect messages? This is would also get fixed by completely understanding auth tokens, which I do not completely get yet.

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

# Final notes
Yes, the current implementation could be done with an IRC connection, but those are significantly more limited and will never be able to read channel redemptions.

By using any program in this repository, you agree not to cause harm to or harass any Twitch streamers or collect data about them or their streams without their consent.