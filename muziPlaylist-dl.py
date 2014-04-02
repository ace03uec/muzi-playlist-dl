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
choice = raw_input('Choose which playlist to download. [1,2,3,..etc]: ')
choice = int(choice)-1
#handle bad input
chosen_playlist = avlbl_playlists_json[choice]
chosen_playlist_id = chosen_playlist['id']
chosen_playlist_url = muzi_url+"ajax/playlist/?id="+chosen_playlist_id
chosen_playlist_json = json.load(urllib2.urlopen(chosen_playlist_url))

#Playlist Info
chosen_playlist_tracks = chosen_playlist_json['tracks']
chosen_playlist_creator = chosen_playlist_json['username']
chosen_playlist_name = chosen_playlist_json['name']
print "The following playlist has been chosen to be downloaded : "+chosen_playlist_name


#Create folders
if (os.path.exists(default_path) == False):
	os.mkdir(default_path,0755)
chosen_playlist_folder = default_path+chosen_playlist_name
if (os.path.exists(chosen_playlist_folder) == False):
	os.mkdir(chosen_playlist_folder,0755) 
else:
	print "The Playlist you are trying to create, appears to exist. If you continue you will try to force the download."
#Download Tracks
index = 1
total = len(chosen_playlist_tracks)
for track in chosen_playlist_tracks:
	file_name = track['title']+'.mp3'
	print "Downloading "+str(index)+" / "+str(total)+" : "+file_name #debug
	file_url_json = json.load(urllib2.urlopen(tracks_url+track['id']))
	index = index+1
	file_suburl = file_url_json['file']
	temp_file_url = cdn_url+file_suburl
	temp_file_url = temp_file_url.replace('\\','/')
	final_file_url = temp_file_url.replace(' ','%20')
#	print final_file_url #debug
	mp3_file = urllib2.urlopen(final_file_url)
	with open(chosen_playlist_folder+"/"+file_name,'wb') as tune:
		tune.write(mp3_file.read())


		
	
 
