from googleapiclient.discovery import build
import googleapiclient.discovery
import googleapiclient.errors
from pytube import YouTube
import os

api_version = "v3"
api_key = os.environ.get("youtube_api_key")
api_service_name = "youtube"

# YouTube Object
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=api_key)


def get_popular_videos():
    request = youtube.videos().list(
        part="snippet",
        chart='mostPopular',
        maxResults=10,
    )
    response = request.execute()
    return response


def search_video(search_keys):
    request = youtube.search().list(
        part="snippet",
        maxResults=50,
        q=search_keys
    )
    response = request.execute()
    return response


def search_pagination(search_keys, page_token):
    request = youtube.search().list(
        part="snippet",
        maxResults=50,
        q=search_keys,
        pageToken=page_token
    )
    response = request.execute()
    return response


def get_single_video(video_id):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()
    return response


def get_channel_info(channel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()
    return response


def download_video(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return "Download completed"
    except:
        return "Something went wrong, please try again"
