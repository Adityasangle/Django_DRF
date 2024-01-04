from django.urls import path,include
from .views import Movies

from rest_framework import routers

router  = routers.DefaultRouter()
router.register('movies',Movies)
urlpatterns = [
    path("",include(router.urls))
]
# urlpatterns = [
#      path("movies",Movies.as_view())
#  ]

