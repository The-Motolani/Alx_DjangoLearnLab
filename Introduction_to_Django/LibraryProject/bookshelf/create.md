# CRUD OPERATIONS

## Create

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author = "Georger Orwell", publication_year = 1949)
```
<!--Expected output ... -->
