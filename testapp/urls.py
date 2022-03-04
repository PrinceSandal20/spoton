from django.urls import path,include
from .views import (
    RentInListView,
    RentInDetailView,
    RentInCreateView,
    RentInUpdateView,
    RentInDeleteView
)     
from . import views

urlpatterns = [
    path('',views.home,name="home1"),
    path('final/',views.final,name="final"),
    path('about/',views.about,name='about'),
    path('products/',RentInListView.as_view(),name='home'),
    path('rentIn/<int:pk>/',RentInDetailView.as_view(),name='rentIn-detail'),
    path('rentIn/new/',RentInCreateView.as_view(),name='rentIn-create'),
    path('rentIn/<int:pk>/update/',RentInUpdateView.as_view(),name='rentIn-update'),
    path('rentIn/<int:pk>/delete/',RentInDeleteView.as_view(),name='rentIn-delete'),
    path('search/',views.search,name="search"),
]

