from django.conf.urls import url

from views import Pokes

urlpatterns = [
    url(r'^', Pokes.as_view(), name='pokes'),
    url(r'^create', Pokes.as_view(), name='pokes-create'),
]