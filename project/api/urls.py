
from django.urls import path
from api.views import UserListAPIView, GenerateDLO


urlpatterns = [
    path("users/", UserListAPIView.as_view()),
    path("dlo/<int:pk>", GenerateDLO.as_view())
]
