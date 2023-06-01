from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()


router.register('saveDataAPI', views.saveDataAPI)


urlpatterns = router.urls