from django.conf.urls import include, url

urlpatterns = [
    url(r'^mqqm/', include('mqqm.urls')),
    url(r'^v1/mqq/', include('v1_mqq.urls')),
]