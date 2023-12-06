from django.urls import path
from sistema.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
