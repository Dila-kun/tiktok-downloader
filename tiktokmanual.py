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

# def getDownloadVideos(downloaded_videos, user_name):
#     path = "downloaded/" + user_name + ".txt"
#     fileToList(path, downloaded_videos)

def getVideosToDownload(videos_id, downloaded_videos):
    return list(set(videos_id) - set(downloaded_videos))

def storageVideoDownloaded(video_id, file_name):
    f = open(file_name, "a")
    f.write(video_id)
    f.write("\n")
    f.close()

def downloadVideo(video_id, user_name):
    command = "youtube-dl.exe https://www.tiktok.com/@" + user_name + "/video/" + video_id + " -i -c -o \"" + user_name + "/%(upload_date)s - %(title)s - %(id)s - (%(duration)ss) [%(resolution)s].%(ext)s\""
    os.system(command)
    count = 0
    while not os.path.exists(user_name) and count < 5:
        os.system(command)
        count += 1
        tm.sleep(10)

def moverVideo(user_name):
    file_name = os.listdir(user_name)
    source = 'E:/Downloads/Entites/tiktokdownload/' + user_name + '/' + file_name[0]
    folder = 'E:/Downloads/Entites/tiktok/' + user_name
    destination = 'E:/Downloads/Entites/tiktok/' + user_name + '/' + file_name[0]
    if not os.path.exists(folder):
        os.mkdir(folder)
    shutil.move(source, destination)
    os.rmdir(user_name)

def downloadUserVideos(videos_to_download, user_name, backup_path):

    for video_id in videos_to_download:
        downloadVideo(video_id, user_name)
        if os.path.exists(user_name):
            moverVideo(user_name)
            f = open(backup_path, "a")
            f.write(video_id)
            f.write("\n")
            f.close()
        # storageVideoDownloaded(video_id, file_name)

# def storageVideosDownloaded(list_name, file_name):
#     f = open(file_name, "a")
#     for x in list_name:
#         f.write(x)
#         f.write("\n")
#     f.close()

def user(user_name):
    all_videos_id = getAllUserVideos(user_name)
    videos_to_download = list(())
    path_v = "downloaded/" + user_name + ".txt"
    if os.path.isfile(path_v):
        downloaded_videos = fileToList(path_v)
        videos_to_download = getVideosToDownload(all_videos_id, downloaded_videos)
    else:
        videos_to_download = all_videos_id

    downloadUserVideos(videos_to_download, user_name, path_v)
    # if videos_to_download:
    #     storageVideosDownloaded(videos_to_download, path_v)


def main():
    user_name = input("Enter username: ")
    user(user_name)


main()