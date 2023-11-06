
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import threading

from flask import redirect
from api_downloader.utils import *
import requests


def index(request):
    url = "http://127.0.0.1:8000/api/popular"
    response = requests.get(url).json()
    context = {
        "items": response["items"],
        "head": "Most Popular Videos"
    }
    return render(request, "downloader/index.html", context)


def get_video(request):
    video_id = request.GET.get("video_id")
    url = f"http://127.0.0.1:8000/api/video/details/{video_id}"
    response = requests.get(url).json()
    context = {
        "items": response["items"]
    }
    return render(request, "downloader/get-video.html", context)


def search_videos(request):
    if request.method == "POST":
        search_keys = request.POST.get("search_keys")
        response = search_video(search_keys)
    else:
        search_keys = request.GET.get("search_keys")
        page_token = request.GET.get("page_token")
        response = search_pagination(search_keys, page_token)
    context = {
        "data": response,
        "items": response["items"],
        "search_key": search_keys,
    }
    return render(request, "downloader/search.html", context)


def download_videos(request):
    video_id = request.GET.get("video_id")
    prev_page = request.META.get('HTTP_REFERER')
    # download_thread = threading.Thread(target=download_video, args=(video_id,))
    # download_thread.start()
    download_video(video_id)
    return HttpResponseRedirect(prev_page or '/')

# def download_videos(request):
#     video_id = request.GET.get("video_id")
#     prev_page = request.META.get('HTTP_REFERER')
    
#     def download_video_thread(video_id):
#         download_video(video_id)

#     download_thread = threading.Thread(target=download_video_thread, args=(video_id,))
#     download_thread.start()
    
#     return redirect(prev_page or '/')
