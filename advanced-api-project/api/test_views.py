from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user for authentication tests
        self.user = User.objects.create_user(username="tester", password="pass1234")

        # Create sample authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Jane Smith")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2000,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Beta Stories",
            publication_year=2010,
            author=self.author2
        )

        self.client = APIClient()

    # ------------------------------------------
    # LIST VIEW TESTS
    # ------------------------------------------

    def test_list_books(self):
        """Ensure books list endpoint returns all books."""
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_title(self):
        response = self.client.get(reverse("book_list"), {"title": "Alpha Book"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    def test_search_books(self):
        response = self.client.get(reverse("book_list"), {"search": "Beta"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Beta Stories")

    def test_order_books_by_year(self):
        response = self.client.get(reverse("book_list"), {"ordering": "publication_year"})
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    # ------------------------------------------
    # CREATE VIEW TESTS
    # ------------------------------------------

    def test_create_book_unauthenticated(self):
        """Unauthenticated user must NOT be able to create books."""
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(reverse("book_create"), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="pass1234")

        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(reverse("book_create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ------------------------------------------
    # DETAIL VIEW TEST
    # ------------------------------------------

    def test_retrieve_book_detail(self):
        response = self.client.get(reverse("book_detail", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # ------------------------------------------
    # UPDATE VIEW TESTS
    # ------------------------------------------

    def test_update_book_unauthenticated(self):
        data = {"title": "New Title"}
        response = self.client.patch(reverse("book_update", args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username="tester", password="pass1234")

        data = {"title": "Updated Title"}
        response = self.client.patch(reverse("book_update", args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ------------------------------------------
    # DELETE VIEW TESTS
    # ------------------------------------------

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(reverse("book_delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username="tester", password="pass1234")

        response = self.client.delete(reverse("book_delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
