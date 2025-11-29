from rest_framework import serializers
from .models import *
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, year):
        if year > date.today().year:
            raise serializers.ValidationError("Publication year can not be in the future.")
        return year

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = [
            'name',
            'books',
        ]
