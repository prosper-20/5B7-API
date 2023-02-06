from django.urls import path
from .views import post_list, post_detail


urlpatterns = [
    path("home/", post_list, name="api-list"),
    path("<slug:slug>/", post_detail, name="api-detail")
]