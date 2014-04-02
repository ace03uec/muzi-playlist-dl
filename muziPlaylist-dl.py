#coding: utf-8
import os
import urllib2
import errno
import json

muzi_url = 'https://muzi.sdslabs.co.in/'
cdn_url = 'https://music.sdslabs.co.in/'
playlist_url = 'https://muzi.sdslabs.co.in/ajax/playlist/list.php'

avlbl_playlists = urllib2.urlopen(playlist_url)
avlbl_playlists_json = json.load(avlbl_playlists)
print 'available playlists: \n'
for x in avlbl_playlists_json:
	print x['name']

