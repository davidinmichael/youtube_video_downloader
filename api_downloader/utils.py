from googleapiclient.discovery import build
import googleapiclient.discovery
import googleapiclient.errors
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