#!/usr/bin/env python3

import pylast
import os

last_fm = pylast.LastFMNetwork(
    api_key=os.environ["LAST_API_KEY"],
    api_secret=os.environ["LAST_API_SECRET"],
    username=os.environ["LAST_USERNAME"],
    password_hash=pylast.md5(os.environ["LAST_PASSWORD"]),
)

print("Getting now playing...")

track = last_fm.get_authenticated_user().get_now_playing()

if track:
    print("Loving: ", track)
    track.love()
else:
    print("Man, play something")
