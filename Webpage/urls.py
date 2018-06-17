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
    #url(r'^alter/fav/$', views.FavAlterView.as_view(), name='fav-alter'),
    path('alter/fav/', views.FavAlterView.as_view(), name='fav-alter'),
    path('favoritelaptops/', views.FavoritedLaptopsByUserListView.as_view(), name='my-favorite'),
    path('allfavoritedlaptops/', views.AllFavoritedLaptopsByUsersListView.as_view(), name='all-favorite'),
    path('laptop/create/', views.LaptopCreate.as_view(), name='laptop_create'),
    path('dreamlaptop/<int:pk>', views.DreamLaptopDetailView.as_view(), name='dreamlaptop-detail'),
    path('dreamlaptop/create/', views.DreamLaptopCreate.as_view(), name='dreamlaptop_create'),
]