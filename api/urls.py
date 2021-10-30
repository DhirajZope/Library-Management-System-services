from django.urls import path
from .views import LibraryApiView, ListAllBooks


urlpatterns = [
    path('library/', ListAllBooks.as_view(), name='library'),
    path('library/<int:id>', LibraryApiView.as_view(), name='library'),
    path('library/new/', LibraryApiView.as_view(), name='new_post'),
]