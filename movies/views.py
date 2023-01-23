from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from movies.models import Movies
from movies.serializer import MoviesSerializer
from .permissions import UserOrReadOnly


class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"


class MoviesListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """
    view for creating and listing moviess
    """
    serializer_class = MoviesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    queryset = Movies.objects.filter(private=0)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MovieUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    """
    view for get, update, and destroy a movie
    """
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()
    permission_classes = [UserOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        movies = Movies.objects.filter(user_id=user)
        return movies

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    


class UserMoviesAPIView(ListAPIView):
    """
    view for get all movies from user
    """
    permission_classes = [IsAuthenticated]
    serializer_class= MoviesSerializer

    def get_queryset(self):
        user = self.request.user
        movies = Movies.objects.filter(user_id=user)
        return movies