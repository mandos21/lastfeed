import pylast 

# Add your API keys here
API_KEY = ""
API_SECRET = ""

lastfm_network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)


# Add your username
user = lastfm_network.get_user("")

friends_list = user.get_friends()

def poll_friends():
    now_playing_list = []
    for friend in friends_list:
        print("                                                                                                                                                                                                                                                                                                                                   ", end="")
        now_playing = str(friend.get_now_playing())
        friend_name = str(friend.get_name())
        if(now_playing != "None"):
            print(friend_name + ": " + now_playing, end="                                      ")


poll_friends()
