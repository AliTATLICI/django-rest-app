from django.urls import path, include

#from rest_framework import routers
from pbs import views

#router = routers.DefaultRouter()
#router.register(r'birimler', views.BirimViewSet)

urlpatterns = {
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.Index.as_view()),
    path('v1/transaksi/', views.Transaksi.as_view())
    #path('register/', views.Register.as_view())
}