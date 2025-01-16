# import graphene
# from graphene_django.types import DjangoObjectType
# from .models import Book
#
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#
# class CreateBook(graphene.Mutation):
#     class Arguments:
#         title = graphene.String(required=True)
#         author = graphene.String(required=True)
#
#     book = graphene.Field(BookType)
#
#     def mutate(self, title, author):
#         book = Book.objects.create(title=title, author=author)
#         return CreateBook(book=book)
#
# class Mutation(graphene.ObjectType):
#     create_book = CreateBook.Field()
