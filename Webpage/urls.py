from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('laptops/', views.LaptopListView.as_view(), name='laptops'),
    path('laptop/<int:pk>', views.LaptopDetailView.as_view(), name='laptop-detail'),
    path('processor/<int:pk>', views.ProcessorDetailView.as_view(), name='processor-detail'),
    path('graphics_card/<int:pk>', views.GraphicsCardDetailView.as_view(), name='graphics_card-detail'),
    path('ram/<int:pk>', views.RamDetailView.as_view(), name='ram-detail'),
    path('storage_drive/<int:pk>', views.StorageDriveDetailView.as_view(), name='storage_drive-detail'),
    path('display/<int:pk>', views.DisplayDetailView.as_view(), name='display-detail'),
    url(r'^alter/fav/$', views.FavAlterView.as_view(), name='fav-alter'),
]