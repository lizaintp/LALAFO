from rest_framework.generics import ListAPIView

from apps.posts import models
from apps.posts import serializers

class PostAPIView(ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer