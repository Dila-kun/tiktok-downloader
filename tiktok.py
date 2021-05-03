from TikTokApi import TikTokApi
import json
import os

api = TikTokApi();

def getAllUserVideos(user_name):
    videos_id = list(())
    user_videos = api.byUsername(user_name, 2000)
    for v in user_videos:
        videos_id.append(v["id"])
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

def downloadVideo(video_id, user_name):
    if not os.path.exists(user_name):
        os.mkdir(user_name)
    command = "youtube-dl.exe https://www.tiktok.com/@" + user_name + "/video/" + video_id + " -o \"%(uploader)s/%(upload_date)s - %(title)s - %(id)s - (%(duration)ss) [%(resolution)s].%(ext)s\""
    os.system(command)
    # await asyncio.sleep(4)

def downloadUserVideos(videos_to_download, user_name):
    for x in videos_to_download:
        downloadVideo(x, user_name)

def storageVideosDownloaded(list_name, file_name):
    f = open(file_name, "a")
    for x in list_name:
        f.write(x)
        f.write("\n")
    f.close()

def user(user_name):
    all_videos_id = getAllUserVideos(user_name)
    videos_to_download = list(())
    path_v = "downloaded/" + user_name + ".txt"
    if os.path.isfile(path_v):
        downloaded_videos = fileToList(path_v)
        videos_to_download = getVideosToDownload(all_videos_id, downloaded_videos)
    else:
        videos_to_download = all_videos_id

    downloadUserVideos(videos_to_download, user_name)
    if videos_to_download:
        storageVideosDownloaded(videos_to_download, path_v)


def main():
    # get the name of all users
    # path_exist = os.path.isfile("users.txt")
    # if (path_exist):
    if not os.path.exists("users.txt"):
        f = open("users.txt", "x")
        f.close()
    userslist = fileToList("users.txt")
    for x in userslist:
        user(x)


main()

# f = open("downloaded/thallitatreyce.txt", "a")
# for x in list_name:
#     f.write(x)
#     f.write("\n")
#     f.close()

# if not os.path.exists("teste"):
#     os.mkdir("teste")
# teste = open("teste/teste.txt", "w")
# teste.write("testado")
# teste.close()

# print(userslist)





# f = open("demofile2.txt", "a")
# for i in user_videos:
#     f.write("Now the file has more content!")
# result = json.dumps(user_videos)
# f.write(result)
# f.close()