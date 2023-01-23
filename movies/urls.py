from .views import MoviesListCreateView, MovieUpdateDeleteView, UserMoviesAPIView
from django.urls import path

urlpatterns = [
    path('', MoviesListCreateView.as_view(), name='create'),
    path("my_movies/", UserMoviesAPIView.as_view(), name="my_movies"),
    path("<int:pk>/", MovieUpdateDeleteView.as_view(), name="movie_detail"),
]