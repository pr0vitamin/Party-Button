#!/home/jeremy/git/Party-Button/party_env/bin/python

import pychromecast
#import pychromecast.controllers.youtube as youtube

video_url = ""
video_format = ""
cast_device = "SHIELD"

#print "Listing available Chromecasts:"
#print pychromecast.get_chromecasts_as_dict().keys()

print "connecting to cast device:"
cast = pychromecast.get_chromecast(friendly_name=cast_device)
#cast.wait()
print cast.device
print cast.status

#Youtube stuff is broken for now, but might work later
#yt = youtube.YouTubeController()
#cast.register_handler(yt)

print "Trying to play media:"
#yt.play_video("y6120QOlsfU")
mc = cast.media_controller
mc.play_media(video_url, video_format)

playing = False
while True:
    while not mc.status.player_is_playing:
        if playing:
            # video stopped playing, don't do stuff
            playing = False
            print "Not playing event fired"
    while mc.status.player_is_playing:
        if not playing:
            # video started playing, do stuff
            playing = True
            print "Playing event fired"
