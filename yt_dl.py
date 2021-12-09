#Getting/downloading Youtube-video, Youtube-playlist, Video info, Thumbnails, Audio of the video, etc. using Pytube. 

#===================================================Youtube-Video===================================================#
# from pytube import YouTube
# from pytube.cli import on_progress

#Enter the 'video link'
# yt=YouTube('https://www.youtube.com/watch?v=yTWnTAUiY4I', on_progress_callback = on_progress)
# yt=YouTube(input('Enter the video link: '), on_progress_callback = on_progress)


##'Download' any youtube video.
# print(f'Downloading.....\n\nTitle: {yt.title}.')
# yt.streams.get_highest_resolution().download()
# yt.streams.filter(mime_type='video/mp4', res='720p', progressive=True).first().download()




# yt=YouTube('https://youtu.be/kM3G35yhyDw')
# print(f'{round((yt.streams.get_highest_resolution().filesize)/10**6, 2)} MB')


# from pytube.cli import on_progress
# yt=YouTube('https://youtu.be/kM3G35yhyDw', on_progress_callback=on_progress)
# Quality_lst=['144p','360p','480p','720p','1080p']
# yt.streams.filter(res= Quality_lst[0]).first().download()


#Video-File Size Calculation.
# yt=YouTube(input('Enter the video link: '))
# print('\nCalculating.... ')
# # vid_size=(yt.streams.get_highest_resolution().filesize)/1024**2
# vid_size=(yt.streams.filter(res='1080p').first().filesize)/1024**2
# print(f'\nVideo File Size of "{yt.title}" is: \n{vid_size} MB')


#=================================================Youtube-playlist=================================================#
# from pytube import Playlist
# from pytube import YouTube
# from pytube.cli import on_progress

#Getting the playlist link.
# P_lst = Playlist('https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9')
# P_lst = Playlist(input('Enter the playlist link: '))


# print(P_lst.title)


#Printing all video-tiles of the playlist
# for index , video in enumerate(P_lst.videos):
# 	print(f'{index+1}.) {video.title}')



#Youtube-Playlist-Duration (Alternative-link: https://ytplaylist-len.herokuapp.com/) 
# import datetime
# P_lst_time=0
# for video in P_lst.videos:
# 	P_lst_time+=video.length
# Formated_time= str(datetime.timedelta(seconds = P_lst_time)).split(":")
# print(f"{Formated_time[0]}hr {Formated_time[1]}min {Formated_time[2]}sec")



#Download any part of playlist
# Required_vid_index=[1, 2, '5-10', '15-30', 32, 34] 
# for index in Required_vid_index:
# 	if str(index).isnumeric():	
# 		P_lst.videos[index-1].streams.get_highest_resolution().download(filename_prefix=f"{index}.) ")
# 	else:
# 		range_index=int(index.split('-')[0])
# 		for vid in P_lst.videos[int(index.split('-')[0])-1 : int(index.split('-')[1])]:
# 			vid.streams.get_highest_resolution().download(filename_prefix=f"{range_index}.) ")
# 			range_index+=1



#Download Full playlist
# for index , video in enumerate(P_lst.videos):
# 	video.streams.get_highest_resolution().download(filename_prefix=f"{index+1}.) ")



#Download full-playlist with progress-bar.
#Type1:
# Quality_lst=['144p','360p','480p','720p','1080p']
# for index , video_url in enumerate(P_lst.video_urls):
#     yt=YouTube(video_url, on_progress_callback=on_progress)
#     print(f'{index+1}.) {yt.title}')
#     yt.streams.filter(res= Quality_lst[4]).first().download(filename_prefix=f"{index+1}.) ")

#Type2:
# print('➡Downloading...\n')
# for index , video_url in enumerate(P_lst.video_urls):
#     yt=YouTube(video_url, on_progress_callback=on_progress)
#     print(f'{index+1}.) {yt.title}')
#     yt.streams.get_highest_resolution().download(filename_prefix=f"{index+1}.) ")

# print(f'\n☑Downloading Completed!')



#Download any 'part of playlist' with 'progress bar'
# from pytube import YouTube
# from pytube.cli import on_progress
# print('➡Downloading...\n')
# Required_vid_index=[1, 2, '5-10', '15-30', 32, 34] 
# for index in Required_vid_index:
#     if str(index).isnumeric():  
#         yt=YouTube(P_lst.video_urls[index-1], on_progress_callback= on_progress)
#         print(f'{index}.) {yt.title}')
#         yt.streams.get_highest_resolution().download(filename_prefix=f"{index}.) ")
#     else:
#         range_index=int(index.split('-')[0])
#         for vid_url in P_lst.video_urls[int(index.split('-')[0])-1 : int(index.split('-')[1])]:
#             yt=YouTube(vid_url, on_progress_callback=on_progress)
#             print(f'{range_index}.) {yt.title}')
#             yt.streams.get_highest_resolution().download(filename_prefix=f"{range_index}.) ")
#             range_index+=1

# print(f'\n☑Downloading Completed!')





#===============================================-(FINALL PROG)-===============================================#
from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress
import datetime
import os

user_choice_Plist_or_Video=int(input(f'➡Select you choice from the bellow options!  \n 1.)Video. \n 2.)Playlist. \n 3.)Cancel Process.  \n\n➡Enter the number here: '))

if user_choice_Plist_or_Video==1:
    vid_url = YouTube(input("\n⏩Enter the video link here: "), on_progress_callback=on_progress)    
    print(f'\n▶Title: {vid_url.title} \n▶Size: {round(vid_url.streams.get_highest_resolution().filesize/1024**2, 2)} MB \n▶Duration: {datetime.timedelta(seconds = vid_url.length)}') 

    user_choice_down=input(f'\n\nDo you wish to download "{vid_url.title}" video? [y/n]: ').lower()
    if user_choice_down=='y':
        vid_url.streams.get_highest_resolution().download()
        print(f'\n\n☑Downloading Completed!')
    
    else:
        print('\n🟥Downloading Stopped❗')    


elif user_choice_Plist_or_Video==2:
    P_lst = Playlist(input('\n⏩Enter the playlist link: '))
    print(f'\n▶Title: {P_lst.title} \n▶The total number of videos: {len(P_lst.videos)}')

    user_choice_Duration_Size = input(f'\n\n⏬Do you wish to calculate Duration & Size of "{P_lst.title}" playlist? [y/n]: ').lower()
    if user_choice_Duration_Size == 'y':
        P_lst_time=0
        P_lst_size=0
        print('➡Calculating....')
        for video in P_lst.videos:
          P_lst_time+=video.length
          P_lst_size+=(video.streams.get_highest_resolution().filesize)/1024**2
        Formated_time= str(datetime.timedelta(seconds = P_lst_time)).split(":")
        print(f'\nPlaylist-Duration: {Formated_time[0]}hr {Formated_time[1]}min {Formated_time[2]}sec')
        print(f'\nPlaylist-Size: {round(P_lst_size, 2)} MB')

    else:
        print("\n🟥Calculation Stopped❗")


    user_choice_down=input(f'\n\n⏬Do you wish to download "{P_lst.title}" playlist? [y/n]: ').lower()

    if user_choice_down=='y':
        print('\n➡Downloading...\n')
        for index , video_url in enumerate(P_lst.video_urls):
            yt=YouTube(video_url, on_progress_callback=on_progress)
            print(f'{index+1}.) {yt.title}')
            yt.streams.get_highest_resolution().download(filename_prefix=f"{index+1}.) ", output_path=P_lst.title)

        print(f'\n☑Downloading Completed!')

    else:
        print("\n🟥Downloading Stopped❗")


else:
    print('🟥Process Cancelled❗')



#============================================================================================================#



