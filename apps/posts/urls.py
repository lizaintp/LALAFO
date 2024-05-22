from django.urls import path
from apps.posts import views

urlpatterns = [
    path('',views.PostAPIView.as_view(), name = 'api_post')
]
