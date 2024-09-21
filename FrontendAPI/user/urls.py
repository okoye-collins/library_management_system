from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserAPIView.as_view(), name="signup"),
]