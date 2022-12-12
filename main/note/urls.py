from django.urls import path, include
from note import views
urlpatterns = [
    path('all-notes/', ),
    path('note-content', include(''))
]