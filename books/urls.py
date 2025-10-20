from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    CheckoutBookView,
    ReturnBookView
)

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/checkout/', CheckoutBookView.as_view(), name='book-checkout'),
    path('<int:pk>/return/', ReturnBookView.as_view(), name='book-return'),
]