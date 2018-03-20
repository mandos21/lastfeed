import pylast 

API_KEY = "ada4529ad4a007695ea71ab23da78dac"
API_SECRET = "a8d9caa037bc7b31c23c54339ad39a2d"

lastfm_network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)

user = lastfm_network.get_user("m_degenaro")

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
