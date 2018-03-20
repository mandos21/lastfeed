# lastFeed

##### For viewing your last.fm friendlists scrobbles as a zipper-style feed in semi-realtime.



### Dependencies

Install lemonbar[[AUR](https://wiki.archlinux.org/index.php/Lemonbar)][[git](https://github.com/LemonBoy/bar)]

Install zscroll[[AUR](https://aur.archlinux.org/packages/zscroll-git/)][[git](https://github.com/noctuid/zscroll)]


### Setting Up

You'll need last.fm API keys, which you can aquire [here](https://www.last.fm/api/account/create).

In feed.py, add your API keys and username

```python
API_KEY = "key_goes_here"
API_SECRET = "secret_key_goes_here"

lastfm_network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)

user = lastfm_network.get_user("your_username")

friends_list = user.get_friends()
```

In lemonbar.sh change the parameters to your liking

```sh
~/lastfeed/wrapper.sh | lemonbar -g 1920x20+3840 -b -B "$color0" -F "$color1" -U "$color1" -p -u 3
```
In my case, I set the bar to be situated on my rightmost monitor at the bottom.  Thickness is set to 20 px.  
The color variables are taken from my wal colorscheme.  If you don't use wal these can be set manually.

```sh
# Source colors from my wal colorscheme

. "${HOME}/.cache/wal/colors.sh"
```


If you don't know how to use lemonbar or zscroll, check out their git pages or simply use
```sh
man lemonbar
# and/or
man zscroll
```

### Future additions

#### At some point, I intend to add:

dynamic pre-text spacing calculated via monitor size

editable space between scrobbles

True realtime appearence of new scrobbles, not just a list generated every 3 minutes
