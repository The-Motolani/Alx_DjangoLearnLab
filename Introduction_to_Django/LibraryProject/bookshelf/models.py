from django.db import models

# Create your models here.
class Book:
    # Constructor method to initialize attributes
    def __init__(self, title, author, publication_year):
        self.title = title #instance variable
        self.author = author #instance variable 
        self.publication_year = publication_year #instance variable
    