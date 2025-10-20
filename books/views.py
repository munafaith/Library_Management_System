from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer
import datetime

# This view handles listing all books and creating a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['isbn', 'available_copies'] 
    search_fields = ['title', 'author'] 

# This view handles retrieving, updating, and deleting a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class CheckoutBookView(APIView):
    permission_classes = [IsAuthenticated] # Ensures only logged-in users can access this view

    def post(self, request, pk, *args, **kwargs):
        # Find the book by its primary key (pk)
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if there are available copies of the book
        if book.available_copies <= 0:
            return Response({'error': 'No available copies of this book.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user already has an active loan for this book
        existing_loan = Loan.objects.filter(user=request.user, book=book, is_returned=False).exists()
        if existing_loan:
            return Response({'error': 'You have already checked out this book.'}, status=status.HTTP_400_BAD_REQUEST)

        # If all checks pass, create the loan
        book.available_copies -= 1
        book.save()

        loan = Loan.objects.create(
            user=request.user,
            book=book
        )
        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated] # Protect this endpoint

    def post(self, request, pk, *args, **kwargs):
        # Find the active loan for this book and user
        try:
            loan = Loan.objects.get(user=request.user, book__pk=pk, is_returned=False)
        except Loan.DoesNotExist:
            return Response({'error': 'No active loan found for this book.'}, status=status.HTTP_404_NOT_FOUND)

        # Update the loan and the book's copy count
        loan.is_returned = True
        loan.return_date = datetime.datetime.now()
        loan.save()

        book = loan.book
        book.available_copies += 1
        book.save()

        return Response({'message': 'Book returned successfully.'}, status=status.HTTP_200_OK)