from django.urls import path
from .views import HomePageView, GMBuildsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gmbuilds/',GMBuildsPageView.as_view(), name='gmbuilds'),
]