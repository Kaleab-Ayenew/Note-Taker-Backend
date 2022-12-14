from django.urls import path, include
from note import views
urlpatterns = [
    path('my-notes/', views.note_list, name='note_list_url'),
    path('note-content/', views.note_content, name='note_content_url')
]