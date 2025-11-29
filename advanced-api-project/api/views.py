from django.shortcuts import render
from rest_framework import permissions, generics, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    pass

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
filterset_fields = ['title', 'author', 'publication_year']
search_fields = ['title', 'author_name']
ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]