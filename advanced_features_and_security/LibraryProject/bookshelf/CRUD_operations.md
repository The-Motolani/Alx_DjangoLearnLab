# CRUD OPERATIONS

## Create

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author = "Georger Orwell", publication_year = 1949)
```
<!--Expected output ... -->

## Retrieve

book = Book.objects.all()

## Update

```python
book = Book.objects.get(title="1984")
book.title="Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
```
<!---->

## Delete

```python
book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# comment
```
