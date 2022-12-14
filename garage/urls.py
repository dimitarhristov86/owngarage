from django.urls import path
from .views import CarListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from . import views


urlpatterns = [
    path('', CarListView.as_view(), name='garage-home'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('car/new/', CarCreateView.as_view(), name='car-new'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    path('my_cars/', views.my_cars, name='my-cars'),
    path('contact_us/', views.contact_us, name='garage-contact_us'),
    path('contact_user/<int:pk>/', views.ContactUser.as_view(), name='contact-user'),
    path('search_cars/', views.search_cars, name='search-cars'),
]
