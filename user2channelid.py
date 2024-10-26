import requests

def user2channelid(users_list, auth_token, client_id):
    # converts twitch usernames to their unique channel ids
    num_users = len(users_list)

    # next create the command
    if users_list != []:
        req_url = "https://api.twitch.tv/helix/users?"
        # add users part
        for idx in range(num_users):
            user = users_list[idx]
            added_part = f"login={user}"
            if idx < num_users-1:
                added_part += "&"
            req_url += added_part

        payload = {"Authorization":"Bearer " + auth_token, "Client-ID":client_id}
        # GET request for the data
        r = requests.get(req_url, headers=payload)
        data = eval(r.text)["data"]

        channel_ids = {}
        for response in data:
            channel_ids[response["login"]] = response["id"]

        return channel_ids
    else:
        return {}