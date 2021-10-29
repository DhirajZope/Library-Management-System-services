from django.urls import path
from .views import LibraryApiView


urlpatterns = [
    path('library/', LibraryApiView.as_view(), name='library'),
    path('library/<int:id>', LibraryApiView.as_view(), name='library'),
]