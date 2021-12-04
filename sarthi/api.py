from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class BookList(APIView):
    def get(self, request):
        model = book.objects.all()
        serializer = BookSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get_book(self, book_id):
        try:
            model = book.objects.get(id=book_id)
            return model
        except book.DoesNotExist:
            return
        # Response(f'book with{book_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)

    def get(self, request, book_id):
        if not self.get_book(book_id):
            return Response(f'book with{book_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(self.get_book(book_id))
        return Response(serializer.data)

    def put(self, request, book_id):
        if not self.get_book(book_id):
            return Response(f'book with{book_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(self.get_user(book_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        if not self.get_book(book_id):
            return Response(f'book with{book_id} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_book(book_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
