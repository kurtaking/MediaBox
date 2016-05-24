from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class Index(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        return Response(template_name='user/index.html')

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
