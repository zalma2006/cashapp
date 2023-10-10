from django.urls import include, path
from .views import BanksView, UserView

urlpatterns = [
    path("users/", UserView.as_view(template_name='banks/users.html'), name='users'),

    path("banks/", BanksView.as_view()),
]