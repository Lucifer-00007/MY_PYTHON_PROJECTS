#3.5l water in total
#Name of the music files:- Water.mp3, eye.mp3, physical.mp3
#water- 3.5l (437.5ml every 1hr) in bwt 9am-5pm. - Drank button(to reset reminder) - Logfile(to keep all the time stamp and the record)
#eye- every 30 min exercise of the eyes - EyDone button(to reset the reminder ) - Logfile
#physical activity - every 45 min a physical activity - ExDone - Logfile

#Rule:- Use Pygame Module to play audio.


##Type1 Fault is first "for loop of k" is running 8 times then "for loop of l" is running 16 times then "for loop of j" is running 10 times  :-
# import time
# for k in range(8):          #----------------Drink-Water----------------#
#     # time.sleep(3600)   #1hr gap
#     time.sleep(1)    #testing purpose
#     print("drink water .mp3 file run here")
#
#
# for l in range(16):          #----------------Eye-Rest----------------#
#     # time.sleep(1800)   #30min gap
#     time.sleep(0.5)      #testing purpose
#     print("Give rest to ur eye .mp3 file run")
#
# #45min = 10.66 times. Thus loop should run for 10.66 times to complete  8hrs notification of every 45min.
# for j in range(10):          #----------------Physical-Activity---------------#
#     # time.sleep(2800)   #45min gap
#     time.sleep(0.75)     #testing purpose
#     print("Perform a physical activity .mp3 file run")




# #Type2(trying to play a music using pygame):-
# import time
# import pygame
# print("Now the music will play like this:--")
# pygame.mixer.init()
# pygame.mixer.music.load('abd.mp3')
# pygame.mixer.music.play()
# for i in range(7):
#     time.sleep(5)
#     print(f"...Enjoy the music round{i}...")



# #Type3  Fault is absence of time accuracy of the notification :-
# import time
# import pygame
# j="drank"
# k="eydone"
# l="exdone"
# No_of_sleep_second=10
#
# def getmytime():
#     import datetime
#     return datetime.datetime.now()
#
# log_file=open("Healty_Prog_log.txt","a")
#
# for i in range(16):    #for 1 day (total 8hrs). Afert that u should restart this program...
#     if i < 8 and j=="drank" and j!="stopwn":                                  #----------------Drink-Water----------------#
#         time.sleep(1 * No_of_sleep_second)
#         pygame.mixer.init()
#         pygame.mixer.music.load('water.mp3')
#         pygame.mixer.music.play()
#         j=input("Drink water!! To reset water.mp3 file type 'drank' press enter. And to stop this reminder type 'stopwn' and press enter = ")
#         # time.sleep(1*30)  #30sec
#         t1=getmytime()
#         log_file.write(f"[{t1}],{j} \n")
#
#     if i < 16 and k=="eydone" and k!="stopeyn":                                #----------------Eye-Rest----------------#
#         time.sleep(0.5 * No_of_sleep_second)
#         pygame.mixer.music.load('eye.mp3')
#         pygame.mixer.music.play()
#         k=input("Give rest to ur eye!! To reset eye.mp3 file type 'eydone' press enter. And to stop this reminder type 'stopeyn' and press enter = ")
#         # time.sleep(0.5*30)  #15sec
#         t2=getmytime()
#         log_file.write(f"[{t2}],{k} \n")
#
#     if i < 10 and l=="exdone" and l!="stopexn":                                #----------------Physical-Activity---------------#
#         time.sleep(0.75 * No_of_sleep_second)
#         pygame.mixer.music.load('physical.mp3')
#         pygame.mixer.music.play()
#         l=input("Perform a physical activity!! To reset pysical.mp3 file type 'exdone' press enter. And to stop this reminder type 'stopexn' and press enter = ")
#         # time.sleep(0.75*30)   #22.5sec
#         t3=getmytime()
#         log_file.write(f"[{t3}],{l} \n")
# log_file.close()



#Type4:-
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, reset):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == reset:
            mixer.music.stop()
            break

def log_now(msg):
    with open("Healty_Prog_log.txt", "a") as f:
        f.write(f"[{datetime.now()}], {msg}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    # watersecs = 40*60
    # eyessecs = 45*60
    # exsecs = 30*60
    watersecs = 1*30  #for Testing Purpose
    eyessecs = 0.5*30 #for Testing Purpose
    exsecs = 0.75*30  #for Testing Purpose

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to rest the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water!!")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'eydone' to reset the alarm.")
            musiconloop('eye.mp3', 'eydone')
            init_eyes = time()
            log_now("Eyes Relaxed!!")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'exdone' to reset the alarm.")
            musiconloop('physical.mp3', 'exdone')
            init_exercise = time()
            log_now("Physical Activity done!!")
























































