#coding: utf-8
import os
import urllib2
import errno
import json

#Base URL's required
muzi_url = 'https://muzi.sdslabs.co.in/'
cdn_url = 'https://music.sdslabs.co.in/'
playlists_url = 'https://muzi.sdslabs.co.in/ajax/playlist/list.php'

#Extract Playlists available
avlbl_playlists = urllib2.urlopen(playlists_url)
avlbl_playlists_json = json.load(avlbl_playlists)
print 'available playlists: \n'
index = 0
for playlist in avlbl_playlists_json:
    index = index+1
    print str(index)+"\t"+playlist['name']+"\t"+playlist['username']

#Playlist Choice and JSON extract
choice = raw_input('Choose which playlist to download. [1,2,3,...]')
choice = choice -1
chosen_playlist = avlbl_playlists_json[choice]
chosen_playlist_id = chosen_playlist['id']
chosen_playlist_url = muzi_url+"ajax/playlist/?id="+chosen_playlist_id
chosen_playlist_json = json.load(urllib2.urlopen(chosen_playlist_url))

#Playlist download

    
