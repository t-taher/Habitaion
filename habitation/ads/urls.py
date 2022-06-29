from django.db import router
from habitation.ads.api.views import ADViewSet, FavouriteView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.
router.register('ads', ADViewSet, basename='AD')
router.register('favourite', FavouriteView, basename='Favourite')


app_name = "ads"

urlpatterns = [] + router.urls
