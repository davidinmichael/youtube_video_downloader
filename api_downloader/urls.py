from django.urls import path
from .views import *


urlpatterns = [
    path("popular/", PopularVideos.as_view()),
]
