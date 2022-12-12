from django.urls import path, include
from note import views
urlpatterns = [
    path('all-notes/', views.note_list, 'note_list_url'),
    path('note-content', views.note_content, 'note_content_url')
]