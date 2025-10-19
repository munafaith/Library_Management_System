from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This view handles listing all books and creating a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This view handles retrieving, updating, and deleting a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer