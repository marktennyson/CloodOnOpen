from django.urls import path
from .views import *

apiUrlpatterns = [
    path('api/', apiIndexView)
]

urlpatterns = apiUrlpatterns+[
    path('', indexView),
    path('index2/', index2View),
    path('all-data',allData),
    path('put/',putData),
    path('all-regions/', allRegions),
    path('all-sub-regions/', allSubRegions),
    path('country-per/', countryPer),
]