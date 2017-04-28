#!/usr/bin/env python

import time
import os
import motephat

motephat.configure_channel(1, 16, False)
motephat.configure_channel(4, 16, False)

motephat.set_clear_on_exit(True)

twitterUrl = os.environ.get('twitter')
facebookUrl = os.environ.get('facebook')
youtubeUrl = os.environ.get('youtube')
instagramUrl = os.environ.get('instagram')


def getTwitterFollowers():
	followers = os.popen("curl -s %s | grep 'data-nav=\"followers\"' | grep -o '[0-9|,]\+' | tr -d ','" % twitterUrl).read()

	return followers

def getFacebookLikes():
	likes = os.popen("curl -s %s | grep 'Likes:' | grep -o '[0-9]\+'" % facebookUrl).read()

	return likes

def getYoutubeSubscribers():
	subscribers = os.popen("curl -s %s | grep -o '[0-9|,]\+ subscribers' | grep -o '[0-9|,]\+' | tr -d ','" % youtubeUrl).read()

	return subscribers

def getInstagramFollowers():
	followers = os.popen("curl -s %s | grep -o 'meta content=\"[[:digit:]]\{1,\} Followers' | grep -o '[0-9]\+'" % instagramUrl).read()

	return followers

def setMoteColor(r, g, b):
	# http://forums.pimoroni.com/t/mote-phat-not-all-leds-are-lighting-on-first-show/3740/3
	# Workaround: multiple motephat.show()
	motephat.set_all(r, g, b, 1.0)
	motephat.show()
	motephat.show()

def setMoteBlink(r, g, b):
	for x in range(3):
		setMoteColor(r, g, b)
		time.sleep(0.5)

		setMoteColor(255, 255, 255)
		time.sleep(0.5)

def main():
	previousTwitterFollowers = 0
	previousFacebookLikes = 0
	previousYoutubeSubscribers = 0
	previousInstagramFollowers = 0

	while(1):
		currentTwitterFollowers = getTwitterFollowers().strip()

		if(currentTwitterFollowers > previousTwitterFollowers):
			setMoteBlink(64, 153, 255)
			print "Twitter: " + currentTwitterFollowers
			previousTwitterFollowers = currentTwitterFollowers

		currentFacebookLikes = getFacebookLikes().strip()

		if(currentFacebookLikes > previousFacebookLikes):
			setMoteBlink(59,89,152)
			print "Facebook: " + currentFacebookLikes
			previousFacebookLikes = currentFacebookLikes

		currentYoutubeSubscribers = getYoutubeSubscribers().strip()

		if(currentYoutubeSubscribers > previousYoutubeSubscribers):
			setMoteBlink(239, 14, 17)
			print "Youtube: " + currentYoutubeSubscribers
			previousYoutubeSubscribers = currentYoutubeSubscribers

		currentInstagramFollowers = getInstagramFollowers().strip()

		if(currentInstagramFollowers > previousInstagramFollowers):
			setMoteBlink(152, 66, 137)
			print "Instagram: " + currentInstagramFollowers
			previousInstagramFollowers = currentInstagramFollowers

		setMoteColor(255, 255, 255)

		time.sleep(60)

main()
