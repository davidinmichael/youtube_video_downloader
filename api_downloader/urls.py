from django.urls import path
from .views import *


urlpatterns = [
    path("popular/", PopularVideos.as_view()),
    path("search/", SearchVideos.as_view()),
    # path("search/?search_key=<str:search_keys>&?token=<str:page_token>/", SearchPaginated.as_view()),
]