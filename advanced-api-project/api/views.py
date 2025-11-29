from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.
class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    pass

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            "title": ["exact", "icontains"],
            "publication_year": ["exact", "gte", "lte"],
            "author__name": ["exact", "icontains"],
        }

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

filterset_class = BookFilter
filterset_fields = ['title', 'author', 'publication_year']
search_fields = ['title', 'author_name']
ordering_fields = ['title', 'publication_year']
ordering = ['title']

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