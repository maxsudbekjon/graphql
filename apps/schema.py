# import graphene
# from graphene_django import DjangoObjectType
#
# from apps.models import Book
#
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = ("id", "title",'author')
#
# class Query(graphene.ObjectType):
#     books = graphene.List(BookType)
#     book_by_id = graphene.Field(BookType, id=graphene.String())
#
#     def resolve_books(root, info, **kwargs):
#         # Querying a list
#         return Book.objects.all()
#
#     def resolve_book_by_id(root, info, id):
#         # Querying a single question
#         return Book.objects.get(pk=id)
# schema = graphene.Schema(query=Query)
import graphene
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError

from .models import Book, Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
# Query: Kitoblarni olish uchun root query
# class Query(graphene.ObjectType):
#     all_books = graphene.List(BookType)  # Barcha kitoblarni olish
#     book_by_id = graphene.Field(BookType, id=graphene.ID(required=True))  # ID orqali olish
#
#     def resolve_all_books(self, info, **kwargs):
#         return Book.objects.all()
#
#     def resolve_book_by_id(self, info, id):
#         try:
#             return Book.objects.get(pk=id)
#         except Book.DoesNotExist:
#             return None

# Mutation'ni ulash
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, author):
        book = Book.objects.create(title=title, author=author)
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

#
from django.db.models import Q


class Search(graphene.ObjectType):
    search_books = graphene.List(BookType, keyword=graphene.String())

    def resolve_search_books(self, info, keyword=None):
        if keyword:
            search = (Q(title__icontains=keyword) |
                     Q(title__iexact=keyword) |
                     Q(title__istartswith=keyword) |
                     Q(title__contains=keyword) |
                     Q(author__icontains=keyword) |
                     Q(author__iexact=keyword) |
                     Q(author__istartswith=keyword) |
                     Q(author__contains=keyword))
            return Book.objects.filter(search)

        return Book.objects.all()
# class Query(graphene.ObjectType):
#     get_author_with_books = graphene.Field(AuthorType, id=graphene.ID(required=True))
#
#     def resolve_get_author_with_books(self, info, id):
#         try:
#             return Author.objects.get(pk=id)
#         except Author.DoesNotExist:
#             return None
# class Query(graphene.ObjectType):
#     books = graphene.List(BookType, limit=graphene.Int(), page=graphene.Int())
#
#     def resolve_books(self, info, limit=None, page=None):
#         books = Book.objects.all()
#         if page:
#             books = books[page+1:]
#         if limit:
#             books = books[:limit]
#         return books
# class Query(graphene.ObjectType):
#     books = graphene.List(BookType, title=graphene.String())
#
#     def resolve_books(self, info, title=None):
#         if title is None:
#             raise GraphQLError('Title is required')
#
#         return Book.objects.filter(title__icontains=title)


schema = graphene.Schema(query=Query, mutation=Mutation)


