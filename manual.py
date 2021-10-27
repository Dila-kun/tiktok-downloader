import os
import time as tm
import shutil

def getAllUserVideos(user_name):
    videos_id = list(())
    video_id = input("Enter video id: ")
    while video_id != "-1":
        videos_id.append(video_id)
        video_id = input("Enter video id: ")
    return videos_id

def fileToList(file_name):
    list_name = list(())
    f = open(file_name, "r")
    list_name = f.read().splitlines()
    f.close()
    return list_name

def downloadVideo(video_id, user_name):
    command = "youtube-dl.exe https://www.tiktok.com/@" + user_name + "/video/" + video_id + " -o \"" + user_name + "/%(upload_date)s - %(title)s - %(id)s - (%(duration)ss) [%(resolution)s].%(ext)s\""
    os.system(command)
    if not os.path.exists(user_name):
        os.system(command)
        if not os.path.exists(user_name):
            os.system(command)

def moverVideo(user_name):
    file_name = os.listdir(user_name)
    source = 'E:/Downloads/Entites/tiktokdownload/' + user_name + '/' + file_name[0]
    folder = 'E:/Downloads/Entites/tiktok/' + user_name
    destination = 'E:/Downloads/Entites/tiktok/' + user_name + '/' + file_name[0]
    if not os.path.exists(folder):
        os.mkdir(folder)
    shutil.move(source, destination)
    os.rmdir(user_name)

def downloadUserVideos(videos_to_download, user_name):
    
    for video_id in videos_to_download:
        downloadVideo(video_id, user_name)
        if os.path.exists(user_name):
            moverVideo(user_name)


def user(user_name):
    all_videos_id = getAllUserVideos(user_name)

    downloadUserVideos(all_videos_id, user_name)


def main():
    user_name = input("Enter username: ")
    user(user_name)


main()