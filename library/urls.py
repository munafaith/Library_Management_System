from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    UserListCreateView,
    UserDetailView,
    CheckoutBookView,
    ReturnBookView
)
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('books/<int:pk>/checkout/', CheckoutBookView.as_view(), name='book-checkout'),
    path('books/<int:pk>/return/', ReturnBookView.as_view(), name='book-return'),

]