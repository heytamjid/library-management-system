from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.allbooks, name='allbooks' ),
    path('detailedview/<str:thisslug>/', views.detailedview, name='detailedview' ),
    path('borrow/<int:boid>/', views.borrow_book, name='borrow' ),
    path('return/<int:boid>/', views.return_book, name='return' ),
    path('wishlist/<int:boid>/', views.wishlist, name='wishlist' ),
    path('search/', views.search_books, name='search-books'),
    #path('category/<str:catename>/', views.cate, name='cate'),
]