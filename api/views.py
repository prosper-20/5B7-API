from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from post.models import Post


@api_view(['GET'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def post_detail(request, slug):
    if request.method == "GET":
        post = Post.objects.get(slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)



