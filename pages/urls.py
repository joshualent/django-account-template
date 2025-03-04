from django.urls import path, reverse

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
