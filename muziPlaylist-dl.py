#coding: utf-8
import os
import urllib2
import errno
import json

#Base URL's required
muzi_url = 'https://muzi.sdslabs.co.in/'
cdn_url = 'https://music.sdslabs.co.in/'
playlists_url = 'https://muzi.sdslabs.co.in/ajax/playlist/list.php'
tracks_url = 'https://muzi.sdslabs.co.in/ajax/track/?id='
default_path = os.environ["HOME"]+"/muziPlaylists/"

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
choice = int(choice)-1
chosen_playlist = avlbl_playlists_json[choice]
chosen_playlist_id = chosen_playlist['id']
chosen_playlist_url = muzi_url+"ajax/playlist/?id="+chosen_playlist_id
chosen_playlist_json = json.load(urllib2.urlopen(chosen_playlist_url))

#Playlist Info
chosen_playlist_tracks = chosen_playlist_json['tracks']
chosen_playlist_creator = chosen_playlist_json['username']
chosen_playlist_name = chosen_playlist_json['name']

#Create folders
os.mkdir(default_path,0755)
chosen_playlist_folder = default_path+chosen_playlist_name
os.mkdir(chosen_playlist_folder,0755) 

#Download Tracks
for track in chosen_playlist_tracks:
	file_name = track['title']+'-'+track['artist']+'.mp3'
	file_url_json = json.load(urllib2.urlopen(tracks_url+track['id']))
	file_suburl = file_url_json['file']
	temp_file_url = cdn_url+file_suburl
	temp_file_url = temp_file_url.replace('\\','/')
	final_file_url = temp_file_url.replace(' ','%20')
	mp3_file = urllib2.urlopen(final_file_url)
	with open(chosen_playlist_folder+file_name,'wb') as tune:
		tune.write(mp3_file.read())


		
	
 
