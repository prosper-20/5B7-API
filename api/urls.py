from django.urls import path
from .views import post_list, post_detail, post_delete, post_update, post_create


urlpatterns = [
    path("home/", post_list, name="api-list"),
    path("<slug:slug>/", post_detail, name="api-detail"),
    path("<slug:slug>/update", post_update, name="api-update"),
    path("<slug:slug>/delete", post_delete, name="api-delete"),
    path("create", post_create, name="create")
]